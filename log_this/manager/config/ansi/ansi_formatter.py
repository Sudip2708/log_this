# file: ansi_formatter.py
from typing import Union, Optional
from ._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS


class ANSIFormatter:
    """Class for formatting text with ANSI escape sequences."""

    _instance: Optional['ANSIFormatter'] = None
    ESCAPE = "\033["

    def __new__(cls) -> 'ANSIFormatter':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Inicializace proběhne pouze jednou díky Singletonu
        if not hasattr(self, '_initialized'):
            self.reset = f"{self.ESCAPE}0m"
            self._config_dict = {**TEXT_STYLES, **TEXT_COLORS,
                                 **BACKGROUND_COLORS}
            self._register_attributes()
            self._initialized = True

    def _register_attributes(self):
        """Dynamically register text styles and colors as attributes."""
        for name, code in self._config_dict.items():
            setattr(self, name, f"{self.ESCAPE}{code}m")

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



    def rgb(self, r: int, g: int, b: int, background: bool = False) -> str:
        """
        Generate an RGB color escape code.
    
        Args:
            r: Red component (0-255)
            g: Green component (0-255)
            b: Blue component (0-255)
            background: If True, sets background color instead of text color
    
        Returns:
            ANSI escape sequence for the specified RGB color
        """
        for value in (r, g, b):
            if not isinstance(value, int) or not (0 <= value <= 255):
                raise ValueError(
                    f"RGB values must be integers in range 0-255, got {value}")
    
        color_type = 48 if background else 38
        return f"{self.ESCAPE}{color_type};2;{r};{g};{b}m"
    
    
    def hex(self, hex_color: str, background: bool = False) -> str:
        """
        Generate a color escape code from hex string.
    
        Args:
            hex_color: Color in hex format (e.g., '#FF0000' or 'FF0000')
            background: If True, sets background color instead of text color
    
        Returns:
            ANSI escape sequence for the specified color
        """
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            raise ValueError("Hex color must be in format '#RRGGBB' or 'RRGGBB'")
    
        try:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
        except ValueError:
            raise ValueError(f"Invalid hex color format: {hex_color}")
    
        return self.rgb(r, g, b, background)

    def indent(self, text: str, level: int = 1,
               indent_char: str = "  ") -> str:
        """
        Odsadí text se zachováním ANSI sekvencí.

        Args:
            text: Text k odsazení
            level: Počet úrovní odsazení
            indent_char: Znak nebo řetězec použitý pro odsazení
        """
        prefix = indent_char * level
        lines = text.split('\n')
        return '\n'.join(f"{prefix}{line}" for line in lines)

    def __call__(self, spaces: int) -> str:
        """
        Umožňuje použít instanci jako funkci pro odsazení v f-stringu.

        Usage:
            f"{style(4)}Text"  # odsadí text o 4 mezery
        """
        return " " * spaces

    def colorize(self, text: str, levelname: str) -> str:
        """
        Obarví text podle úrovně logu.

        Args:
            text: Text k obarvení
            levelname: Úroveň logu ('ERROR', 'WARNING', 'INFO', 'DEBUG')
        """
        colors = {
            'ERROR': self.red,
            'WARNING': self.yellow,
            'INFO': self.green,
            'DEBUG': self.cyan
        }
        color = colors.get(levelname.upper(), self.reset)
        return f"{color}{text}{self.reset}"

    def colorize_level(self, levelname: str) -> str:
        """
        Obarví a naformátuje název úrovně logu.

        Args:
            levelname: Úroveň logu ('ERROR', 'WARNING', 'INFO', 'DEBUG')
        """
        # Pro levelname použijeme bold
        return self.colorize(f"{self.bold}{levelname}{self.reset}",
                             levelname)

    def colorize_message(self, message: str, levelname: str) -> str:
        """
        Obarví zprávu logu podle úrovně.

        Args:
            message: Zpráva k obarvení
            levelname: Úroveň logu
        """
        return self.colorize(message, levelname)

    def format_log(self, levelname: str, message: str) -> str:
        """
        Naformátuje celý log včetně úrovně a zprávy.

        Args:
            levelname: Úroveň logu
            message: Zpráva logu
        """
        return f"{self.colorize_level(levelname)} - {self.colorize_message(message, levelname)}"

# Singleton instance
style = ANSIFormatter()

# Aliasy pro samostatný import
sset = style.set
sreset = style.reset

# Aliasy pro jednoduché použití
colorize = style.colorize
colorize_level = style.colorize_level
colorize_message = style.colorize_message
format_log = style.format_log