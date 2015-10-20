
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the GSM emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('type', help='Network type (one of gsm, gprs, edge, '
                                     'edge, cdma, hspa, hsupa, umts, hsdpa, '
                                     'evdo, lte')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'type': parsed_args.type,
        }

        self.app.do_post('android', 'sensors', 'gsm', 'network', avm_id,
                         json=payload)
