# file: ansi_formatter.py
from typing import Union, Optional
from ._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS, LEVELS_COLORS, LEVELS_COLORS_SMALL

class StyleBuilder:
    """Helper class for chaining style methods."""

    def __init__(self, formatter: 'ANSIFormatter', text: str):
        self._formatter = formatter
        self._text = text
        self._styles = list[]

    def __str__(self):
        if self._styles:
            return self._formatter.apply_styles(self._text, self._styles)
        else:
            return self._text

    def color(self, colors) -> 'StyleBuilder':
        for i in colors:
            self._styles.append(i)
        return self

    # Další metody pro styly...
    def style(self, styles) -> 'StyleBuilder':
        for i in styles:
            self._styles.append(i)
        return self


class ANSIFormatter:
    """Class for formatting text with ANSI escape sequences."""

    _instance: Optional['ANSIFormatter'] = None
    ESCAPE = "\033["
    _text_set = set()

    def __new__(cls) -> 'ANSIFormatter':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Inicializace proběhne pouze jednou díky Singletonu
        if not hasattr(self, '_initialized'):
            self.reset = f"{self.ESCAPE}0m"
            self._config_dict = {**TEXT_STYLES, **TEXT_COLORS, **BACKGROUND_COLORS, **LEVELS_COLORS, **LEVELS_COLORS_SMALL}
            self._register_attributes()
            self._initialized = True

    def _register_attributes(self):
        """Dynamically register text styles and colors as attributes."""
        for name, code in self._config_dict.items():
            setattr(self, name, f"{self.ESCAPE}{code}m")


    def set(self, text: str) -> StyleBuilder:
        """
        Start style chain for text.

        Usage:
            set("Hello").color("ERROR").style(bold)
        """
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
                style_codes.append(str(i).split('[')[-1].rstrip('m'))

        # Navrácení formátovaného textu
        if not ansi_codes:
            return text
        return f"{self.ESCAPE}{';'.join(style_codes)}m{text}{self.reset}"


# Vytvoření singleton instance
inst = ANSIFormatter()
style = inst.set

# Ukázka zápisu:
# f'{style(%(levelname)s).set(bold).color(%(levelname)s)}'