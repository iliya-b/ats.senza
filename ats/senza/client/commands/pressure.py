
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the pressure sensor emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('pressure', type=float, help='pressure (float)')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'pressure': parsed_args.pressure,
        }

        self.app.do_post('android', 'sensors', 'pressure', avm_id,
                         json=payload)
