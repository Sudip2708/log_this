from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text

from abc_helper import AbcSingletonMeta
from ._cli_styles import PRINT_STYLES, DIALOG_STYLES


class CliPrinter(metaclass=AbcSingletonMeta):

    PRINT_STYLES = PRINT_STYLES
    DIALOG_STYLES = DIALOG_STYLES

    def __init__(self):
        """Inicializuje styly pro tisk"""
        self._print_style = Style.from_dict(self.PRINT_STYLES)
        self._dialog_style = Style.from_dict(self.DIALOG_STYLES)

    @property
    def style(self):
        """Vrací styl pro dialogy"""
        return self._dialog_style

    def print(self, style, text):
        """
        Vypíše text s daným stylem.

        :param style: Název stylu (např. "title", "default")
        :param text: Řetězec, který se má vypsat
        """
        if style not in self.PRINT_STYLES:
            print(text)
        else:
            styled_text = FormattedText([("class:" + style, text)])
            print_formatted_text(
                styled_text,
                style=self._print_style
            )


cli_printer = CliPrinter()
cli_print = cli_printer.print
cli_style = cli_printer.style