
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.SensorProducer):
    event_name = 'temperature'

    schema = {
        'type': 'object',
        'properties': {
            'temperature': {
                'type': 'number'
            },
        },
        'required': ['temperature']
    }

    @staticmethod
    def pack(*, request, temperature):
        return pkt(
            sensor_temperature=pkt.SensorTemperaturePayload(
                temperature=temperature,
            )
        )
