
from . import gsm
from ..sensors_packet_pb2 import sensors_packet as pkt


class Producer(gsm.Producer):
    schema = {
        'type': 'object',
        'properties': {
            'strength': {
                'enum': [0, 1, 2, 3, 4]
            }
        }
    }

    @staticmethod
    def pack(*, request, strength):
        return pkt(
            gsm=pkt.GSMPayload(
                action_type=pkt.GSMPayload.GSMActionType.Value(gsm.ACTION_MAPPER['signal']),
                signal_strength=strength)
        )
