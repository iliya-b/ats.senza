
import importlib
import sys
import time
import uuid

import aioamqp
from aiohttp import web


class SenzaApp(web.Application):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config

    async def setup(self, *args, **kw):
        await self.setup_amqp()
        self.setup_routes()

    async def amqp_connection(self):
        host = self.config['amqp']['hostname']
        port = 5672
        login = self.config['amqp']['username']
        password = self.config['amqp']['password']

        try:
            return await aioamqp.connect(host=host, port=port, login=login,
                                         password=password, virtualhost='/')
        except ConnectionRefusedError:
            self.logger.error('Connection refused @ amqp://%s:%s', host, port)
            raise

    async def setup_amqp(self):
        self.logger.debug('Set up AMQP..')
        try:
            transport, protocol = await self.amqp_connection()
        except ConnectionRefusedError:
            time.sleep(3)
            sys.exit(1)
        self.amqp_publish_channel = await protocol.channel()

    def setup_routes(self):
        for module in [
            importlib.import_module('ats.senza.server.protocol.%s' % name)
            for name in [
                'accelerometer',
                'camera',
                'magnetometer',
                'orientation',
                'gyroscope',
                'gravity',
                'linear_acc',
                'rotation_vector',
                'temperature',
                'proximity',
                'light',
                'pressure',
                'relative_humidity',
                'battery',
                'gps',
                'recorder',
            ]
        ]:
            p = module.Producer()
            self.router.add_route('GET', '/android/sensors/%s' % p.event_name, p.get_handler)
            self.router.add_route('POST', '/android/sensors/%s/{avm_id}' % p.event_name, p.post_handler)
        for name in ['sms', 'call', 'signal', 'network', 'registration']:
            module = importlib.import_module('ats.senza.server.protocol.gsm.%s' % name)
            p = module.Producer()
            self.router.add_route('GET', '/android/sensors/gsm/%s' % name, p.get_handler)
            self.router.add_route('POST', '/android/sensors/gsm/%s/{avm_id}' % name, p.post_handler)

    async def send_event(self, routing_key, payload, paylog):
        properties = {
            'message_id': uuid.uuid1().hex,
            'timestamp': int(time.time()),
            'content_type': 'application/octet-stream',
            'delivery_mode': 2,
        }
        chan = self.amqp_publish_channel

        self.logger.debug('sending event %s to %s - %s', paylog, routing_key, properties)
        await chan.publish(payload=payload,
                           exchange_name='android-events',
                           routing_key=routing_key,
                           properties=properties)
