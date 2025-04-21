from typing import Union

from ...._bases import BaseGenericValidator, T1, T2


class UnionValidator(BaseGenericValidator):
    """
    Validátor pro typovou anotaci Union[T1, T2, ...]

    Union reprezentuje sjednocení typů - hodnota může být jakéhokoliv z uvedených typů.
    Validátor ověřuje, zda hodnota odpovídá alespoň jednomu z uvedených typů.

    Syntaxe:
        - Union[T1, T2, ...]            # Hodnota může být typu T1 nebo T2 nebo ...
        - T1 | T2 | ...                 # Alternativní zápis v Pythonu 3.10+

    Příklady použití:
        - Union[int, str]               # Hodnota může být celé číslo nebo řetězec
        - Union[float, None]            # Hodnota může být desetinné číslo nebo None
        - str | int | bool              # Pythonic syntax od verze 3.10
        - Union[List[int], Dict[str, Any], None]  # Komplexnější příklad

    Implementační detaily:
        Tento validátor deleguje validaci na základní validate_typing metodu.
        Hodnota je postupně validována proti každému typu v Union, dokud není
        nalezena shoda nebo nejsou vyčerpány všechny typy.

    Validační proces:
        1. Získá všechny vnitřní typy pomocí get_args
        2. Předá validaci základní metodě validate_typing
        3. Ta postupně zkouší validovat hodnotu proti každému vnitřnímu typu
        4. Hodnota je platná, pokud odpovídá alespoň jednomu vnitřnímu typu

    Použití v kódu:
        - Pro parametry s více možnými typy:
          def process(data: Union[str, bytes]) -> None
        - Pro návratové hodnoty různých typů:
          def fetch() -> Union[Dict[str, Any], None]
        - Pro volitelné parametry specifického typu (před Python 3.10):
          def configure(option: Union[int, None] = None)

    Srovnání s Optional:
        - Optional[T] je zkratka pro Union[T, None]
        - Optional explicitně vyjadřuje, že hodnota může být None
        - Union je obecnější a používá se pro různé kombinace typů

    Běžné vzory použití:
        - Funkce přijímající různé typy vstupních dat
        - Heterogenní kolekce dat
        - Funkce s potenciálně chybějícími nebo selhávajícími výstupy
        - Postupné zavedení typových anotací do projektu

    Běžné chyby:
        - Použití Union místo Optional pro hodnoty, které mohou být None
        - Příliš široké použití Union, což omezuje výhody statické typové kontroly
        - Zbytečné použití Union tam, kde by stačil jednodušší typ

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Union
        - https://peps.python.org/pep-0604/ (Operátor | pro union)
        - https://mypy.readthedocs.io/en/stable/kinds_of_types.html#union-types
    """

    VALIDATOR_KEY = "union"
    ANNOTATION = Union[T1,T2,...]
    INFO = "Definuje, že hodnota musí odpovídat alespoň jedné vnitřní definici."
    ORIGIN = Union

