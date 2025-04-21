from .._base_type_validator import BaseTypeValidator


class FloatValidator(BaseTypeValidator):
    """
    Validátor pro typovou anotaci float

    Float reprezentuje číslo s plovoucí desetinnou čárkou v Pythonu. Používá se
    pro reprezentaci reálných čísel s omezenou přesností a umožňuje práci
    s desetinnými hodnotami, vědeckou notací a speciálními hodnotami jako inf a NaN.

    Syntaxe:
        - float    # Přímý zápis typu

    Příklady použití:
        - float    # Číslo s plovoucí desetinnou čárkou

    Validační proces:
        1. Ověřuje, zda hodnota je instance typu float
        2. Kontroluje, že hodnota je přímo objekt typu float, nikoliv hodnoty,
           které lze na float převést (int, str s číslem)

    Použití v kódu:
        - Pro parametry funkcí: def calculate_area(radius: float) -> float
        - Pro návratové hodnoty: def get_average() -> float
        - Pro typování proměnných: temperature: float = 36.6

    Speciální hodnoty:
        - float('inf'), float('-inf'): Reprezentace nekonečna
        - float('nan'): Reprezentace "Not a Number" (NaN)
        - -0.0: Záporná nula (odlišná od 0.0 v některých operacích)

    Přesnost a omezení:
        - Reprezentuje čísla s dvojitou přesností (obvykle IEEE 754)
        - Může způsobovat chyby při zaokrouhlování (např. 0.1 + 0.2 != 0.3)
        - Má omezený rozsah a přesnost (přibližně 15-17 platných číslic)

    Kompatibilita:
        - int hodnoty lze převést na float, ale float není int (pro účely validace)
        - complex má float jako součást reálné a imaginární komponenty

    Běžné chyby:
        - Spoléhání na přesnost při finančních výpočtech (místo Decimal)
        - Přímé porovnávání float hodnot pomocí == (místo math.isclose)
        - Použití str hodnot obsahujících čísla, které nejsou float instance
        - Zaměňování int a float typů v místech, kde je vyžadován konkrétní typ

    Reference:
        - https://docs.python.org/3/library/functions.html#float
        - https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
        - https://docs.python.org/3/tutorial/floatingpoint.html
    """

    VALIDATOR_KEY = "float"
    ANNOTATION = float
    INFO = "Definuje, že hodnota může být pouze číslo s plovoucí desetinnou čárkou"
    ORIGIN = float