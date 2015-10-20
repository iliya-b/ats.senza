
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.SensorProducer):
    event_name = 'proximity'

    schema = {
        'type': 'object',
        'properties': {
            'distance': {
                'type': 'number',
                'minimum': 0
            },
        },
        'required': ['distance']
    }

    @staticmethod
    def pack(*, request, distance):
        return pkt(
            sensor_proximity=pkt.SensorProximityPayload(
                distance=distance,
            )
        )
