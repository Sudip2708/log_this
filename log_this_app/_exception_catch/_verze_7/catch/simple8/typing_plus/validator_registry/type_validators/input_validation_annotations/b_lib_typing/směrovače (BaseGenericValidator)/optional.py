from typing import Optional

from ...._bases import BaseGenericValidator, T


class OptionalValidator(BaseGenericValidator):
    """
    Validátor pro typovou anotaci Optional[T]

    Optional reprezentuje typ, který může být buď typu T, nebo None.
    Je to zkrácený zápis pro Union[T, None] - vyjadřuje tedy, že hodnota
    může být buď daného typu nebo chybět (být None).

    Syntaxe:
        - Optional[T]            # Hodnota může být typu T nebo None
        - T | None               # Alternativní zápis v Pythonu 3.10+

    Příklady použití:
        - Optional[int]          # Celé číslo nebo None
        - Optional[str]          # Řetězec nebo None
        - Optional[List[float]]  # Seznam desetinných čísel nebo None
        - str | None             # Pythonic syntax od verze 3.10

    Implementační detaily:
        Tento validátor je speciálním případem Union validátoru, který vždy
        obsahuje None jako jednu z možností. Validační proces je delegován
        na základní validate_typing metodu stejně jako u Union.

    Validační proces:
        1. Získá vnitřní typ pomocí get_args
        2. Předá validaci základní metodě validate_typing
        3. Ta ověří, zda hodnota je None nebo odpovídá specifikovanému typu
        4. Hodnota je platná, pokud je None nebo odpovídá vnitřnímu typu

    Použití v kódu:
        - Pro volitelné parametry:
          def process(data: str, timeout: Optional[int] = None)
        - Pro volitelné atributy tříd:
          class User:
              name: str
              email: Optional[str] = None
        - Pro návratové hodnoty, které mohou chybět:
          def find_user(id: int) -> Optional[User]

    Srovnání s Union:
        - Optional[T] je specifický případ Union[T, None]
        - Optional explicitně vyjadřuje, že hodnota může chybět
        - Optional je sémanticky výstižnější než Union pro vyjádření chybějících hodnot

    Běžné vzory použití:
        - Volitelné parametry funkcí
        - Atributy tříd, které mohou být nedefinované
        - Návratové hodnoty funkcí, které mohou selhat
        - Vyjádření nepovinných hodnot v datových strukturách

    Běžné chyby:
        - Zapomenutí výchozí hodnoty None u volitelných parametrů
        - Redundantní použití Optional[Optional[T]]
        - Používání Union[T, None] místo Optional[T]
        - Opomenutí kontroly na None před použitím hodnoty

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Optional
        - https://mypy.readthedocs.io/en/stable/kinds_of_types.html#optional-types-and-the-none-type
        - https://peps.python.org/pep-0484/#optional-types
    """

    VALIDATOR_KEY = "optional"
    ANNOTATION = Optional[T]
    INFO = "Definuje, že hodnota musí odpovídat alespoň jedné vnitřní definici, nebo mít hodnotu None."
    ORIGIN = Optional