from typing import MutableSet
from collections.abc import MutableSet as MutableSetOrigin

from ...._bases import BaseIterableItemValidator, T


class MutableSetValidator(BaseIterableItemValidator):
    """
    Validátor pro typovou anotaci MutableSet[T]

    MutableSet reprezentuje měnitelnou množinu, která rozšiřuje základní rozhraní
    AbstractSet o metody pro přidávání, odebírání a modifikaci prvků. Typickým
    příkladem je built-in set v Pythonu.

    Syntaxe:
        - MutableSet[T]              # Preferovaný zápis (vyžaduje import z typing)
        - collections.abc.MutableSet # Třída z collections.abc modulu

    Příklady použití:
        - MutableSet[int]            # Měnitelná množina celých čísel
        - MutableSet[str]            # Měnitelná množina řetězců
        - MutableSet[Tuple[int, str]] # Měnitelná množina n-tic

    Požadované metody:
        MutableSet vyžaduje všechny metody z AbstractSet a navíc:
        - add(): Přidání prvku do množiny
        - discard(): Odstranění prvku z množiny (bez vyhození výjimky, pokud prvek neexistuje)
        - __ior__: Operátor |= (in-place union)
        - __iand__: Operátor &= (in-place intersection)
        - __ixor__: Operátor ^= (in-place symmetric difference)
        - __isub__: Operátor -= (in-place difference)

    Vnitřní typy:
        MutableSet vyžaduje specifikaci typu T pro své prvky, kde T musí být
        hashable typ (prvky musí být hashovatelné).

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.MutableSet
        2. Pokud je požadována hloubková kontrola, ověří typy všech prvků v množině
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def update_set(unique_items: MutableSet[str]) -> None
        - Pro návratové hodnoty: def create_unique_ids() -> MutableSet[int]
        - Pro typové anotace proměnných: tags: MutableSet[str] = {"python", "typing"}

    Hierarchie typů:
        - MutableSet dědí z AbstractSet
        - MutableSet je konkrétnější než AbstractSet (přidává mutabilitu)
        - set a UserSet jsou implementace MutableSet
        - frozenset implementuje AbstractSet, ale ne MutableSet

    Kompatibilní typy:
        - set, UserSet a další měnitelné množinové typy
        - Není kompatibilní s immutable množinami jako frozenset

    Kdy použít:
        - Když funkce potřebuje modifikovat předanou množinu
        - Pro parametry, které vyžadují set-like chování včetně možnosti úprav
        - Pro reprezentaci kolekcí, kde záleží na jedinečnosti prvků a potřebujeme je měnit

    Běžné chyby:
        - Záměna s AbstractSet nebo Set, které mohou být i immutable
        - Použití nehashable typů jako prvků množiny
        - Zapomenutí na import: from typing import MutableSet
        - Předpoklad uspořádání prvků (množiny jsou neuspořádané)

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.MutableSet
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSet
    """

    VALIDATOR_KEY = "mutableset"
    ANNOTATION = MutableSet[T]

    IS_INSTANCE = MutableSetOrigin
    DUCK_TYPING = {
        "has_attr": ("__contains__", "__iter__", "__len__", "add", "discard"),
    }

    DESCRIPTION = "Změnitelná množina"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní MutableSet z collections.abc, "
            "tedy že podporuje operace jako add, discard, __ior__ "
            "pro úpravu obsahu množiny."
        )
