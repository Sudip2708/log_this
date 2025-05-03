from typing import Reversible
from collections.abc import Reversible as ReversibleOrigin

from ...._bases import BaseIsInstanceValidator, T


class ReversibleValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci Reversible[T]

    Reversible reprezentuje objekty, které lze procházet v opačném pořadí pomocí funkce reversed().
    Jedná se o objekty implementující metodu __reversed__, která vrací iterátor poskytující
    prvky v opačném pořadí.

    Syntaxe:
        - Reversible[T]     # Preferovaný zápis (vyžaduje import z typing)
        - Reversible        # Obecný reversible objekt bez specifikace typu prvků
        - collections.abc.Reversible  # Třída z collections.abc modulu

    Příklady použití:
        - Reversible[int]   # Reverzibilní objekt s celými čísly
        - Reversible[str]   # Reverzibilní objekt s řetězci
        - Reversible[Any]   # Reverzibilní objekt s libovolnými prvky

    Vnitřní typy:
        Anotace Reversible typicky vyžaduje specifikaci typu T, který reprezentuje
        typ prvků, jež objekt poskytuje při iteraci v opačném pořadí. T může být libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Reversible
        2. Neprovádí hloubkovou kontrolu typů iterovaných prvků

    Použití v kódu:
        - Pro parametry funkcí: def process_backwards(data: Reversible[int]) -> None
        - Pro návratové hodnoty: def get_reversible_data() -> Reversible[str]
        - Pro typování proměnných: values: Reversible[float] = [1.0, 2.5, 3.7]

    Protokolové požadavky:
        Pro správnou implementaci Reversible[T] objekt musí:
        - Implementovat metodu '__reversed__', která vrací iterátor (objekt s metodou '__next__')
        - Iterátor vrácený metodou '__reversed__' musí poskytovat prvky typu T v opačném pořadí
        - Objekt by měl být také Iterable (měl by implementovat __iter__)

    Příklad implementace:
        ```python
        class NumberRange(Reversible[int]):
            def __init__(self, start: int, end: int):
                self.start = start
                self.end = end

            def __iter__(self):
                current = self.start
                while current <= self.end:
                    yield current
                    current += 1

            def __reversed__(self):
                current = self.end
                while current >= self.start:
                    yield current
                    current -= 1
        ```

    Běžné použití:
        ```python
        def print_backwards(values: Reversible[int]) -> None:
            for value in reversed(values):  # Využívá __reversed__ pro získání iterátoru
                print(value)
        ```

    Konkrétní příklady implementujících objektů:
        - list, tuple, range
        - str (vrací znaky v opačném pořadí)
        - collections.deque
        - Vlastní třídy implementující __reversed__

    Srovnání s jinými typy:
        - Sequence: Mnoho sequence typů implementuje Reversible, ale ne všechny sekvence jsou reversibilní
        - Iterable: Reversible rozšiřuje Iterable o možnost iterace v opačném pořadí
        - Collection: Reversible může být Collection, pokud také splňuje Container a Sized protokoly

    Běžné chyby:
        - Předpoklad, že všechny iterovatelné objekty jsou také reverzibilní (např. set není reverzibilní)
        - Nesprávná implementace __reversed__, která nevrací iterátor
        - Zaměňování operace reverse() (modifikuje seznam na místě) a reversed() (vytváří nový iterátor)

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Reversible
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Reversible
        - https://docs.python.org/3/library/functions.html#reversed
    """

    VALIDATOR_KEY = "reversible"
    ANNOTATION = Reversible[T]

    IS_INSTANCE = ReversibleOrigin
    DUCK_TYPING = {
        "has_callable_attr": "__reversed__"
    }

    DESCRIPTION = "Objekt umožňující iteraci v opačném pořadí"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní Reversible z collections.abc, "
            "tedy že implementuje metodu __reversed__ a může být procházen "
            "v opačném pořadí, například pomocí funkce reversed()."
        )
