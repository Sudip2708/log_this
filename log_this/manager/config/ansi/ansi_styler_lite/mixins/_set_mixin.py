from typing import Union
from ..utils import get_available_styles

class SetMixin:
    """Mixin s hlavní metodou pro nastavení stylu."""

    def s(self, *styles: Union[str, int]) -> 'StyledText':
        """Alias for set method."""
        return self.set(*styles)

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

        # Cyklus procházející dodané ansi kody pro stylizování textu
        for style in styles:

            # Kontrola, zda jsou kody dodané jako str nebo int
            if isinstance(style, (str, int)):
                # Převod na str
                style_str = str(style)

            # Pokud se jedná o jiný formát
            else:
                # Vyvolání výjimky
                raise TypeError(
                    f"Style must be string or integer, not {type(style).__name__}")

            # Kontrola zda se styl nachází v seznamu podporovaných stylů
            if style_str in self._builder.allowed_codes:
                # pokud ano, přidání stylu do atributu pro seznam stylů
                self._styles.append(style_str)

            # Pokud se nejedná o podporovaný styl
            else:
                # Vyvolání výjimky s výpisem podporovaných stylů
                raise ValueError(
                    f"Invalid style: '{style}'. Available styles are: "
                    f"{get_available_styles()}"
                )

        # Navrácení textové reprezentace instance
        # Jedná se o plně spracovaný řetězec obsahující staré i nové styli
        return self

