
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.SensorProducer):
    event_name = 'rotation_vector'

    schema = {
        'type': 'object',
        'properties': {
            'x': {
                'type': 'number'
            },
            'y': {
                'type': 'number'
            },
            'z': {
                'type': 'number'
            },
            'angle': {
                'type': 'number'
            },
            'accuracy': {
                'type': 'number'
            }
        },
        'required': ['x', 'y', 'z', 'angle', 'accuracy']
    }

    @staticmethod
    def pack(*, request, x, y, z, angle, accuracy):
        data = [x, y, z, angle, accuracy]
        return pkt(
            sensor_rot_vector=pkt.SensorRotVectorPayload(
                size=len(data),
                data=data
            )
        )
