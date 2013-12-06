# Import python libs
import optparse

# Import salt libs
import salt.config

def parse():
    '''
    Parse the command line input
    '''
    parser = optparse.OptionParser()
    parser.add_option(
            '--theme',
            dest='theme',
            default='std',
            help='Set the color theme to use from std or bright')
    parser.add_option(
            '-c',
            '--config-dir',
            dest='config_dir',
            default='/etc/salt',
            help='The config dir')
    options, args = parser.parse_args()
    opts = options.__dict__
    opts.update(salt.config.master_config(opts['config_dir']))
    opts['color'] = False
    return opts
