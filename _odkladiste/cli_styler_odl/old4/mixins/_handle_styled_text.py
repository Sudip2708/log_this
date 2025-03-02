from abc import ABC

from abc_helper import abc_method, abc_property
from ..utils import validate_style_and_text


class HandleStyledTextMixin(ABC):

    # Metoda pro naformátování stylu a textu
    _format_text = abc_method("_format_text")

    # Metoda pro vytisknutí naformátovaného obsahu
    _print_styled = abc_method("_print_styled")


    def _handle_styled_text(self,
            style: str,
            text: str
    ):
        """Zpracuje případ, kdy jsou předány dva argumenty: styl a text"""

        # Validace zda styl i text jsou str
        validate_style_and_text(style, text)

        # Vytištění ostylovaného textu
        self._print_styled([
            self._format_text(style, text)
        ])