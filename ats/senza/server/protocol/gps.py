
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.Producer):
    event_name = 'gps'

    schema = {
        'type': 'object',
        'properties': {
            'latitude': {
                'type': 'number',
                'minimum': -90,
                'maximum': 90,
            },
            'longitude': {
                'type': 'number',
                'minimum': -180,
                'maximum': 180,
            }
        },
        'required': ['latitude', 'longitude']
    }

    @staticmethod
    def pack(*, request, latitude, longitude):
        return pkt(
            gps=pkt.GPSPayload(
                status=pkt.GPSPayload.GPSStatusType.Value('ENABLED'),
                latitude=latitude,
                longitude=longitude,
                altitude=0,
                bearing=0
            )
        )
