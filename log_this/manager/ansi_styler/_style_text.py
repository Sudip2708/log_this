print("_style_text.py.py")
from typing import List, TYPE_CHECKING
from .mixins import SetMixin, ProcesAnsiCodesMixin
from .utils import process_text

if TYPE_CHECKING:
    from .ansi_formatter import ANSIFormatter

class StyledText(SetMixin, ProcesAnsiCodesMixin):
    """Helper class for applying styles to specific text."""

    def __init__(self, builder: 'ANSIFormatter', text: str):
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

        # Kontrola zda atribut pro styli není prázdný
        if not self._styles:
            # Pokud ano, bude navrácen pouze text
            return self._text

        # Vytvoření seznamu s ansi kody
        ansi_code_list = self.proces_ansi_codes()

        # Volání funkce pro spracování textu a navrácení výsledného řetězce
        return process_text(self._text, ansi_code_list)




