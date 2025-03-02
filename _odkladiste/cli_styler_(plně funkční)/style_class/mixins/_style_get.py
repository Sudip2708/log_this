from abc import ABC

from abc_helper import abc_property


class StyleGetMixin(ABC):
    """
    Mixin přidávající metodu třídě StyleClass.

    Jedná se o metodu pro vytvoření naformátovaného tuple obsahující setyl a text.
    Mixin používá atributy definované při inicializaci třídy StyleClass.
    """

    # Interní atributy definované na hlavní třídě
    color = abc_property("color")
    style = abc_property("style")
    symbol = abc_property("symbol")
    end_line = abc_property("end_line")


    def style_get(self, text: str = None) -> tuple:
        """
        Metoda vrátí naformátovaný tuple (symbol, ostylovaný text).

        Metoda nejprve vytvoří styl sečtením řetězců definujících barvu a formát.
        Následně metoda přidá k textu značku a způsob ukončení řádku.
        Metoda vrací tuple z těchto vytvořených hodnot.

        # Vytvořené tuple se dá použít:
         - Jako definice textu a stylu pro dialogová okna
         - Jako podklad pro FormattedText a následné vytisknutí do konzole
        """

        # Definice stylu (sečte řetězce pro barvu a dodatečný styl)
        style = self.color + self.style

        # Definice stylu (sečte řetězce pro symbol, text a ukončení řádku)
        text = self.symbol + text + self.end_line

        # Navrácení tuple obsahující styl a doplněný text
        return style, text
