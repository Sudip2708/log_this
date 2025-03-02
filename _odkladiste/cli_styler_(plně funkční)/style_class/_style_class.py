# cli_styler/_style_class.py
from .mixins import StyleGetMixin, StylePrintMixin


class StyleClass(

    StyleGetMixin,
    # Mixin obsahující metodu pro navrácení ostylovaného textu
    # Přidává metodyu: style_get(text)
    # Používá atributy: symbol, color, style, end_line

    StylePrintMixin
    # Mixin obsahující metodu pro vytisknutí ostylovaného textu
    # Přidává metodu: style_print(text)
    # Používá metody: style_get(text)

):
    """
    Základní třída pro instance stylů.

    Styly přebírá z konfiguračního slovníku a přidává metody
    pro navrácení ostylovaného textu jako tuple (styl, text),
    a pro vytisknutí ostylovaného textu do konzole.
    """

    # Atributy použité v mixinech
    symbol = None
    color = None
    style = None
    end_line = None


    def __init__(self, style_dict: dict, ids: tuple):
        """
        Inicializační metoda pro instance stylů.

        Metoda očekává slovník s definicemi pro jednotlivé styly
        a tuple s defincí sady značek a barevného režimu.

        Metoda nejprve načte id pro sadu značek a barevného režimu.
        (Jedná se o interně generované parametry, kde se předpokládá správný formát.)

        Dále metoda vytvoří na základě obdrženého slovníku atributy pro daný styl.
        (Pokud jsou nastaveny barvy, nebo značky na "native",
        tedy na zobrazení bez značekn nebo bez barev,
        namísto značky, nebo barvy bude přidán prázdný řetězec.)

        Pokud by u některého slovníku definující jednotlivé styly
        chyběl některá z klíčů, dojde k vyvolání výjimky.
        """

        # Načtení id pro definici sady značek a barevného modu
        symbol_id, color_id = ids

        # Inicializace atributů
        try:

            # Přiřazení definované značky, nebo prázdného řetězce
            self.symbol = style_dict["symbol"][symbol_id] \
                if symbol_id is not None else ""

            # Přiřazení definice barvy, nebo prázdného řetězce
            self.color = style_dict["color"][color_id] \
                if color_id  is not None else ""

            # Přiřazení dodatečného formátování textu
            self.style = style_dict["style"]

            # Přiřazení znaku pro nový řádek
            self.end_line = style_dict["end_line"]


        # Pokud by některý klíč nebyl nalezen
        except KeyError as e:
            raise KeyError(
                f"Načtený styl {style_dict} "
                f"nemá správně definované všechny potřebné klíče. \n"
                f"Pro pokračování je potřeba opravit definici tohoto stylu."
            )


