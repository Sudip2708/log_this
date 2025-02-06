from dataclasses import dataclass
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text


@dataclass
class StyleConfig:
    """Konfigurace pro jednotlivé typy zpráv"""
    symbol: str = ''
    intro_style: str = ''
    info_style: str = ''
    hint_style: str = ''


class ConfigStyler:
    """Centrální správa stylů pro LogThis knihovnu"""

    STYLE_CONFIGS = {
        'title':    StyleConfig("", "fg:blue bold underline"),
        'info':     StyleConfig("ℹ", "fg:blue"),
        'warning':  StyleConfig("⚠", "fg:yellow bold"),
        'error':    StyleConfig("✘", "fg:red bold"),
        'critical': StyleConfig("✘", "fg:red bold italic"),
        'success':  StyleConfig("✔", "fg:green"),
        'help':     StyleConfig("?", "fg:cyan")
    }

    def __init__(self):
        # Styly pro dialogy
        self.dialog_style = Style.from_dict({
            'dialog':           'fg:white bg:blue',
            'dialog.body':      'fg:white bg:black',
            'dialog.border':    'fg:green',
            'selected':         'fg:black bg:white',
            'key.name':         'fg:bold italic',
            'key.info':         'fg:gray'
        })


        # Styly pro CLI výstupy
        style_dict = {}
        for style_name, config in self.STYLE_CONFIGS.items():
            style_dict.update({
                f'{style_name}.info': config.info_style,
                f'{style_name}.detail': config.detail_style,
                f'{style_name}.hint': config.hint_style
            })
        self.cli_style = Style.from_dict(style_dict)

    def get_dialog_style(self) -> Style:
        """Vrátí styl pro dialogy"""
        return self.dialog_style

    def print_message(
            self,
            style: str,
            info: str = None,
            detail: str = None,
            hint: str = None
    ) -> None:
        """
        Vytiskne stylovanou zprávu do konzole.

        Args:
            style: Typ zprávy ('info', 'warning', etc.)
            info: Hlavní informační text
            detail: Doplňující informace
            hint: Nápověda
        """
        config = self.STYLE_CONFIGS.get(style)
        texts = []

        if info:
            texts.append((
                f'class:{style}.info',
                f'{config.symbol} {info}\n'
            ))
        if detail:
            texts.append((
                f'class:{style}.detail',
                f'{detail}\n'
            ))
        if hint:
            texts.append((
                f'class:{style}.hint',
                f'{hint}'
            ))

        print_formatted_text(
            FormattedText(texts),
        )

styler = ConfigStyler()
dialog_style = styler.dialog_style
cli_print = styler.print_message


"""
## Použití: 

styler = LogThisStyler()

# V dialogových oknech
radiolist_dialog(
    title='Hlavní menu',
    text='Vyberte požadovaný úkon:',
    values=[...],
    style=styler.get_dialog_style()
).run()

# Pro CLI výstupy
styler.print_message(
    style='info',
    intro='Konfigurace byla úspěšně změněna',
    info='Hodnota "max_level" byla nastavena na "DEBUG"',
    hint='Pro zobrazení aktuální konfigurace použijte příkaz "log-this config show"'
)
"""