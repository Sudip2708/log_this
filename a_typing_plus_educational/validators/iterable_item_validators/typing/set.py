from typing import Set

from ...._bases import BaseIterableItemValidator, T


class SetValidator(BaseIterableItemValidator):
    """
    Validátor pro typovou anotaci Set[T]

    Set reprezentuje množinu jedinečných prvků stejného typu. Na rozdíl od seznamu (List)
    neuchovává duplicitní hodnoty a nepřiřazuje prvkům konkrétní pořadí.

    Syntaxe:
        - Set[T]               # Preferovaný zápis (vyžaduje import z typing)
        - set[T]               # Od Python 3.9+
        - set                  # Obecná množina bez specifikace typu prvků

    Příklady použití:
        - Set[int]             # Množina celých čísel
        - Set[str]             # Množina řetězců
        - Set[Tuple[int, int]] # Množina dvojic celých čísel
        - Set[frozenset]       # Množina neměnných množin

    Vnitřní typy:
        Anotace Set vyžaduje specifikaci typu vnitřních prvků T, kde T může být
        libovolný hashable typ. Prvky v množině musí být hashovatelné.

    Validační proces:
        1. Ověří, zda hodnota je instance typu set
        2. Pokud je požadována hloubková kontrola, ověří typy všech prvků množiny
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_unique_items(items: Set[int]) -> None
        - Pro návratové hodnoty: def get_unique_tags() -> Set[str]
        - Pro typování proměnných: unique_names: Set[str] = {"Alice", "Bob"}

    Kompatibilita:
        - Set je kompatibilní s AbstractSet a Collection
        - Set není kompatibilní s List (ten uchovává duplicity a pořadí)
        - Set není kompatibilní s Dict (ten mapuje klíče na hodnoty)
        - Set není kompatibilní s FrozenSet (ten je neměnný)

    Omezení:
        - Prvky množiny musí být hashovatelné (immutable)
        - Nelze použít vnořené měnitelné typy jako list, dict nebo samotný set

    Běžné chyby:
        - Zapomenutí importu: from typing import Set
        - Pokus o vložení nehashable typu jako list nebo dict
        - Spoléhání na pořadí prvků, které není garantováno

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Set
        - https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    """

    VALIDATOR_KEY = "set"
    ANNOTATION = Set[T]

    IS_INSTANCE = set
    DUCK_TYPING = {
        "has_attr": ("__contains__", "__iter__", "__len__", "add", "discard"),
    }

    DESCRIPTION = "Vestavěná množina"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je typu set. "
            "Jedná se o změnitelnou neuspořádanou kolekci unikátních prvků, "
            "která podporuje množinové operace jako sjednocení, průnik či rozdíl."
        )
