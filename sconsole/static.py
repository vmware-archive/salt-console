'''
Holds static data components, like the palette
'''

def msg(msg, logfile='console_log.txt'):
    '''
    Send a message to a logfile, defaults to console_log.txt.
    This is useful to replace a print statement since curses does put
    a bit of a damper on this
    '''
    with open(logfile, 'a+') as fp_:
        fp_.write(str(msg))


def get_palette(theme='std'):
    '''
    Return the preferred palette theme

    Themes:
    std
        The standard theme used by the console
    '''
    if theme == 'bright':
        return [
                ('banner', 'white', 'dark blue')
               ]
    else:
        return [
                ('banner', 'white', 'dark blue')
               ]
