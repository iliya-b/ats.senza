
import cliff.command
import json


class Schema(cliff.command.Command):
    """Display JSON schema for a given subcommand"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('name', help='command name')
        return ap

    def take_action(self, parsed_args):
        r = self.app.do_get('android', 'sensors', parsed_args.name)

        print(json.dumps(r.json(), indent=4))
