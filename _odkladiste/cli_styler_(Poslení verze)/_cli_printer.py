from._cli_styler import CliStyler
from._styles_settings import StyleItems
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText


class StylePrinter:


    def __init__(self, styler: CliStyler):
        self._styler = styler  # Uložíme instanci CliStyler


    def __getattr__(self, attr):
        """
        Přesměruje přístup k atributům na _styler.
        Umožní volání: cli_print.error.title("Text").
        """
        item = getattr(self._styler, attr)  # Získá atribut ze `CliStyler`

        if isinstance(item, StyleItems):  # Pokud je to styl, vrátíme ho
            return item

        raise AttributeError(
            f"'{self.__class__.__name__}' nemá atribut '{attr}'")


    def __call__(self, style_item: tuple):
        """Automaticky vytiskne ostylovaný text při zavolání"""
        print_formatted_text(FormattedText([style_item]))



