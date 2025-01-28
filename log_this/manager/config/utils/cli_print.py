from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style

# Definice stylů
STYLES = Style.from_dict({
    'none': '',
    'info': 'fg:green',
    'warning': 'fg:yellow bold',
    'error': 'fg:red bold italic',
    'help': 'fg:cyan underline',
    'success': ''
})

LEVELS_SYMBOLS = {
    'NONE': " ",
    'INFO': "ℹ",
    'WARNING': "⚠",
    'ERROR': "✘",
    'HELP': "",
    'SUCCESS': "✔"
}

# Stylovaný výstup
def cli_print1(style='none', message='\n'):

    # Použití HTML-like syntaxe
    print_formatted_text(
        HTML(
            f'<{style}>{LEVELS_SYMBOLS} {message}</{style}>'
        ),
        style=STYLES
    )

def cli_print2(style='none', message='\n'):

    # Použití FormattedText syntaxe
    print_formatted_text(
        FormattedText([(
            f'class:{style}',
            f'{LEVELS_SYMBOLS} {message}'
        )]),
        style=STYLES
    )


# Definice stylů
STYLES = Style.from_dict({
    'none': '',
    'none.intro': '',
    'none.info': '',
    'none.hint': '',

    'info': '',
    'info.intro': 'fg:green',
    'info.info': '',
    'info.hint': '',

    'warning': '',
    'warning.intro': 'fg:yellow bold',
    'warning.info': '',
    'warning.hint': '',

    'error': '',
    'error.intro': 'fg:red bold italic',
    'error.info': '',
    'error.hint': '',

    'critical': '',
    'critical.intro': '',
    'critical.info': '',
    'critical.hint': '',

    'help': '',
    'help.intro': 'fg:cyan underline',
    'help.info': '',
    'help.hint': '',

    'success': '',
    'success.intro': '',
    'success.info': '',
    'success.hint': '',
})

def cli_print3(
        style='none',
        intro=None,
        info=None,
        hint=None
):

    texts_set = []

    if intro:
        texts_set.append(
            (f'class:{style}.intro', f'{LEVELS_SYMBOLS} {intro}')
        )

    if info:
        texts_set.append(
            (f'class:{style}.info', f'{info}')
        )

    if hint:
        texts_set.append(
            (f'class:{style}.hint', f'{hint}')
        )

    # Použití FormattedText syntaxe
    print_formatted_text(
        FormattedText(texts_set),
        style=STYLES
    )
