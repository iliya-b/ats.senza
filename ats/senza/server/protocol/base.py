
import json
import jsonschema
from http import HTTPStatus

from aiohttp import web


class Producer:
    event_name = None
    routing_key_tmpl = 'android-events.{avm_id}.{event_name}'
    schema = {}

    async def post_handler(self, request):
        avm_id = request.match_info['avm_id']
        params = await request.json()
        try:
            jsonschema.validate(params, self.schema)
        except jsonschema.ValidationError as exc:
            return web.Response(
                status=HTTPStatus.BAD_REQUEST,
                text=json.dumps({'error': str(exc), 'schema': self.schema}, indent=4)
            )

        pkt = self.pack(request=request, **params)

        try:
            # protobuf?
            payload = pkt.SerializeToString()
            paylog = ' '.join(
                line.strip()
                for line in str(pkt).split('\n')
                if line
            )
        except AttributeError:
            payload = pkt
            paylog = params

        routing_key = self.routing_key_tmpl.format(avm_id=avm_id, event_name=self.event_name)

        await request.app.send_event(routing_key=routing_key,
                                     payload=payload,
                                     paylog=paylog)
        return web.Response(status=HTTPStatus.NO_CONTENT)

    async def get_handler(self, request):
        return web.Response(content_type='application/json',
                            text=json.dumps(self.schema, indent=4))

    @staticmethod
    def pack(self, **kw):
        raise NotImplementedError


class SensorProducer(Producer):
    routing_key_tmpl = 'android-events.{avm_id}.sensors.{event_name}'
