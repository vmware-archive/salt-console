'''
Holds static data components, like the palette
'''
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
