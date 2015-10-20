
from .. import base

ACTION_MAPPER = {
    'call': {
        'receive': 'RECEIVE_CALL',
        'accept': 'ACCEPT_CALL',
        'cancel': 'CANCEL_CALL',
        'hold': 'HOLD_CALL'
    },
    'network': 'SET_NETWORK_TYPE',
    'registration': 'SET_NETWORK_REGISTRATION',
    'signal': 'SET_SIGNAL',
    'sms': 'RECEIVE_SMS'
}


class Producer(base.Producer):
    event_name = 'gsm'
