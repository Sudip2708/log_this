# Doplňujíci metody pro plus verzi
# rgb() a hex() se přidávají přec colors() přímím zadáním

# přidat možnost transparent, která by přejímala barvu nadřazeného rodiče.

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
        raise ValueError(
            "Hex color must be in format '#RRGGBB' or 'RRGGBB'")

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

def spaces(self, spaces: int) -> str:
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

