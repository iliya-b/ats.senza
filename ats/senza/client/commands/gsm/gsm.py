
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the GSM emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('action_type', help='Action to perform')
        ap.add_argument('phone_number', default="", help='Phone number')
        ap.add_argument('sms_text', default="", help='sms text')
        ap.add_argument('signal_strength', type=int, default=2, help='Set signal strength')
        ap.add_argument('network', default="", help='Set network type')
        ap.add_argument('registration', default="", help='Set network registration')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'action_type': parsed_args.action_type,
            'phone_number': parsed_args.phone_number,
            'network': parsed_args.network,
            'registration': parsed_args.registration,
            'sms_text': parsed_args.sms_text,
            'signal_strength': parsed_args.signal_strength,
        }

        self.app.do_post('android', 'sensors', 'gsm', avm_id,
                         json=payload)
