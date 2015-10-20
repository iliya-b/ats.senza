
from ats.util.options import Option, get_configdict, EnvConfigPrinter


prefix = 'SENZA_'

options = [
    Option('server.listen_address', default='127.0.0.1'),
    Option('server.listen_port', default=8083),
    Option('log.jsonformat', default=False),
    Option('amqp.hostname', default='127.0.0.1'),
    Option('amqp.username', default='guest'),
    Option('amqp.password', default='guest'),
    Option('camera.video_path', default='/data/project/camera/'),
]


def config_get(environ):
    return get_configdict(prefix=prefix,
                          options=options,
                          environ=environ)


def ConfigPrinter():
    return EnvConfigPrinter(prefix=prefix,
                            options=options)
