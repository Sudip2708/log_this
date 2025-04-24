from typing import SupportsInt

from ...._bases import IsInstanceValidatorBase


class SupportsIntValidator(IsInstanceValidatorBase):
    """
    Validátor pro typovou anotaci SupportsInt

    SupportsInt reprezentuje protokol pro objekty, které lze konvertovat na celé
    číslo implementací metody __int__. Zahrnuje všechny typy, které lze explicitně převést
    na int pomocí funkce int().

    Syntaxe:
        - SupportsInt          # Jediný zápis (vyžaduje import z typing)

    Příklady použití:
        - SupportsInt          # Jakýkoliv objekt, který lze převést na int

    Validační proces:
        1. Ověří, zda objekt je instance SupportsInt (implementuje metodu '__int__')
        2. Neprovádí kontrolu skutečné funkčnosti metody

    Použití v kódu:
        - Pro parametry funkcí: def calculate_factorial(value: SupportsInt) -> int
        - Pro návratové hodnoty: def get_item_count() -> SupportsInt
        - Pro typování proměnných: count: SupportsInt = CustomInteger(42)

    Protokolové požadavky:
        Pro správnou implementaci SupportsInt objekt musí:
        - Implementovat metodu '__int__', která vrací hodnotu typu int

    Příklad implementace:
        ```python
        class Quantity(SupportsInt):
            def __init__(self, amount: float, unit: str = "pcs"):
                self.amount = amount
                self.unit = unit

            def __int__(self) -> int:
                return int(self.amount)

            def __str__(self) -> str:
                return f"{self.amount} {self.unit}"
        ```

    Běžné použití:
        ```python
        def allocate_buffer(size: SupportsInt) -> bytearray:
            return bytearray(int(size))

        # Použití s vlastní třídou
        buffer = allocate_buffer(Quantity(1024, "bytes"))

        # Použití s nativními typy
        buffer = allocate_buffer(1024)
        buffer = allocate_buffer(1024.5)  # bude zaokrouhleno na 1024
        buffer = allocate_buffer(Decimal("1024"))
        ```

    Kompatibilní typy:
        - int: nativní celé číslo
        - float: desetinné číslo (implicitně implementuje __int__, provádí oříznutí)
        - Decimal: přesné desetinné číslo
        - Fraction: zlomek
        - bool: pravdivostní hodnota (True jako 1, False jako 0)
        - Jakýkoli vlastní objekt implementující __int__

    Srovnání s podobnými protokoly:
        - SupportsFloat: podobný protokol pro převod na desetinné číslo
        - SupportsComplex: podobný protokol pro převod na komplexní číslo
        - SupportsIndex: protokol pro převod na index (implementuje __index__)
        - SupportsBytes: podobný protokol pro převod na bajty

    Praktické využití:
        - Počítání nebo indexování s vlastními typy
        - Alokace prostředků na základě velikosti
        - ID a referenční hodnoty
        - Paginace a stránkování
        - Funkce, které akceptují různé typy reprezentující celá čísla

    Běžné chyby:
        - Nevrácení validní int hodnoty z metody __int__
        - Zaměňování s typem int (SupportsInt je protokol, ne konkrétní typ)
        - Neošetření zaokrouhlení nebo oříznutí desetinných hodnot
        - Chybějící ošetření výjimek při převodu nestandardních hodnot
        - Spoléhání se na implicitní konverzi místo explicitní (vždy použít int(obj))

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.SupportsInt
        - https://docs.python.org/3/reference/datamodel.html#object.__int__
        - https://peps.python.org/pep-0544/ (protokoly a strukturální podtypy)
    """

    VALIDATOR_KEY = "supportsint"
    ANNOTATION = SupportsInt
    INFO = "Definuje, že objekt musí podporovat metodu __int__"
    ORIGIN = SupportsInt