from ._print_styled import PrintStyledMixin
from ._handle_single_argument import HandleSingleArgumentMixin
from ._handle_styled_text import HandleStyledTextMixin
from ._format_text import FormatTextMixin
from .cli_print import CliPrintMixin

__all__ = [

    "FormatTextMixin",  # _format_text()
    # Metoda formátuje text podle zadaného stylu
    # Používá atributy: 'print_styles_dict'

    "PrintStyledMixin",  # _print_styled()
    # Metoda vytiskne formátovaný text.
    # Používá atributy: '_print_style'

    "HandleSingleArgumentMixin",  # _handle_single_argument()
    # Metoda zpracuje případ, kdy je předán jeden argument
    # Používá metody: _format_text(), _print_styled()

    "HandleStyledTextMixin",  # _handle_styled_text()
    # Metoda zpracuje případ, kdy jsou předány dva argumenty: styl a text
    # Používá metody: _format_text(), _print_styled()

    "CliPrintMixin",  # print()
    # Univerzální metoda pro tisk textu s různými styly.
    # Používá metody: _handle_single_argument(), _handle_styled_text()

]