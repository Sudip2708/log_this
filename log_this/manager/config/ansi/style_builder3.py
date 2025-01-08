# file: ansi_formatter.py
from typing import Union, Optional
from ._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS

class StyleBuilder:
    """Helper class for chaining style methods."""

    def __init__(self, formatter: 'ANSIFormatter', text: str):
        self._formatter = formatter
        self._text = text
        self._styles = []

    def __str__(self):
        if self._styles:
            return self._formatter.apply_styles(self._text, self._styles)
        else:
            return self._text

    def set(self, items):
        for i in items:
            self._styles.append(i)
        return self



class ANSIFormatter:
    """Class for formatting text with ANSI escape sequences."""

    _instance: Optional['ANSIFormatter'] = None
    ESCAPE = "\033["
    LEVELS_COLORS = {
        'ERROR': "31",  # red
        'WARNING': "33",  # yellow
        'INFO': "32",  # green
        'DEBUG': "36",  # cyan
        'CRITICAL': '36;43',  # red with yellow background
    }

    def __new__(cls) -> 'ANSIFormatter':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Inicializace proběhne pouze jednou díky Singletonu
        if not hasattr(self, '_initialized'):
            self.reset = f"{self.ESCAPE}0m"
            self._config_dict = {**TEXT_STYLES, **TEXT_COLORS, **BACKGROUND_COLORS}
            self._register_attributes()
            self._initialized = True

    def _register_attributes(self):
        """Dynamically register text styles and colors as attributes."""
        for name, code in self._config_dict.items():
            setattr(self, name, f"{self.ESCAPE}{code}m")

    def color(self, label_level: str):
        """Metoda pro získání barvy dle levelu labelu"""
        level = label_level.upper()
        return self.LEVELS_COLORS.get(label, "")

    def style(self, text: str) -> StyleBuilder:
        """Metoda pro vytvoření instance StyleBuilder"""
        return StyleBuilder(self, text)

    def apply_styles(self, text: str, styles) -> str:
        """Apply list of styles to text, preserving nested styles."""

        # Detekce již existujících ANSI sekvencí v textu
        if self.ESCAPE in text:
            # Zde by byla logika pro zachování vnořených stylů
            # Pro jednoduchost zatím jen vrátíme text jak je
            return text

        # Aplikace nových stylů
        ansi_codes = []
        for i in styles:

            # Pokud je styl zadán jako str
            if isinstance(i, str) and i in self._config_dict:
                ansi_codes.append(self._config_dict[i])

            # Pokud je styl zadán jako atribut ANSIFormatter
            elif hasattr(self, i):
                ansi_codes.append(str(i).split('[')[-1].rstrip('m'))

        # Navrácení formátovaného textu
        if not ansi_codes:
            return text
        return f"{self.ESCAPE}{';'.join(ansi_codes)}m{text}{self.reset}"


# Vytvoření singleton instance
inst = ANSIFormatter()
style = inst.style
color = inst.color

# Ukázka zápisu:
# f'{style(%(levelname)s).set(bold, color(%(levelname)s))}'