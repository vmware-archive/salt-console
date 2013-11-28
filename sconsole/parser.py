# Import python libs
import optparse

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
    options, args = parser.parse_args()
    return options.__dict__
