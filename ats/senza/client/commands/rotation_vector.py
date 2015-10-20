
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the rotation vector sensor emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('x', type=float, help='rotation vector: x (float)')
        ap.add_argument('y', type=float, help='rotation vector: y (float)')
        ap.add_argument('z', type=float, help='rotation vector: z (float)')
        ap.add_argument('angle', type=float, help='rotation vector: angle (float)')
        ap.add_argument('accuracy', type=float, help='rotation vector: accuracy (float)')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'x': parsed_args.x,
            'y': parsed_args.y,
            'z': parsed_args.z,
            'angle': parsed_args.angle,
            'accuracy': parsed_args.accuracy,
        }

        self.app.do_post('android', 'sensors', 'rotation_vector', avm_id,
                         json=payload)
