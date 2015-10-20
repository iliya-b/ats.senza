
import cliff.command


class Command(cliff.command.Command):
    """Send a gsm network command to the GSM emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('strength', type=int, help='Signal strength (between 0 and 4)')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'strength': parsed_args.strength,
        }

        self.app.do_post('android', 'sensors', 'gsm', 'signal', avm_id,
                         json=payload)
