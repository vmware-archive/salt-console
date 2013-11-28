# Import sconsole libs
import sconsole.manager
import sconsole.parser

def start():
    opts = sconsole.parser.parse()
    manager = sconsole.manager.Manager(opts)
    manager.start()
