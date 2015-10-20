
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the light sensor emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('light', type=float, help='light level (float)')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'light': parsed_args.light,
        }

        self.app.do_post('android', 'sensors', 'light', avm_id,
                         json=payload)
