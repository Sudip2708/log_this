from typing import Union, Optional, List, Dict, Tuple, Any
import re
from log_this.manager.config.ansi._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS


class ANSIFormatter:
    """Base class for ANSI formatting functionality."""

    _instance: Optional['StyleBuilder'] = None

    ESCAPE = "\033["
    RESET = "\033[0m"
    PATTERN = re.compile(r"\033\[[0-9;]*m|[^\033]+")
    LEVELS_COLORS: Dict[str, str] = {
        'ERROR': "31",  # red
        'WARNING': "33",  # yellow
        'INFO': "32",  # green
        'DEBUG': "36",  # cyan
        'CRITICAL': '36;43'  # red with yellow background
    }

    def __new__(cls) -> 'ANSIFormatter':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the formatter with ANSI codes and styles."""
        self.config_dict = {**TEXT_STYLES, **TEXT_COLORS, **BACKGROUND_COLORS}
        self.config_keys = set(self.config_dict.keys())
        self.allowed_codes = set(self.config_dict.values())


    def color(self, label_level: str) -> str:
        """Get color code for specified log level.

        Args:
            label_level: Logging level name (ERROR, WARNING, etc.)

        Returns:
            ANSI color code for the specified level
        """
        level = label_level.upper()
        return self.LEVELS_COLORS.get(level, "")

    def style(self, text: str):
        return StyledText(self, text)


class StyledText:
    """Helper class for applying styles to specific text."""

    def __init__(self, builder: ANSIFormatter, text: str = None):
        """Initialize StyledText with builder and text.

        Args:
            builder: StyleBuilder instance to use for style application
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
        else:
            return self.process_text()

    def _set(self, *codes: str) -> 'StyledText':
        """Add multiple styles to be applied.

        Args:
            *codes: Variable number of style names or attribute names to apply

        Returns:
            Self for method chaining
        """
        for code in codes:
            if code in self._builder.allowed_codes:
                self._styles.append(code)
            else:
                raise ValueError(f"Invalid code: {code}, allowed values: {self._builder.allowed_codes}")
        return self

    @staticmethod
    def wrap_with_codes(string: str, codes: Any = None) -> str:
        """
        Wraps text with ANSI escape sequences using the specified formatting codes.

        Args:
            string: The text to be wrapped with ANSI codes.
            codes: Single code or multiple codes to apply. Can be int, str, tuple, list, or set.
                If None or empty, returns the original text.

        Returns:
            str: Text wrapped with ANSI escape sequences.

        Raises:
            TypeError: If codes are not of the correct type or not convertible to str.
            ValueError: If any of the codes is not valid.
        """
        if codes is None or not codes:
            return string

        if isinstance(codes, (int, str)):
            return f"\033[{codes}m{string}\033[0m"

        if isinstance(codes, (list, set)):
            codes = tuple(set(codes))

        if len(codes) == 1:
            code = codes[0]
            if not isinstance(code, (int, str)):
                raise TypeError("Code must be int or str")
            return f"\033[{code}m{string}\033[0m"

        try:
            codes_str = ";".join(str(code) for code in codes)
        except TypeError:
            raise TypeError("All codes must be convertible to str")

        return f"\033[{codes_str}m{string}\033[0m"


    def process_text(self, string: str, new_codes: str) -> str:
        """
        Processes text containing ANSI sequences and adds new formatting codes to unformatted parts.

        This function preserves existing ANSI formatting while adding new formatting codes
        to unformatted text segments. It handles nested and multiple ANSI codes properly.

        Args:
            string: Input text that may contain ANSI escape sequences.
            new_codes: New formatting codes to apply to unformatted text segments.
                Can be a single code or multiple codes.

        Returns:
            str: Processed text with both existing and new ANSI formatting applied.

        """
        pattern = self._builder.PATTERN
        current_codes: set[str] = set()
        result: list[str] = []

        for match in pattern.finditer(string):
            part = match.group(0)

            if part.startswith("\033"):
                codes = part[2:-1].split(";")

                if "0" in codes:
                    current_codes.clear()
                else:
                    current_codes.update(codes)
            else:
                formatted_part = (
                    self.wrap_with_codes(part, current_codes)
                    if current_codes
                    else self.wrap_with_codes(part, new_codes)
                )
                result.append(formatted_part)

        return "".join(result)

inst = ANSIFormatter()
style = inst.style
set =

#
# # Basic styling examples
# print("\nBasic styling:")
# print(style("Bold text").set("bold"))
# print(style("Red text").set("red"))
# print(style("Bold red text").set("bold", "red"))
# print(style("Blue text on yellow background").set("blue", "bg_yellow"))
#
# # Using predefined log level colors
# print("\nLog level styling:")
# print(style("ERROR").set(color("ERROR"), "bold"))
# print(style("WARNING").set(color("WARNING")))
# print(style("INFO").set(color("INFO")))
# print(style("DEBUG").set(color("DEBUG")))
# print(style("CRITICAL").set(color("CRITICAL")))
#
# # Text concatenation examples
# print("\nConcatenation examples:")
# print(style("Red").set("red") + " and " + style("Blue").set("blue"))
# print(style("Rainbow: ").set("bold") +
#       style("R").set("red") +
#       style("G").set("green") +
#       style("B").set("blue"))
#
# # Nested styles
# print("\nNested styles:")
# nested_text = (
#         style("This is ").set("bold") +
#         style("nested").set("red", "italic") +
#         " styling"
# )
# print(style(nested_text).set("underline"))
#
# # Complex formatting example
# print("\nComplex formatting:")
# status = style("[ERROR]").set("red", "bold")
# message = style("Failed to connect").set("red")
# details = style("(timeout after 30s)").set("dim")
# print(f"{status} {message} {details}")
#
# # Multiple styles in one line
# print("\nMultiple styles:")
# print(
#     style("CRITICAL: ").set("bg_red", "white", "bold") +
#     style("System shutdown").set("red", "bold") +
#     style(" (Action required)").set("blink", "yellow")
# )
#
# # Table-like output
# print("\nFormatted table-like output:")
# header = style("Status  | Message         | Time").set("bold", "underline")
# row1 = (style("OK     ").set("green") + " | " +
#         style("User logged in").set("default") + " | " +
#         style("10:00").set("dim"))
# row2 = (style("ERROR  ").set("red") + " | " +
#         style("Failed backup").set("default") + " | " +
#         style("10:15").set("dim"))
# print(header)
# print(row1)
# print(row2)
#
# # Different text styles combination
# print("\nText style combinations:")
# print(style("Bold + Italic").set("bold", "italic"))
# print(style("Underline + Dim").set("underline", "dim"))
# print(style("Strike + Red background").set("strike", "bg_red"))
# print(style("Framed blue text").set("framed", "blue"))
#
# # Progressive text building
# print("\nProgressive text building:")
# text = style("Start")
# text = text.set("bold")
# text = text + style(" Middle").set("red", "italic")
# text = text + style(" End").set("blue", "underline")
# print(text)