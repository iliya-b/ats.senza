
import sys
import warnings

from cliff.commandmanager import CommandManager

import ats.senza
from ats.client.client import ClientApp


class App(ClientApp):
    default_config_file = 'senza-client.ini'

    def __init__(self):
        super().__init__(
            description='senza',
            version=ats.senza.version,
            command_manager=CommandManager('senza'))


def main(argv=sys.argv[1:]):
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    app = App()
    return app.run(argv)
