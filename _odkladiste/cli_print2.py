
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

from ._base_calss import StyleItems
from ._error import ErrorStyle
from ._info import InfoStyle
from ._intro import IntroStyle
from ._success import SuccessStyle
from ._warning import WarningStyle


class StylePrinterProxy:
    """Proxy pro přesměrování volání na StyleItems a tisk textu."""

    def __init__(self, style):
        self._style = style  # Uložíme instanci stylu (např. `IntroStyle`)

    def __getattr__(self, attr):
        """Zachytíme volání `cli_print.intro.title` a provedeme tisk."""
        style_item = getattr(self._style, attr)  # Získáme `StyleItems` (např. `title`)

        if not isinstance(style_item, StyleItems):
            raise AttributeError(f"Styl '{attr}' nebyl nalezen.")

        def print_and_return(text):
            """Funkce, která provede tisk a vrátí tuple."""
            style_tuple = style_item(text)
            print_formatted_text(FormattedText([style_tuple]))

        return print_and_return


class CLIPrint:
    """Spravuje všechny styly CLI"""

    def __init__(self, colors, symbols):
        self.error = StylePrinterProxy(ErrorStyle(colors, symbols))
        self.info = StylePrinterProxy(InfoStyle(colors, symbols))
        self.intro = StylePrinterProxy(IntroStyle(colors, symbols))
        self.success = StylePrinterProxy(SuccessStyle(colors, symbols))
        self.warning = StylePrinterProxy(WarningStyle(colors, symbols))



