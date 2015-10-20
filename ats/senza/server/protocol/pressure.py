
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.SensorProducer):
    event_name = 'pressure'

    schema = {
        'type': 'object',
        'properties': {
            'pressure': {
                'type': 'number',
                'minimum': 0,
            },
        },
        'required': ['pressure']
    }

    @staticmethod
    def pack(*, request, pressure):
        return pkt(
            sensor_pressure=pkt.SensorPressurePayload(
                pressure=pressure,
            )
        )
