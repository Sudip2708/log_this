print("ansi_formatter.py")
from typing import Union, Optional, Dict
import re
import json
from ._style_text import StyledText
from ._ansi_codes import (
    TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS, LEVELS_COLORS, MESSAGE_COLORS
)


class ANSIFormatter:
    """Base class for ANSI formatting functionality."""

    _instance: Optional['ANSIFormatter'] = None  # Fixed type annotation

    ESCAPE = "\033["
    RESET = "\033[0m"
    PATTERN = re.compile(r"\033\[[0-9;]*m|[^\033]+")
    LEVELS_SYMBOLS = {
        'ERROR': "✘",
        'CRITICAL': "✘",
        'WARNING': "⚠",
        'INFO': "ℹ",
        'DEBUG': "🔍",
        'SUCCESS': "✔"
    }

    def __new__(cls) -> 'ANSIFormatter':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the formatter with ANSI codes and styles."""
        self.level_color_dict = LEVELS_COLORS
        self.message_color_dict = MESSAGE_COLORS
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
        return self.level_color_dict.get(level, "37")

    def style(self, text: str) -> 'StyledText':
        """Create a new StyledText instance for the given text.

        Args:
            text: Text to be styled

        Returns:
            StyledText instance for method chaining
        """
        return StyledText(self, text)

    def colored_level(self, level: str):
        """Metoda pro formátování levelu"""
        level_color = self.level_color_dict.get(level, "37")
        return f"{self.ESCAPE}{level_color}m{level}{self.RESET}"

    def colored_message(self, level: str, message: str):
        """Metoda pro formátování zprávy na základě levelu"""
        message_color = self.message_color_dict.get(level, "37")
        return self.style(message).set(message_color)

    # def cli_format(self, level: str, message: str) -> str:
    #     """Format a message with appropriate colors for level and message."""
    #     return (f"{self.colored_level(level)}: "
    #             f"{self.colored_message(level, message)}")


    def cli_format(self, level: str, message: str, extra: str = "{}") -> str:
        """
        Format a message for CLI output with consistent styling.

        Args:
            level: Message level (ERROR, SUCCESS, INFO, etc.)
            message: The message to format
            extra: Slovník s dodatečnými informacení pro vykreslení logu

        Returns:
            Formatted string ready for CLI output
        """

        # Kontrola povinných parametrů
        if not level:
            raise ValueError("Log level is required.")
        if not message:
            raise ValueError("Log message is required.")

        # Načtení slovníku extra
        try:
            extra_dict = json.loads(extra)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in 'extra': {e}")

        # Přepis levelu na velká písmena
        level = level.upper()

        # Načtení symbolu a hlavičky
        symbol = self.LEVELS_SYMBOLS.get(level, "•")

        # Vytvoření intra
        level_color = self.level_color_dict.get(level, "37")
        text = f"{symbol} {message}"
        intro = self.style(text).set_checked(level_color)


        # Format message lines with proper indentation and color
        message_color = self.message_color_dict.get(level, "0")
        formatted_lines = [
            self.style(f"  {line}").set(color(message_color))
            for line in message_lines
        ]

        # Combine all lines
        return "\n".join([str(intro), *formatted_lines, ""])


# Create singleton instance
inst = ANSIFormatter()
style = inst.style
color = inst.color
cli_format = inst.cli_format


