
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the gyroscope emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('azimuth', type=float, help='azimuth (float)')
        ap.add_argument('pitch', type=float, help='pitch (float)')
        ap.add_argument('roll', type=float, help='roll (float)')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'azimuth': parsed_args.azimuth,
            'pitch': parsed_args.pitch,
            'roll': parsed_args.roll,
        }

        self.app.do_post('android', 'sensors', 'gyroscope', avm_id,
                         json=payload)
