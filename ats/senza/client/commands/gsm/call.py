
import cliff.command


class Command(cliff.command.Command):
    """Send a call command to the GSM emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('action', help='Action to perform (one of "receive", '
                                       '"accept", "cancel, "hold")')
        ap.add_argument('phone_number', help='Phone number to use')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'action': parsed_args.action,
            'phone_number': parsed_args.phone_number,
        }

        self.app.do_post('android', 'sensors', 'gsm', 'call', avm_id,
                         json=payload)
