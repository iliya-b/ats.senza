
from os.path import realpath
from pathlib import Path
import struct

from . import base


class Producer(base.Producer):
    event_name = 'camera'

    schema = {
        'type': 'object',
        'properties': {
            'file_id': {
                'type': 'string'
            }
        },
        'required': ['file_id']
    }

    @staticmethod
    def pack(*, request, file_id):
        # Check relative paths
        if not realpath(file_id).startswith(realpath('.')):
            raise Exception('Wrong path')
        video_path = request.app.config['camera']['video_path']
        file_path = Path(video_path, file_id).as_posix().encode("utf-8")
        len_file = len(file_path)
        return struct.pack('>H%ss' % len_file,
                           len_file,
                           file_path)
