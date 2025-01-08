from typing import Union, Optional, List, Dict, Tuple, Any, Set
import re
from _odkladiste._ansi_codes import TEXT_STYLES, TEXT_COLORS, \
    BACKGROUND_COLORS


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

    def style(self, text: str) -> 'StyledText':
        """Create a new StyledText instance for the given text.

        Args:
            text: Text to be styled

        Returns:
            StyledText instance for method chaining
        """
        return StyledText(self, text)

    def format_available_styles(self) -> str:
        """
        Returns a formatted string containing all available styles organized by category.

        Returns:
            str: Formatted string with all available styles and their codes
        """
        output = []

        # Helper function to format a dictionary section
        def format_section(title: str, styles: dict) -> str:
            section = [f"\n{title}:"]
            for name, code in sorted(styles.items()):
                section.append(f"  {name}: {code}")
            return "\n".join(section)

        # Add each section
        output.append(format_section("Text Styles", TEXT_STYLES))
        output.append(format_section("Text Colors", TEXT_COLORS))
        output.append(format_section("Background Colors", BACKGROUND_COLORS))

        return "\n".join(output)

class StyledText:
    """Helper class for applying styles to specific text."""

    def __init__(self, builder: ANSIFormatter, text: str):
        """Initialize StyledText with builder and text.

        Args:
            builder: ANSIFormatter instance to use for style application
            text: Text string to be styled
        """
        self._builder = builder
        self._text = text
        self._styles: List[str] = []

    def __str__(self) -> str:
        """Convert styled text to string.

        Returns:
            Formatted text with applied ANSI styles
        """
        if not self._styles:
            return self._text

        # Convert style names to ANSI codes
        codes = []
        for style_name in self._styles:
            if style_name in self._builder.config_dict:
                codes.append(self._builder.config_dict[style_name])
            elif style_name in self._builder.allowed_codes:
                codes.append(style_name)

        return self.process_text(self._text, codes)

    def set(self, *styles: Union[str, int]) -> 'StyledText':
        """Add multiple styles to be applied.

        Args:
            *styles: Variable number of style identifiers to apply.
                    Can be style names (e.g., 'bold', 'red'),
                    ANSI codes as strings (e.g., '31', '1'),
                    or ANSI codes as integers (e.g., 31, 1)

        Returns:
            Self for method chaining

        Raises:
            ValueError: If any style identifier is invalid
            TypeError: If any style is not str or int
        """
        for style in styles:
            if isinstance(style, (str, int)):
                style_str = str(style)
            else:
                raise TypeError(
                    f"Style must be string or integer, not {type(style).__name__}")

            if style_str in self._builder.allowed_codes:
                self._styles.append(style_str)
            else:
                # Use the new formatted listing in error message
                raise ValueError(
                    f"Invalid style: '{style}'. Available styles are: "
                    f"{self._builder.format_available_styles()}"
                )

        return self

    @staticmethod
    def wrap_with_codes(text: str, codes: Union[
        str, List[str], Tuple[str, ...], Set[str]]) -> str:
        """Wrap text with ANSI escape sequences.

        Args:
            text: Text to be wrapped
            codes: ANSI codes to apply

        Returns:
            Text wrapped with ANSI escape sequences
        """
        if not codes:
            return text

        if isinstance(codes, (list, tuple, set)):
            codes_str = ";".join(str(code) for code in codes)
        else:
            codes_str = str(codes)

        return f"\033[{codes_str}m{text}\033[0m"

    def process_text(self, text: str, codes: List[str]) -> str:
        """Process text with ANSI sequences and apply new codes.

        Args:
            text: Input text that may contain ANSI sequences
            codes: New formatting codes to apply

        Returns:
            Processed text with all formatting applied
        """
        pattern = self._builder.PATTERN
        current_codes: Set[str] = set()
        result: List[str] = []

        for match in pattern.finditer(text):
            part = match.group(0)

            if part.startswith("\033"):
                codes_in_text = part[2:-1].split(";")
                if "0" in codes_in_text:
                    current_codes.clear()
                else:
                    current_codes.update(codes_in_text)
            else:
                formatted_part = (
                    self.wrap_with_codes(part, current_codes)
                    if current_codes
                    else self.wrap_with_codes(part, codes)
                )
                result.append(formatted_part)

        return "".join(result)


# Create singleton instance
inst = ANSIFormatter()
style = st = inst.style


# Usage example:
print(style("Bold red text").set("bold", "red"))


# Testovací vstupy
vstup1 = "Toto je text."
vstup2 = "Toto je \033[1;31mčervený text\033[0m a další část."
vstup3 = "\033[34mModrý\033[0m text a \033[32mzelený\033[0m."

print(style(vstup1).set(31, 1))
print(style(vstup2).set("bold", "34"))
print(style(vstup3).set("4", "35"))