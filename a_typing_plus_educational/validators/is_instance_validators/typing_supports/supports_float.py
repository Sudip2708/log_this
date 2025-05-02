from typing import SupportsFloat

from ...._bases import BaseIsInstanceValidator


class SupportsFloatValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci SupportsFloat

    SupportsFloat reprezentuje protokol pro objekty, které lze konvertovat na desetinné
    číslo implementací metody __float__. Zahrnuje všechny typy, které lze explicitně převést
    na float pomocí funkce float().

    Syntaxe:
        - SupportsFloat          # Jediný zápis (vyžaduje import z typing)

    Příklady použití:
        - SupportsFloat          # Jakýkoliv objekt, který lze převést na float

    Validační proces:
        1. Ověří, zda objekt je instance SupportsFloat (implementuje metodu '__float__')
        2. Neprovádí kontrolu skutečné funkčnosti metody

    Použití v kódu:
        - Pro parametry funkcí: def calculate_square_root(value: SupportsFloat) -> float
        - Pro návratové hodnoty: def get_coefficient() -> SupportsFloat
        - Pro typování proměnných: factor: SupportsFloat = CustomNumber(1.5)

    Protokolové požadavky:
        Pro správnou implementaci SupportsFloat objekt musí:
        - Implementovat metodu '__float__', která vrací hodnotu typu float

    Příklad implementace:
        ```python
        class Price(SupportsFloat):
            def __init__(self, amount: float, currency: str = "USD"):
                self.amount = amount
                self.currency = currency

            def __float__(self) -> float:
                return float(self.amount)

            def __str__(self) -> str:
                return f"{self.amount} {self.currency}"
        ```

    Běžné použití:
        ```python
        def calculate_tax(price: SupportsFloat, rate: float = 0.21) -> float:
            return float(price) * rate

        # Použití s vlastní třídou
        tax = calculate_tax(Price(100, "EUR"))

        # Použití s nativními typy
        tax = calculate_tax(100)
        tax = calculate_tax(100.0)
        tax = calculate_tax(Decimal("100.00"))
        ```

    Kompatibilní typy:
        - float: nativní desetinné číslo
        - int: celé číslo (implicitně implementuje __float__)
        - Decimal: přesné desetinné číslo
        - Fraction: zlomek
        - Jakýkoli vlastní objekt implementující __float__

    Srovnání s podobnými protokoly:
        - SupportsInt: podobný protokol pro převod na celé číslo
        - SupportsComplex: podobný protokol pro převod na komplexní číslo
        - SupportsBytes: podobný protokol pro převod na bajty
        - SupportsAbs: protokol pro absolutní hodnotu

    Praktické využití:
        - Matematické operace vyžadující desetinná čísla
        - Finanční výpočty s vlastními typy
        - Převody jednotek
        - Práce s vlastními numerickými typy
        - Funkce, které akceptují různé typy reprezentující desetinná čísla

    Běžné chyby:
        - Nevrácení validní float hodnoty z metody __float__
        - Zaměňování s typem float (SupportsFloat je protokol, ne konkrétní typ)
        - Spoléhání na implicitní konverzi místo explicitní (vždy použít float(obj))
        - Chybějící ošetření výjimek při převodu nestandardních hodnot

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.SupportsFloat
        - https://docs.python.org/3/reference/datamodel.html#object.__float__
        - https://peps.python.org/pep-0544/ (protokoly a strukturální podtypy)
    """

    VALIDATOR_KEY = "supportsfloat"
    ANNOTATION = SupportsFloat

    IS_INSTANCE = SupportsFloat
    HAS_ATTRS = "__float__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Objekt podporující konverzi na float"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje protokol SupportsFloat, "
            "tedy implementuje metodu __float__, která umožňuje konverzi objektu "
            "na číslo s plovoucí desetinnou čárkou pomocí funkce float()."
        )
