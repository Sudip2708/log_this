from typing import AbstractSet
from collections.abc import Set

from ..._bases3 import BaseIterableValidator, T


class AbstractSetValidator(BaseIterableValidator):
    """
    Validátor pro typovou anotaci AbstractSet[T]

    AbstractSet reprezentuje abstraktní rozhraní pro množinové typy. Definuje společné vlastnosti
    a metody všech množinových typů bez ohledu na jejich mutabilitu (možnost změny obsahu).

    Syntaxe:
        - AbstractSet[T]      # Preferovaný zápis (vyžaduje import z typing)
        - collections.abc.Set # Třída z collections.abc modulu

    Příklady použití:
        - AbstractSet[int]    # Abstraktní množina celých čísel
        - AbstractSet[str]    # Abstraktní množina řetězců
        - AbstractSet[Tuple[int, str]]  # Abstraktní množina n-tic (int, str)

    Vnitřní typy:
        AbstractSet vyžaduje specifikaci typu T pro prvky množiny, kde T může být
        libovolný hashable typ (prvky musí být hashovatelné).

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Set
        2. Pokud je požadována hloubková kontrola, ověří typy všech prvků v množině
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_data(data: AbstractSet[str]) -> None
        - Pro návratové hodnoty: def get_unique_ids() -> AbstractSet[int]
        - Pro typové anotace proměnných: unique_names: AbstractSet[str]

    Porovnání s jinými množinovými typy:
        - AbstractSet je nadřazené rozhraní pro Set a FrozenSet
        - Na rozdíl od Set a MutableSet nespecifikuje mutabilitu (změnitelnost)
        - AbstractSet je užitečné, když záleží jen na operacích čtení množiny

    Kompatibilní typy:
        - set, frozenset, MutableSet, a další třídy implementující collections.abc.Set

    Běžné chyby:
        - Záměna s konkrétními typy Set nebo FrozenSet, kde AbstractSet je abstraktní rozhraní
        - Použití nehashable typů jako prvků množiny
        - Zapomenutí na import: from typing import AbstractSet

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.AbstractSet
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Set
    """

    VALIDATOR_KEY = "abstractset"
    ANNOTATION = AbstractSet[T]

    IS_INSTANCE = Set
    HAS_ATTRS = "__contains__", "__iter__", "__len__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Abstraktní množinový typ"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje protokol AbstractSet z collections.abc, "
            "tj. podporuje operace množin (např. in, iterace, porovnání)."
        )
