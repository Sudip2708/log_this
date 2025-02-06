from dataclasses import dataclass
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text

from ._dialog_style import dialog_style



class ConfigStyler:
    """Centrální správa stylů pro LogThis knihovnu"""

    @staticmethod
    def dialog_style() -> Style:
        """
        Vrací styl pro dialogová okna.

        Returns:
            Style: Nastavení stylů pro dialogová okna.
        """
        return dialog_style()





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