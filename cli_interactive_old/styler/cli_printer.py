from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text

from singleton_meta import SingletonMeta
from styler.cli_styles import PRINT_STYLES, DIALOG_STYLES


class CliPrinter(metaclass=SingletonMeta):

    PRINT_STYLES = PRINT_STYLES
    DIALOG_STYLES = DIALOG_STYLES

    def __init__(self):
        """Inicializuje styly pro tisk"""
        self._print_style = Style.from_dict(self.PRINT_STYLES)
        self._dialog_style = Style.from_dict(self.DIALOG_STYLES)

    @property
    def print_style(self):
        """Vrací styl pro běžný tisk"""
        return self._print_style

    @property
    def dialog_style(self):
        """Vrací styl pro dialogy"""
        return self._dialog_style

    def cli_print(self, style, text):
        """
        Vypíše text s daným stylem.

        :param style: Název stylu (např. "title", "default")
        :param text: Řetězec, který se má vypsat
        """
        if style not in self.PRINT_STYLES:
            print(text)
        else:
            styled_text = FormattedText([("class:" + style, text)])
            print_formatted_text(styled_text, style=self.print_style)


cli_printer = CliPrinter()
cli_print = cli_printer.cli_print
cli_style = cli_printer.dialog_style