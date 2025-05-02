from typing import FrozenSet

from ..._bases3 import BaseIterableValidator, T


class FrozenSetValidator(BaseIterableValidator):
    """
    Validátor pro typovou anotaci FrozenSet[T]

    FrozenSet reprezentuje neměnnou (immutable) množinu jedinečných prvků stejného typu.
    Na rozdíl od běžné množiny (Set) nemůže být po vytvoření modifikována - nelze přidávat,
    odebírat či měnit prvky. Díky své neměnnosti může být FrozenSet použit jako klíč
    ve slovníku nebo jako prvek v jiné množině.

    Syntaxe:
        - FrozenSet[T]         # Preferovaný zápis (vyžaduje import z typing)
        - frozenset[T]         # Od Python 3.9+
        - frozenset            # Obecný frozenset bez specifikace typu prvků

    Příklady použití:
        - FrozenSet[int]       # Neměnná množina celých čísel
        - FrozenSet[str]       # Neměnná množina řetězců
        - FrozenSet[Tuple[str, int]] # Neměnná množina dvojic (řetězec, číslo)
        - Dict[FrozenSet[int], str]  # Slovník s neměnnými množinami jako klíči

    Vnitřní typy:
        Anotace FrozenSet vyžaduje specifikaci typu vnitřních prvků T, kde T může být
        libovolný hashable typ. Prvky v neměnné množině musí být hashovatelné.

    Validační proces:
        1. Ověří, zda hodnota je instance typu frozenset
        2. Pokud je požadována hloubková kontrola, ověří typy všech prvků množiny
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_constant_items(items: FrozenSet[int]) -> None
        - Pro návratové hodnoty: def get_supported_formats() -> FrozenSet[str]
        - Pro typování proměnných: default_flags: FrozenSet[str] = frozenset({"read", "write"})
        - Jako klíče ve slovníku: cache_keys: Dict[FrozenSet[str], int] = {}

    Kompatibilita:
        - FrozenSet je kompatibilní s AbstractSet a Collection
        - FrozenSet není kompatibilní s běžnou množinou Set (ta je měnitelná)
        - FrozenSet může být použit jako klíč ve slovníku (Dict)
        - FrozenSet může být prvkem v jiné množině (Set nebo FrozenSet)

    Výhody oproti Set:
        - Může být použit jako klíč ve slovníku
        - Může být prvkem v jiné množině
        - Zaručuje neměnnost obsahu

    Běžné chyby:
        - Zapomenutí importu: from typing import FrozenSet
        - Pokus o modifikaci frozenset po jeho vytvoření
        - Používání běžného Set namísto FrozenSet pro případy, kde je potřeba neměnnost

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.FrozenSet
        - https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    """

    VALIDATOR_KEY = "frozenset"
    ANNOTATION = FrozenSet[T]

    IS_INSTANCE = frozenset
    HAS_ATTRS = "__contains__", "__iter__", "__len__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Neměnná množina"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je typu frozenset. "
            "Jedná se o neměnnou verzi množiny (set), která rovněž obsahuje "
            "pouze unikátní prvky a umožňuje množinové operace."
        )

