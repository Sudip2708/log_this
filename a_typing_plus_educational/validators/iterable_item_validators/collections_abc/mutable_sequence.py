from typing import MutableSequence
from collections.abc import MutableSequence as MutableSequenceOrigin

from ...._bases import BaseIterableItemValidator, T


class MutableSequenceValidator(BaseIterableItemValidator):
    """
    Validátor pro typovou anotaci MutableSequence[T]

    MutableSequence reprezentuje měnitelnou sekvenční kolekci, která rozšiřuje Sequence
    o metody pro úpravu obsahu. Umožňuje přidávání, odebírání a modifikaci prvků.
    Typickým příkladem je list v Pythonu.

    Syntaxe:
        - MutableSequence[T]              # Preferovaný zápis (vyžaduje import z typing)
        - collections.abc.MutableSequence # Třída z collections.abc modulu

    Příklady použití:
        - MutableSequence[int]            # Měnitelná sekvence celých čísel
        - MutableSequence[str]            # Měnitelná sekvence řetězců
        - MutableSequence[Dict[str, int]] # Měnitelná sekvence slovníků

    Požadované metody:
        MutableSequence vyžaduje všechny metody z Sequence a navíc:
        - __setitem__: Pro nastavení hodnoty na určitém indexu
        - __delitem__: Pro odstranění hodnoty na určitém indexu
        - insert(): Pro vložení prvku na určitou pozici
        - append(): Pro přidání prvku na konec
        - reverse(): Pro obrácení pořadí prvků
        - extend(): Pro rozšíření o další prvky
        - pop(): Pro odstranění a vrácení prvku
        - remove(): Pro odstranění první instance prvku
        - __iadd__: Pro operátor += (in-place addition)

    Vnitřní typy:
        MutableSequence vyžaduje specifikaci typu T pro své prvky, kde T může být
        libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.MutableSequence
        2. Pokud je požadována hloubková kontrola, ověří typy všech prvků v sekvenci
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def modify_data(data: MutableSequence[int]) -> None
        - Pro návratové hodnoty: def create_list() -> MutableSequence[str]
        - Pro typové anotace proměnných: items: MutableSequence[float] = [1.0, 2.0, 3.0]

    Hierarchie typů:
        - MutableSequence dědí z Sequence
        - MutableSequence je konkrétnější než Sequence (přidává mutabilitu)
        - list a UserList jsou implementace MutableSequence

    Kompatibilní typy:
        - list, bytearray, UserList a další měnitelné sekvenční typy
        - Není kompatibilní s immutable sekvencemi jako tuple nebo str

    Kdy použít:
        - Když funkce potřebuje modifikovat předanou sekvenci
        - Pro parametry, které vyžadují list-like chování včetně možnosti úprav
        - Pro obecnější typ než konkrétní list, když záleží jen na operacích změny

    Běžné chyby:
        - Záměna se Sequence, která neumožňuje modifikaci
        - Použití pro immutable typy jako tuple nebo str
        - Zapomenutí na import: from typing import MutableSequence

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.MutableSequence
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence
    """

    VALIDATOR_KEY = "mutable_sequence"
    ANNOTATION = MutableSequence[T]

    IS_INSTANCE = MutableSequenceOrigin
    DUCK_TYPING = {
        "has_attr": (
            "__getitem__", "__setitem__", "__delitem__",
            "__len__", "__iter__", "insert"
        ),
    }

    DESCRIPTION = "Změnitelná sekvence prvků"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní MutableSequence "
            "z collections.abc, tedy že podporuje operace jako "
            "append, insert, __setitem__ a __delitem__ pro úpravu obsahu."
        )
