from typing import SupportsIndex

from ...._bases import BaseIsInstanceValidator


class SupportsIndexValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci SupportsIndex

    SupportsIndex je protokol reprezentující objekty, které lze použít jako index
    v sekvencích (např. list, tuple) díky implementaci metody __index__.
    Tento protokol je užitečný např. pro slice operace, práci s numpy nebo bitové operace.

    Syntaxe:
        - SupportsIndex        # Jediný zápis (vyžaduje import z typing)

    Příklady použití:
        - SupportsIndex        # Jakýkoliv objekt, který lze použít jako index

    Validační proces:
        1. Ověří, zda objekt je instance SupportsIndex (implementuje metodu '__index__')
        2. Neprovádí kontrolu výstupní hodnoty ani rozsahu

    Použití v kódu:
        - Pro parametry funkcí: def access_item(index: SupportsIndex) -> Any
        - Pro návratové hodnoty: def get_index() -> SupportsIndex
        - Pro typování proměnných: start: SupportsIndex = MyIndex(0)

    Protokolové požadavky:
        Objekt musí:
        - Implementovat metodu '__index__', která vrací hodnotu typu int

    Příklad implementace:
        ```python
        class MyIndex(SupportsIndex):
            def __init__(self, value: int):
                self.value = value

            def __index__(self) -> int:
                return self.value
        ```

    Běžné použití:
        ```python
        def get_item(seq: list, index: SupportsIndex):
            return seq[index]

        get_item([10, 20, 30], 1)
        get_item([10, 20, 30], MyIndex(2))
        ```

    Kompatibilní typy:
        - int: standardní index
        - bool: True jako 1, False jako 0 (díky __index__)
        - numpy.int_ a další NumPy typy
        - vlastní typy implementující __index__

    Srovnání s jinými protokoly:
        - SupportsInt: pro obecnou konverzi na celé číslo
        - SupportsFloat: pro převod na float
        - SupportsComplex: pro převod na komplexní číslo
        - SupportsBytes: pro bajtové zobrazení

    Praktické využití:
        - Indexování sekvencí (list, tuple, string)
        - Slice operace: [start:stop:step]
        - NumPy a Pandas indexace
        - Bitové operace, práce s binárními strukturami

    Běžné chyby:
        - Implementace __int__ místo __index__
        - Nevracení typu int z metody __index__
        - Zaměňování SupportsInt a SupportsIndex (různé použití)
        - Použití float místo indexovatelných typů

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.SupportsIndex
        - https://docs.python.org/3/reference/datamodel.html#object.__index__
        - https://peps.python.org/pep-0357/ (motivace pro __index__)
    """

    VALIDATOR_KEY = "supportsindex"
    ANNOTATION = SupportsIndex

    IS_INSTANCE = SupportsIndex
    HAS_ATTRS = "__index__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Objekt použitelný jako index"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje protokol SupportsIndex, "
            "tedy implementuje metodu __index__, která umožňuje použít objekt "
            "jako index v sekvencích nebo při převodech mezi celočíselnými typy."
        )

