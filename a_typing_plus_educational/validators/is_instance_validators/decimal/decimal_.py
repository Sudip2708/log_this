from decimal import Decimal

from ...._bases import BaseIsInstanceValidator


class DecimalValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci Decimal

    Decimal v Pythonu je typ pro reprezentaci desetinných čísel s přesnou aritmetikou.
    Tento typ je užitečný pro finanční a jiné výpočty, kde je nezbytná vysoká přesnost
    a kde zaokrouhlování způsobené standardními plovoucími čísly může vést k chybám.

    Syntaxe:
        - Decimal('123.45')  # Příklad vytvoření Decimal z řetězce
        - Decimal(123.45)    # Příklad vytvoření Decimal z float
        - Decimal('0.1') + Decimal('0.2')  # Příklad sčítání Decimal hodnot

    Příklady použití:
        - Decimal('10.05')      # Příklad vytvoření hodnoty Decimal
        - d = Decimal('100.2')  # Příklad přiřazení hodnoty do proměnné
        - result = d * Decimal('2')  # Použití při výpočtu

    Validační proces:
        1. Ověřuje, zda hodnota je přesně instance typu `decimal.Decimal`
        2. Zajišťuje, že hodnota je validní reprezentací desetinného čísla

    Použití v kódu:
        - Pro parametry funkcí: def calculate_interest(rate: Decimal) -> Decimal
        - Pro finanční výpočty: total = amount * interest_rate
        - Pro typování proměnných: price: Decimal = Decimal('19.99')

    Specifické použití:
        - Pro přesné finanční výpočty, kde je nutná kontrola na zaokrouhlování
        - Pro výpočty s hodnotami, kde je důležitá přesnost (například ve vědeckých výpočtech)
        - Využití při převodech mezi různými měnovými hodnotami, kde je potřeba zachovat přesnost

    Kompatibilita:
        - `Decimal` je kompatibilní s operacemi, které vyžadují přesnost aritmetiky (např. sčítání, násobení)
        - `Decimal` není kompatibilní s nečíslicovými typy, jako jsou `str`, `bool`, apod.
        - `Decimal` podporuje aritmetické operace s jinými hodnotami typu `Decimal`, ale je potřeba zajistit kompatibilitu s jinými číselnými typy.

    Běžné chyby:
        - Zaměňování typu `Decimal` s běžnými plovoucími body (float), které mohou vést k zaokrouhlovacím chybám
        - Použití `Decimal` při aritmetických operacích s plovoucími čísly, což může vést k nesprávným výsledkům
        - Použití nevalidních hodnot pro inicializaci objektu `Decimal`, jako jsou nesprávně formátované řetězce

    Reference:
        - https://docs.python.org/3/library/decimal.html
        - https://realpython.com/python-decimal/
    """

    VALIDATOR_KEY = "decimal"
    ANNOTATION = Decimal

    IS_INSTANCE = Decimal
    DUCK_TYPING = {
        "has_attr": (
            "__add__", "__sub__", "__mul__", "__truediv__", "__neg__",
            "__pos__", "__abs__", "adjusted", "as_tuple"
        ),
        "has_callable_attr": ("adjusted", "as_tuple")
    }

    DESCRIPTION = "Desetinné číslo s přesnou aritmetikou"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí decimal.Decimal, "
            "tedy číslo s plovoucí desetinnou čárkou s přesnou aritmetikou. "
            "Vhodné pro finanční výpočty, kde je třeba eliminovat chyby zaokrouhlení."
        )
