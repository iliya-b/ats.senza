
import cliff.command


class Command(cliff.command.Command):
    """Send a SMS to the GSM emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('phone_number', help='Phone number to use')
        ap.add_argument('text', help='SMS text')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'phone_number': parsed_args.phone_number,
            'text': parsed_args.text,
        }

        self.app.do_post('android', 'sensors', 'gsm', 'sms', avm_id,
                         json=payload)
