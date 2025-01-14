print("_set_mixin.py")
from typing import Union
from ..utils import get_available_styles

class SetMixin:
    """Mixin s hlavní metodou pro nastavení stylu."""

    def set(
            self,
            *styles: Union[str, int],
            values_checked: bool = False
    ) -> 'StyledText':
        """Add multiple styles to be applied.

        Args:
            *styles: Variable number of style identifiers to apply.
                    Can be style names (e.g., 'bold', 'red'),
                    ANSI codes as strings (e.g., '31', '1'),
                    or ANSI codes as integers (e.g., 31, 1)
            values_checked: If True, styles are assumed to be valid and do not need verification.


        Returns:
            Self for method chaining

        Raises:
            ValueError: If any style identifier is invalid
            TypeError: If any style is not str or int
        """

        # Cyklus procházející dodané ansi kody pro stylizování textu
        for style in styles:

            # Kontrola, zda jsou kody dodané jako str nebo int
            if not isinstance(style, (str, int)):
                raise TypeError(
                    f"Style must be string or integer, not {type(style).__name__}")

            # Převod na str, pokud by hodnota byla dodaná jako int
            style_str = str(style)

            # Kontrola zda se styl nachází v seznamu podporovaných stylů
            if style_str not in self._builder.allowed_codes:
                raise ValueError(
                    f"Invalid style: '{style}'. Available styles are: "
                    f"{get_available_styles()}"
                )

            # Pokud je hodnota 0 (reset), vymaž všechny styly
            if style_str == "0":  # Reset styles
                self._styles = []

            # Pokud jde o jinou hodnotu, přidej ji do seznam stylů
            else:
                self._styles.append(style_str)

        # Navrácení textové reprezentace instance
        # Jedná se o plně spracovaný řetězec obsahující staré i nové styli
        return self


    def s(self, *styles: Union[str, int]) -> 'StyledText':
        """Alias for set method."""
        return self.set(*styles)