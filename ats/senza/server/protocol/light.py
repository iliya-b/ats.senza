
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.SensorProducer):
    event_name = 'light'

    schema = {
        'type': 'object',
        'properties': {
            'light': {
                'type': 'number',
                'minimum': 0
            },
        },
        'required': ['light']
    }

    @staticmethod
    def pack(*, request, light):
        return pkt(
            sensor_light=pkt.SensorLightPayload(
                light=light,
            )
        )
