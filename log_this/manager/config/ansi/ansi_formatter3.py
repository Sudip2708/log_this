# file: ansi_formatter.py
from typing import Union, Optional
from ._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS


class GetInstanceFromStr:
    def __init__(self, text: str):
        self._text = text


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
            self._style_dict = TEXT_STYLES
            self._color_dict = {**TEXT_COLORS, **BACKGROUND_COLORS}
            self._register_attributes()
            self._initialized = True

    def _register_attributes(self):
        """Dynamically register text styles and colors as attributes."""
        for name, code in self._config_dict.items():
            setattr(self, name, f"{self.ESCAPE}{code}m")


    def set(self, text: str):
        if isinstance(text, str):
            self._text = text
        else:
            raise

class Style:

    def __init__(self, text):
        if isinstance(text, str):
            self._text = text
        else:
            raise




    def style(self, *styles: Union[str, Any])
        if styles:
            for style in styles:
                if hasattr(self, style) or (isinstance(style, str) and style in self._style_dict):
                    self._text_set.add(style)

    _level_color_dict = {
        'ERROR': self.red,
        'WARNING': self.yellow,
        'INFO': self.green,
        'DEBUG': self.cyan
    }


    def color(self, *colors: Union[str, Any]):
        if colors:
            for color in colors:
                if hasattr(self, color) or (isinstance(color, str) and color in self._color_dict):
                    self._text_set.add(style)

                elif isinstance(color, str) and color.upper() in self._level_color_dict:
                    self._text_set.add(style)








        if not styles:
            return text

        # Sesbírání všech stylů
        ansi_codes = []
        for style in styles:
            if isinstance(style, str):
                if style in self._config_dict:
                    ansi_codes.append(self._config_dict[style])
            else:
                # Pokud je to atribut třídy (např. style.red)
                code = str(style).split('[')[-1].rstrip('m')
                ansi_codes.append(code)

        # Aplikace stylů na text
        return f"{self.ESCAPE}{';'.join(ansi_codes)}m{text}{self.reset}"






    def set(self, *args: Union[str, 'ANSIAttribute']) -> str:
        """Combine multiple ANSI codes."""
        codes = []
        for arg in args:
            if isinstance(arg, str):
                if arg not in self._config_dict:
                    raise ValueError(f"Unknown style or color: '{arg}'")
                codes.append(self._config_dict[arg])
            else:
                code = str(arg).split('[')[-1].rstrip('m')
                codes.append(code)

        return f"{self.ESCAPE}{';'.join(codes)}m"

    def style(self, text: str, *styles: Union[str, Any]) -> str:
        """
        Apply styles to text.

        Args:
            text: Text to style
            *styles: Style attributes or names (can be both attribute references
                    or strings)

        Examples:
            style('Hello', 'red', 'bold')
            style('Hello', red, bold)
            style('%(levelname)s', color('%(levelname)s'), 'bold')
        """
        if not styles:
            return text

        # Sesbírání všech stylů
        ansi_codes = []
        for style in styles:
            if isinstance(style, str):
                if style in self._config_dict:
                    ansi_codes.append(self._config_dict[style])
            else:
                # Pokud je to atribut třídy (např. style.red)
                code = str(style).split('[')[-1].rstrip('m')
                ansi_codes.append(code)

        # Aplikace stylů na text
        return f"{self.ESCAPE}{';'.join(ansi_codes)}m{text}{self.reset}"

    def color(self, level: str) -> str:
        """
        Get color for log level.

        Args:
            level: Log level name

        Returns:
            Color name or ANSI sequence for the level
        """
        LEVELS_COLORS = {
            'ERROR': "31",  # red
            'WARNING': "33",  # yellow
            'INFO': "32",  # green
            'DEBUG': "36",  # cyan
            'CRITICAL': '36;43',  # red with yellow background
        }
        level = level.upper()
        color = self._level_colors.get(level, 'default')

        # Pro CRITICAL přidáme bold
        if level == 'CRITICAL':
            return self.set(color, 'bold')

        return self._config_dict[color]


# Vytvoření singleton instance
style = ANSIFormatter()

# Expose color function directly
color = style.color