
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the relative_humidity sensor emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('relative_humidity', type=float, help='relative_humidity (float)')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'relative_humidity': parsed_args.relative_humidity,
        }

        self.app.do_post('android', 'sensors', 'relative_humidity', avm_id,
                         json=payload)
