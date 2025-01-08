from typing import Union, Optional, List, Dict, Tuple
import re
from ._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS


class StyleBuilder:
    """Helper class for chaining style methods.

    Allows for fluent style application to text strings with support for
    multiple styles and nested ANSI sequences.
    """

    def __init__(self, formatter: 'ANSIFormatter', text: str):
        """Initialize StyleBuilder with formatter and text.

        Args:
            formatter: ANSIFormatter instance to use for style application
            text: Text string to be styled
        """
        self._formatter = formatter
        self._text = text
        self._styles: List[str] = []

    def __str__(self) -> str:
        """Convert styled text to string.

        Returns:
            Formatted text with applied ANSI styles
        """
        if self._styles:
            return self._formatter.apply_styles(self._text, self._styles)
        return self._text

    def set(self, *items: str) -> 'StyleBuilder':
        """Add multiple styles to be applied.

        Args:
            *items: Variable number of style names to apply

        Returns:
            Self for method chaining
        """
        self._styles.extend(items)
        return self


class ANSIFormatter:
    """Class for formatting text with ANSI escape sequences.

    Supports nested styles, multiple color/style combinations,
    and maintains a singleton instance.
    """

    _instance: Optional['ANSIFormatter'] = None
    ESCAPE = "\033["
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
        if not hasattr(self, '_initialized'):
            self.reset = f"{self.ESCAPE}0m"
            self._config_dict = {**TEXT_STYLES, **TEXT_COLORS,
                                 **BACKGROUND_COLORS}
            self._register_attributes()
            self._initialized = True
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

    def style(self, text: str) -> StyleBuilder:
        """Create a StyleBuilder instance for the given text.

        Args:
            text: Text to be styled

        Returns:
            StyleBuilder instance for method chaining
        """
        return StyleBuilder(self, text)

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

    def apply_styles(self, text: str, styles: List[str]) -> str:
        """Apply list of styles to text, preserving nested styles.

        Args:
            text: Text to style
            styles: List of style names to apply

        Returns:
            Styled text with ANSI sequences
        """
        if not styles:
            return text

        # Convert style names to ANSI codes
        ansi_codes = []
        for style in styles:
            if isinstance(style, str) and style in self._config_dict:
                ansi_codes.append(self._config_dict[style])
            elif hasattr(self, style):
                code = str(getattr(self, style)).split('[')[-1].rstrip('m')
                ansi_codes.append(code)

        combined_style = ';'.join(ansi_codes)

        # If no existing ANSI sequences, apply styles to whole text
        if self.ESCAPE not in text:
            return f"{self.ESCAPE}{combined_style}m{text}{self.reset}"

        # Handle nested styles
        result = []
        segments = self._split_with_ansi(text)

        for segment_text, segment_style in segments:
            if segment_style is None:
                # No existing style, apply new styles
                result.append(f"{self.ESCAPE}{combined_style}m{segment_text}")
            else:
                # Preserve existing style
                result.append(f"{self.ESCAPE}{segment_style}m{segment_text}")

        return ''.join(result) + self.reset


# Create singleton instance
inst = ANSIFormatter()
style = inst.style
color = inst.color