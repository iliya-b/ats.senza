
import cliff.command


class Command(cliff.command.Command):
    """Send a command to start or stop video recording"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('filename', help='filename')
        ap.add_argument('start', type=int, help='start')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'filename': parsed_args.filename,
            'start': parsed_args.start,
        }

        self.app.do_post('android', 'sensors', 'recording', avm_id,
                         json=payload)
