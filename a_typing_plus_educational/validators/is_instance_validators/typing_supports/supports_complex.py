from typing import SupportsComplex

from ...._bases import BaseIsInstanceValidator


class SupportsComplexValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci SupportsComplex

    SupportsComplex reprezentuje protokol pro objekty, které lze konvertovat na
    komplexní číslo implementací metody __complex__. Zahrnuje všechny typy, které lze
    explicitně převést na komplexní číslo pomocí funkce complex().

    Syntaxe:
        - SupportsComplex       # Jediný zápis (vyžaduje import z typing)

    Příklady použití:
        - SupportsComplex       # Jakýkoliv objekt, který lze převést na komplexní číslo

    Validační proces:
        1. Ověří, zda objekt je instance SupportsComplex (implementuje metodu '__complex__')
        2. Neprovádí kontrolu skutečné funkčnosti metody

    Použití v kódu:
        - Pro parametry funkcí: def to_complex(value: SupportsComplex) -> complex
        - Pro návratové hodnoty: def get_signal_component() -> SupportsComplex
        - Pro typování proměnných: z: SupportsComplex = MyComplexLike(2, 3)

    Protokolové požadavky:
        Pro správnou implementaci SupportsComplex objekt musí:
        - Implementovat metodu '__complex__', která vrací hodnotu typu complex

    Příklad implementace:
        ```python
        class MyComplexLike(SupportsComplex):
            def __init__(self, real, imag=0):
                self.real = real
                self.imag = imag

            def __complex__(self) -> complex:
                return complex(self.real, self.imag)
        ```

    Běžné použití:
        ```python
        def analyze_signal(z: SupportsComplex):
            result = complex(z)
            print("Complex signal:", result)

        analyze_signal(3.14)
        analyze_signal(MyComplexLike(2, 5))
        ```

    Kompatibilní typy:
        - int, float: implicitně konvertovatelné na komplexní číslo
        - complex: základní typ pro komplexní čísla
        - Decimal, Fraction: konvertovatelné přes __complex__ (nepřímo)
        - bool: True jako 1+0j, False jako 0j
        - Vlastní typy implementující __complex__

    Srovnání s jinými protokoly:
        - SupportsFloat: pro převod na desetinné číslo
        - SupportsInt: pro převod na celé číslo
        - SupportsBytes: pro převod na bajty

    Praktické využití:
        - Zpracování signálů, komplexní algebra
        - Výpočty s vlastním typem čísel
        - Obalování hodnot v komplexních strukturách

    Běžné chyby:
        - Nevrácení komplexní hodnoty z metody __complex__
        - Zaměňování s typem complex
        - Nekompatibilní návratový typ z metody
        - Spoléhání se na implicitní převod

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.SupportsComplex
        - https://docs.python.org/3/reference/datamodel.html#object.__complex__
        - https://peps.python.org/pep-0544/
    """

    VALIDATOR_KEY = "supportscomplex"
    ANNOTATION = SupportsComplex

    IS_INSTANCE = SupportsComplex
    DUCK_TYPING = {
        "has_attr": "__complex__",
    }

    DESCRIPTION = "Objekt podporující konverzi na komplexní číslo"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje protokol SupportsComplex, "
            "tedy implementuje metodu __complex__, která umožňuje konverzi objektu "
            "na komplexní číslo pomocí funkce complex()."
        )

