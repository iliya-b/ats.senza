
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.SensorProducer):
    event_name = 'gyroscope'

    schema = {
        'type': 'object',
        'properties': {
            'azimuth': {
                'type': 'number'
            },
            'pitch': {
                'type': 'number'
            },
            'roll': {
                'type': 'number'
            },
        },
        'required': ['azimuth', 'pitch', 'roll']
    }

    @staticmethod
    def pack(*, request, azimuth, pitch, roll):
        return pkt(
            sensor_gyroscope=pkt.SensorGyroscopePayload(
                azimuth=azimuth,
                pitch=pitch,
                roll=roll
            )
        )
