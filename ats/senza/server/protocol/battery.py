
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.Producer):
    event_name = 'battery'

    schema = {
        'type': 'object',
        'properties': {
            'level_percent': {
                'type': 'number',
                'minimum': 1,
                'maximum': 100
            },
            'ac_online': {
                'type': 'integer',
                'minimum': 0,
                'maximum': 1
            },
            'status': {
                'enum': ['CHARGING', 'DISCHARGING', 'NOTCHARGING', 'FULL', 'UNKNOWN'],
            }
        },
        'required': ['ac_online', 'level_percent']
    }

    @staticmethod
    def pack(*, request, level_percent, ac_online, status='CHARGING'):
        battery_full = 50000000

        return pkt(
            battery=pkt.BatteryPayload(
                battery_level=int(battery_full / 100.0 * level_percent),
                battery_full=battery_full,
                battery_status=pkt.BatteryPayload.BatteryStatusType.Value(status),
                ac_online=ac_online
            )
        )
