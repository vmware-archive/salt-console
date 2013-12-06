'''
Holds static data components, like the palette
'''
# Import python libs
import pprint

# Import third party libs


# Import sconsole libs
import sconsole.widgets
import sconsole.widgets.tree


def job_seed(root_txt='Jobs'):
    '''
    '''
    data = [(sconsole.widgets.FocusText(root_txt), [])]
    return sconsole.widgets.tree.SimpleTree(data)


def tree_seed():
    return {'jids': [
                    {'_|-76789876543456787654': [{'localhost': {'return': True}},
                                                 {'otherhost': {'return': True}}],},
                    {'_|-76789876543456787655': [{'localhost': {'return': True}},
                                                 {'otherhost': {'return': True}}],},
                ],
           }


def msg(msg, logfile='console_log.txt'):
    '''
    Send a message to a logfile, defaults to console_log.txt.
    This is useful to replace a print statement since curses does put
    a bit of a damper on this
    '''
    with open(logfile, 'a+') as fp_:
        fp_.write('{0}\n'.format(pprint.pformat(msg)))


def get_palette(theme='std'):
    '''
    Return the preferred palette theme

    Themes:
    std
        The standard theme used by the console
    '''
    if theme == 'bright':
        return [
                ('banner', 'white', 'dark blue'),
                ('body', 'black', 'light gray'),
                ('focus', 'black', 'dark blue', 'standout'),
                ('bars', 'dark blue', 'light gray', ''),
                ('arrowtip', 'light blue', 'light gray', ''),
                ('connectors', 'light red', 'light gray', ''),
               ]
    else:
        return [
                ('banner', 'white', 'dark blue'),
                ('body', 'white', 'black'),
                ('focus', 'white', 'dark blue', 'standout'),
                ('bars', 'dark blue', 'light gray', ''),
                ('arrowtip', 'light blue', 'light gray', ''),
                ('connectors', 'light red', 'light gray', ''),
               ]
