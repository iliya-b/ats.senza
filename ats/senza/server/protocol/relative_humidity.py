
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.SensorProducer):
    event_name = 'relative_humidity'

    schema = {
        'type': 'object',
        'properties': {
            'relative_humidity': {
                'type': 'number'
            },
        },
        'required': ['relative_humidity']
    }

    @staticmethod
    def pack(*, request, relative_humidity):
        return pkt(
            sensor_relative_humidity=pkt.SensorRelativeHumidityPayload(
                relative_humidity=relative_humidity,
            )
        )
