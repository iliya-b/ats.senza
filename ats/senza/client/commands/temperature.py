
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the thermometer emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('temperature', type=float, help='temperature (float)')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'temperature': parsed_args.temperature,
        }

        self.app.do_post('android', 'sensors', 'temperature', avm_id,
                         json=payload)
