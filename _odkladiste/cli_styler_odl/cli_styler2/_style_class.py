# style_classr.py
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from .constants.signs import END_LINE


class StyleClass:
    """Reprezentuje ostylovaný text a poskytuje metody pro jeho získání a vypsání."""

    def __init__(self, symbol: str, style: str):
        self.symbol = symbol
        self.style = style

    def get_styled(self, text: str = None) -> tuple:
        """Vrátí nenaformátovaný tuple (symbol, ostylovaný text)."""
        return self.style, f"{self.symbol}{text}{END_LINE}"

    def print_styled(self, text: str):
        """Vytiskne ostylovaný text do konzole."""

        # Vytvoření formátovaného textu s odkazem na třídu stylu
        formatted_text = FormattedText([
            self.get_styled(text)
        ])

        # Tisk formátovaného textu s vlastním stylem
        print_formatted_text(formatted_text)
