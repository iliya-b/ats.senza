
import struct

from . import base


class Producer(base.Producer):
    event_name = 'recording'

    schema = {
        'type': 'object',
        'properties': {
            'filename': {
                'type': 'string',
            },
            'start': {
                'enum': [0, 1],
            },
        },
        'required': ['filename', 'start'],
    }

    @staticmethod
    def pack(*, request, filename, start):
        filename = filename.encode('utf8')
        return struct.pack('>HH%ssb' % len(filename),
                           len(filename) + 5,
                           len(filename),
                           filename,
                           start)
