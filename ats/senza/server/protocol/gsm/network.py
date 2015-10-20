
from . import gsm
from ..sensors_packet_pb2 import sensors_packet as pkt


class Producer(gsm.Producer):
    schema = {
        'type': 'object',
        'properties': {
            'type': {
                'enum': ['gsm', 'gprs', 'edge', 'cdma', 'hspa', 'hsupa',
                         'umts', 'hsdpa', 'evdo', 'lte', 'full']
            }
        }
    }

    @staticmethod
    def pack(*, request, type):
        return pkt(
            gsm=pkt.GSMPayload(
                action_type=pkt.GSMPayload.GSMActionType.Value(gsm.ACTION_MAPPER['network']),
                network=type)
        )
