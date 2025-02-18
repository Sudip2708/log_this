# style_classr.py
from prompt_toolkit import print_formatted_text

from .constants.signs import END_LINE


class StyleClass:
    """Reprezentuje ostylovaný text a poskytuje metody pro jeho získání a vypsání."""

    def __init__(self, symbol: str, style: str):
        self.symbol = symbol
        self.style = style

    def get(self, text: str) -> tuple:
        """Vrátí nenaformátovaný tuple (symbol, ostylovaný text)."""
        return self.style, f"{self.symbol}{text}{END_LINE}"

    def print(self, text: str):
        """Vytiskne ostylovaný text do konzole."""
        print_formatted_text([self.get(text)])