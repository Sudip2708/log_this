from typing import Union, Optional, Dict
import re
from ._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS
from .style_builder import StyledBuilder


class ANSIFormatter:
    """Base class for ANSI formatting functionality."""

    _instance: Optional['ANSIFormatter'] = None  # Fixed type annotation

    ESCAPE = "\033["
    RESET = "\033[0m"
    PATTERN = re.compile(r"\033\[[0-9;]*m|[^\033]+")
    LEVELS_COLORS: Dict[str, str] = {
        'ERROR': "31",  # red
        'WARNING': "33",  # yellow
        'INFO': "32",  # green
        'DEBUG': "36",  # cyan
        'CRITICAL': '36;43'  # cyan with yellow background
    }

    def __new__(cls) -> 'ANSIFormatter':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the formatter with ANSI codes and styles."""
        self.config_dict = {**TEXT_STYLES, **TEXT_COLORS, **BACKGROUND_COLORS}
        self.config_keys = set(self.config_dict.keys())
        self.config_values = set(self.config_dict.values())
        self.allowed_codes = self.config_keys | self.config_values

    def color(self, label_level: str) -> str:
        """Get color code for specified log level.

        Args:
            label_level: Logging level name (ERROR, WARNING, etc.)

        Returns:
            ANSI color code for the specified level
        """
        level = label_level.upper()
        return self.LEVELS_COLORS.get(level, "")

    def style(self, text: str) -> 'StyledBuilder':
        """Create a new StyledText instance for the given text.

        Args:
            text: Text to be styled

        Returns:
            StyledText instance for method chaining
        """
        return StyledBuilder(self, text)

# Create singleton instance
inst = ANSIFormatter()
style = st = inst.style


# Testovací vstupy
vstup1 = "Toto je text."
vstup2 = "Toto je \033[1;31mčervený text\033[0m a další část."
vstup3 = "\033[34mModrý\033[0m text a \033[32mzelený\033[0m."

print(style(vstup1).set(31, 1))
print(style(vstup2).set("bold", "34"))
print(style(vstup3).set("4", "35"))