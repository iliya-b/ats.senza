
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the gps emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('latitude', type=float, help='latitude (float)')
        ap.add_argument('longitude', type=float, help='longitude (float)')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'latitude': parsed_args.latitude,
            'longitude': parsed_args.longitude,
        }

        self.app.do_post('android', 'sensors', 'gps', avm_id,
                         json=payload)
