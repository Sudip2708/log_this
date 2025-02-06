from prompt_toolkit.styles import Style

def dialog_style() -> Style:
    """
    Vrací styl pro dialogová okna.

    Returns:
        Style: Nastavení stylů pro dialogová okna.
    """
    return Style.from_dict({
        'dialog':           'fg:white bg:blue',
        'dialog.body':      'fg:white bg:black',
        'dialog.border':    'fg:green',
        'selected':         'fg:black bg:white',
        'key.name':         'fg:bold italic',
        'key.info':         'fg:gray'
    })
