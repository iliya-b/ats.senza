
from . import gsm
from ..sensors_packet_pb2 import sensors_packet as pkt


class Producer(gsm.Producer):
    schema = {
        'type': 'object',
        'properties': {
            'type': {
                'enum': ['home', 'denied', 'searching', 'roaming', 'none']
            }
        }
    }

    @staticmethod
    def pack(*, request, type):
        return pkt(
            gsm=pkt.GSMPayload(
                action_type=pkt.GSMPayload.GSMActionType.Value(gsm.ACTION_MAPPER['registration']),
                registration=type)
        )
