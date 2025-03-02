from prompt_toolkit.styles import Style

from abc_helper import AbcSingletonMeta
from .styles.dialog_styles import DIALOG_STYLES
from .styles.print_styles import PRINT_STYLES
from .mixins import (
    FormatTextMixin,
    PrintStyledMixin,
    HandleSingleArgumentMixin,
    HandleStyledTextMixin,
    CliPrintMixin,
)


class CliStyler(

    FormatTextMixin,  # _format_text()
    # Metoda formátuje text podle zadaného stylu
    # Používá atributy: 'print_styles_dict'

    PrintStyledMixin,  # _print_styled()
    # Metoda vytiskne formátovaný text.
    # Používá atributy: '_print_style'

    HandleSingleArgumentMixin,  # _handle_single_argument()
    # Metoda zpracuje případ, kdy je předán jeden argument
    # Používá metody: _format_text(), _print_styled()

    HandleStyledTextMixin,  # _handle_styled_text()
    # Metoda zpracuje případ, kdy jsou předány dva argumenty: styl a text
    # Používá metody: _format_text(), _print_styled()

    CliPrintMixin,  # cli_print()
    # Univerzální metoda pro tisk textu s různými styly.
    # Používá metody: _handle_single_argument(), _handle_styled_text()

    metaclass=AbcSingletonMeta

):
    # Definice atributů použitých v mixinech
    print_styles_dict = None
    _print_style = None
    _dialog_style = None

    def __init__(self):
        """Inicializuje styly pro tisk"""
        self.print_styles_dict = PRINT_STYLES
        self._print_style = Style.from_dict(self.print_styles_dict)
        self._dialog_style = Style.from_dict(DIALOG_STYLES)

    @property
    def cli_style(self):
        """Vrací styl pro dialogy"""
        return self._dialog_style

    def add_style(self, style_name: str, style_definition: str) -> None:
        """Metoda pro dočasné přidání nového stylu"""
        self.print_styles_dict[style_name] = style_definition
        self._print_style = Style.from_dict(self.print_styles_dict)


styler = CliStyler()
cli_style = styler.cli_style
add_style = styler.add_style
cli_print = styler.cli_print