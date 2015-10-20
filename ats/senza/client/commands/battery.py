
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the battery emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('level_percent', type=int, help='battery level (1-100)')
        ap.add_argument('ac_online', type=int,
                        metavar='ac_online',
                        default=1,
                        choices=[0, 1],
                        help='0=battery; 1=AC')
        ap.add_argument('status',
                        metavar='status',
                        nargs='?',
                        default='CHARGING',
                        choices=[
                            'CHARGING',
                            'DISCHARGING',
                            'NOTCHARGING',
                            'FULL',
                            'UNKNOWN'
                        ],
                        help='One of %(choices)s; default %(default)s')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'level_percent': parsed_args.level_percent,
            'ac_online': parsed_args.ac_online,
            'status': parsed_args.status,
        }

        self.app.do_post('android', 'sensors', 'battery', avm_id,
                         json=payload)
