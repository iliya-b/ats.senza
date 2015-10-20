
from . import gsm
from ..sensors_packet_pb2 import sensors_packet as pkt


class Producer(gsm.Producer):
    schema = {
        'type': 'object',
        'properties': {
            'action': {
                'enum': ['receive', 'accept', 'cancel', 'hold']
            },
            'phone_number': {
                'type': 'string'
            }
        }
    }

    @staticmethod
    def pack(*, request, action, phone_number):
        return pkt(
            gsm=pkt.GSMPayload(
                action_type=pkt.GSMPayload.GSMActionType.Value(gsm.ACTION_MAPPER['call'][action]),
                phone_number=phone_number)
        )
