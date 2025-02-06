print("_style_text.py.py")
from typing import List, TYPE_CHECKING
import re
from .mixins import SetMixin, ProcesAnsiCodesMixin
from .utils import process_text, split_text_with_ansi

if TYPE_CHECKING:
    from .ansi_formatter import ANSIFormatter

class StyledText(SetMixin, ProcesAnsiCodesMixin):
    """Helper class for applying styles to specific text."""

    # Natsavení vzoru pro vyhledávání ansi sekvencí a textu
    pattern = re.compile(r"\033\[[0-9;]*m|[^\033]+")

    def __init__(self, builder: 'ANSIFormatter', text: str):
        """Initialize StyledText with builder and text.

        Args:
            builder: ANSIFormatter instance to use for style application
            text: Text string to be styled
        """
        self._builder = builder
        self._text = text
        self._styles: list[str] = []
        self._values_checked = False
        self.wrap_width: int = 0  # Default to no wrapping

    def __str__(self) -> str:
        """Convert styled text to string.

        Returns:
            Formatted text with applied ANSI styles
        """

        # Kontrola zda atribut pro styli není prázdný
        if not self._styles:
            # Pokud ano, bude navrácen pouze text
            return self._text

        # Vytvoření seznamu s ansi kody
        ansi_code_list = (
            self._styles if self._values_checked
            else self.proces_ansi_codes()
        )

        # Volání funkce pro spracování textu a navrácení výsledného řetězce
        if self.pattern.search(self._text):
            return process_text(self._text, ansi_code_list)
        else:
            return wrap_text_whit_ansi_codes(self._text, self._styles)


    def set_checked(self, *styles: list[str]) -> __str__:
        """Internally add already validated styles."""
        self._values_checked = True
        self._styles = styles
        return self



    def wrap(self, width: int) -> List['StyledText']:
        """Wrap text into multiple StyledText instances with the same styles.

        Args:
            width: Maximum line width for wrapping.

        Returns:
            List of StyledText instances for each wrapped line.
        """
        self.wrap_width = width
        wrapped_lines = split_text_with_ansi(self._text, width)

        # Create new StyledText instances for each line with the same styles
        return [StyledText(self._builder, line).set(*self._styles) for line in wrapped_lines]



