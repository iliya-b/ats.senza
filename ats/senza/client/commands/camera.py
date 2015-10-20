import cliff.command
import json


class Command(cliff.command.Command):
    """Select a video file to provide as camera input"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('file_id', help='Camera file id')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'file_id': parsed_args.file_id,
        }

        self.app.do_post('android', 'sensors', 'camera', avm_id,
                         data=json.dumps(payload))
