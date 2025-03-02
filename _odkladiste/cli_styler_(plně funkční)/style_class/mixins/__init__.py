from ._style_get import StyleGetMixin
from ._style_print import StylePrintMixin

__all__ = [

    "StyleGetMixin",
    # Mixin obsahující metodu pro navrácení ostylovaného textu
    # Přidává metodyu: style_get(text)
    # Používá atributy: symbol, color, style, end_line

    "StylePrintMixin"
    # Mixin obsahující metodu pro vytisknutí ostylovaného textu
    # Přidává metodu: style_print(text)
    # Používá metody: style_get(text)

]