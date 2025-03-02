print("cli_styler/_style_printer.py")
from._styles_settings import StylesManager, StyleBase
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText


class StylePrinter:


    def __init__(self, style_manager: StylesManager):
        self.style_manager = style_manager  # Uložíme instanci CliStyler

    def __getattr__(self, attr):
        """
        Přesměruje přístup k atributům na _styler.
        Umožní volání: cli_print.error.title("Text").
        """
        item = getattr(self._style_manager, attr)  # Získá atribut ze `CliStyler`

        if isinstance(item, StyleBase):  # Pokud je to styl, vrátíme ho
            return item

        raise AttributeError(
            f"'{self.__class__.__name__}' nemá atribut '{attr}'")

    def __call__(self, style_item):
        """Přijme text nebo stylovaný tuple, naformátuje ho a vytiskne."""
        if isinstance(style_item, str):
            # Použije defaultní styl (intro.title) pro formátování
            style_item = self._style_manager.intro.title(style_item)

        if not isinstance(style_item, tuple):
            raise TypeError(
                "StylePrinter očekává text (str) nebo stylovaný tuple.")

        print_formatted_text(FormattedText([style_item]))




