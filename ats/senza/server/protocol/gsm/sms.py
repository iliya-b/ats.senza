
from . import gsm
from ..sensors_packet_pb2 import sensors_packet as pkt


class Producer(gsm.Producer):
    schema = {
        'type': 'object',
        'properties': {
            'phone_number': {
                'type': 'string'
            },
            'text': {
                'type': 'string'
            }
        }
    }

    @staticmethod
    def pack(*, request, phone_number, text):
        return pkt(
            gsm=pkt.GSMPayload(
                action_type=pkt.GSMPayload.GSMActionType.Value(gsm.ACTION_MAPPER['sms']),
                phone_number=phone_number,
                sms_text=text)
        )
