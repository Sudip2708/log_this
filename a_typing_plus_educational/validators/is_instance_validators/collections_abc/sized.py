from typing import Sized
from collections.abc import Sized as SizedOrigin

from ...._bases import BaseIsInstanceValidator


class SizedValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci Sized

    Sized reprezentuje objekty, u kterých lze zjistit jejich velikost pomocí funkce len().
    Jedná se o objekty implementující metodu __len__, která vrací nezáporné celé číslo
    reprezentující počet prvků v objektu.

    Syntaxe:
        - Sized             # Preferovaný zápis (vyžaduje import z typing)
        - collections.abc.Sized  # Třída z collections.abc modulu

    Příklady použití:
        - Sized            # Objekt, jehož velikost lze zjistit pomocí len()

    Poznámka k typům:
        Na rozdíl od většiny ostatních generických typů, Sized není parametrizovaný.
        Typ prvků v objektu není součástí typové anotace Sized.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Sized
        2. Neprovádí kontrolu návratové hodnoty metody '__len__'

    Použití v kódu:
        - Pro parametry funkcí: def process_if_not_empty(collection: Sized) -> bool
        - Pro návratové hodnoty: def create_collection() -> Sized
        - Pro typování proměnných: data: Sized = [1, 2, 3]

    Protokolové požadavky:
        Pro správnou implementaci Sized objekt musí:
        - Implementovat metodu '__len__', která vrací nezáporné celé číslo
        - Metoda '__len__' by měla vrátit 0 pro prázdné objekty

    Příklad implementace:
        ```python
        class Matrix(Sized):
            def __init__(self, rows: int, cols: int):
                self.rows = rows
                self.cols = cols
                self.data = [[0 for _ in range(cols)] for _ in range(rows)]

            def __len__(self) -> int:
                return self.rows * self.cols  # Celkový počet prvků v matici
        ```

    Běžné použití:
        ```python
        def is_empty(collection: Sized) -> bool:
            return len(collection) == 0  # Využívá __len__ pro zjištění velikosti
        ```

    Konkrétní příklady implementujících objektů:
        - list, tuple, str, bytes, bytearray, dict, set, frozenset
        - collections.deque, collections.Counter
        - array.array
        - většina vlastních datových struktur

    Srovnání s jinými typy:
        - Container: Sized definuje velikost, ale nezajišťuje test příslušnosti prvku
        - Iterable: Sized objekty mohou, ale nemusí být iterovatelné
        - Collection: Kombinace Sized, Container a Iterable

    Běžné chyby:
        - Implementace __len__, která vrací záporné číslo (Python vyhodí ValueError)
        - Implementace __len__, která nevrací int (Python typicky automaticky konvertuje)
        - Předpoklad, že objekt s __len__ je také iterovatelný nebo indexovatelný

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Sized
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized
        - https://docs.python.org/3/library/functions.html#len
    """

    VALIDATOR_KEY = "sized"
    ANNOTATION = Sized

    IS_INSTANCE = SizedOrigin
    DUCK_TYPING = {
        "has_callable_attr": "__len__"
    }

    DESCRIPTION = "Objekt s definovanou velikostí"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní Sized z collections.abc, "
            "tedy že implementuje metodu __len__ a může být použit "
            "s funkcí len() pro zjištění počtu prvků."
        )
