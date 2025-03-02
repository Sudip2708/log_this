from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

from ..abc_helper import AbcSingletonMeta


class CLIPrinter(metaclass=AbcSingletonMeta):
    """Dědí z CLIStyler a přidává přímý tisk ostylovaného textu."""

    # Definice singletonu
    def __init__(self, styler):
        if not hasattr(self, "_initialized_printer"):
            self.set_printer_attributes(styler)
            self._initialized_printer = True


    # Nastavení atributů
    def set_printer_attributes(self, styler):
        """Nastaví všechny atributy tak, aby přímo tiskly text."""
        for key in styler.get_styles_keys():
            setattr(self, key,
                    lambda text, style=getattr(self, key):
                    self.print_styled_text(styler.style(text)))


    # Hlavní metoda pro tisk
    @staticmethod
    def print_styled_text(styled_text: tuple):
        """Vytiskne ostylovaný text do konzole."""
        formatted_text = FormattedText([styled_text])
        print_formatted_text(formatted_text)