from typing import Union, Optional, List, Dict, Tuple
import re
from _odkladiste._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS


class ANSIFormatter:
    """Base class for ANSI formatting functionality."""

    ESCAPE = "\033["
    LEVELS_COLORS: Dict[str, str] = {
        'ERROR': "31",  # red
        'WARNING': "33",  # yellow
        'INFO': "32",  # green
        'DEBUG': "36",  # cyan
        'CRITICAL': '36;43'  # red with yellow background
    }

    def __init__(self):
        """Initialize the formatter with ANSI codes and styles."""
        self.reset = f"{self.ESCAPE}0m"
        self._config_dict = {**TEXT_STYLES, **TEXT_COLORS, **BACKGROUND_COLORS}
        self._register_attributes()
        # Compile regex pattern for ANSI sequence detection
        self._ansi_pattern = re.compile(r'\033\[([0-9;]*)m')

    def _register_attributes(self) -> None:
        """Dynamically register text styles and colors as attributes."""
        for name, code in self._config_dict.items():
            setattr(self, name, f"{self.ESCAPE}{code}m")

    def color(self, label_level: str) -> str:
        """Get color code for specified log level.

        Args:
            label_level: Logging level name (ERROR, WARNING, etc.)

        Returns:
            ANSI color code for the specified level
        """
        level = label_level.upper()
        return self.LEVELS_COLORS.get(level, "")

    def _split_with_ansi(self, text: str) -> List[Tuple[str, Optional[str]]]:
        """Split text into segments with their associated ANSI codes.

        Args:
            text: Text containing ANSI sequences

        Returns:
            List of tuples (text_segment, ansi_code)
        """
        segments = []
        last_end = 0
        current_style = None

        for match in self._ansi_pattern.finditer(text):
            # Text before the ANSI sequence
            if match.start() > last_end:
                segments.append((text[last_end:match.start()], current_style))

            # Update current style
            if match.group(1) == '0':
                current_style = None
            else:
                current_style = match.group(1)

            last_end = match.end()

        # Add remaining text
        if last_end < len(text):
            segments.append((text[last_end:], current_style))

        return [seg for seg in segments if seg[0]]  # Filter out empty segments


class StyleBuilder(ANSIFormatter):
    """Class for building and applying ANSI styles with support for method chaining."""

    _instance: Optional['StyleBuilder'] = None

    def __new__(cls) -> 'StyleBuilder':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize StyleBuilder as singleton with base formatter functionality."""
        if not hasattr(self, '_initialized'):
            super().__init__()
            self._initialized = True

    def __call__(self, text: str) -> 'StyledText':
        """Create a StyledText instance for the given text.

        Args:
            text: Text to be styled

        Returns:
            StyledText instance for method chaining
        """
        return StyledText(self, text)


class StyledText:
    """Helper class for applying styles to specific text."""

    def __init__(self, builder: StyleBuilder, text: str):
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

        # Convert style names to ANSI codes
        ansi_codes = []
        for style in self._styles:
            if isinstance(style, str):
                if style in self._builder._config_dict:
                    ansi_codes.append(self._builder._config_dict[style])
                elif hasattr(self._builder, style):
                    code = str(getattr(self._builder, style)).split('[')[
                        -1].rstrip('m')
                    ansi_codes.append(code)

        combined_style = ';'.join(ansi_codes)

        # If no existing ANSI sequences, apply styles to whole text
        if self._builder.ESCAPE not in self._text:
            return f"{self._builder.ESCAPE}{combined_style}m{self._text}{self._builder.reset}"

        # Handle nested styles
        result = []
        segments = self._builder._split_with_ansi(self._text)

        for segment_text, segment_style in segments:
            if segment_style is None:
                # No existing style, apply new styles
                result.append(
                    f"{self._builder.ESCAPE}{combined_style}m{segment_text}")
            else:
                # Preserve existing style
                result.append(
                    f"{self._builder.ESCAPE}{segment_style}m{segment_text}")

        return ''.join(result) + self._builder.reset

    def __add__(self, other: Union[str, 'StyledText']) -> 'StyledText':
        """Concatenate with another text or StyledText.

        Args:
            other: String or StyledText to concatenate with

        Returns:
            New StyledText instance with concatenated content
        """
        other_text = str(other)
        return StyledText(self._builder, str(self) + other_text)

    def set(self, *items: str) -> 'StyledText':
        """Add multiple styles to be applied.

        Args:
            *items: Variable number of style names or attribute names to apply

        Returns:
            Self for method chaining
        """
        self._styles.extend(items)
        return self


# Create singleton instance
style = StyleBuilder()
color = style.color

# if __name__ == "__main__":
# Basic styling examples
print("\nBasic styling:")
print(style("Bold text").set("bold"))
print(style("Red text").set("red"))
print(style("Bold red text").set("bold", "red"))
print(style("Blue text on yellow background").set("blue", "bg_yellow"))

# Using predefined log level colors
print("\nLog level styling:")
print(style("ERROR").set(color("ERROR"), "bold"))
print(style("WARNING").set(color("WARNING")))
print(style("INFO").set(color("INFO")))
print(style("DEBUG").set(color("DEBUG")))
print(style("CRITICAL").set(color("CRITICAL")))

# Text concatenation examples
print("\nConcatenation examples:")
print(style("Red").set("red") + " and " + style("Blue").set("blue"))
print(style("Rainbow: ").set("bold") +
      style("R").set("red") +
      style("G").set("green") +
      style("B").set("blue"))

# Nested styles
print("\nNested styles:")
nested_text = (
        style("This is ").set("bold") +
        style("nested").set("red", "italic") +
        " styling"
)
print(style(nested_text).set("underline"))

# Complex formatting example
print("\nComplex formatting:")
status = style("[ERROR]").set("red", "bold")
message = style("Failed to connect").set("red")
details = style("(timeout after 30s)").set("dim")
print(f"{status} {message} {details}")

# Multiple styles in one line
print("\nMultiple styles:")
print(
    style("CRITICAL: ").set("bg_red", "white", "bold") +
    style("System shutdown").set("red", "bold") +
    style(" (Action required)").set("blink", "yellow")
)

# Table-like output
print("\nFormatted table-like output:")
header = style("Status  | Message         | Time").set("bold", "underline")
row1 = (style("OK     ").set("green") + " | " +
        style("User logged in").set("default") + " | " +
        style("10:00").set("dim"))
row2 = (style("ERROR  ").set("red") + " | " +
        style("Failed backup").set("default") + " | " +
        style("10:15").set("dim"))
print(header)
print(row1)
print(row2)

# Different text styles combination
print("\nText style combinations:")
print(style("Bold + Italic").set("bold", "italic"))
print(style("Underline + Dim").set("underline", "dim"))
print(style("Strike + Red background").set("strike", "bg_red"))
print(style("Framed blue text").set("framed", "blue"))

# Progressive text building
print("\nProgressive text building:")
text = style("Start")
text = text.set("bold")
text = text + style(" Middle").set("red", "italic")
text = text + style(" End").set("blue", "underline")
print(text)