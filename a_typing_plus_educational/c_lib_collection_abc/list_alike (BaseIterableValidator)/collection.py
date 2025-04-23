from typing import Collection
from collections.abc import Collection as CollectionOrigin

from ..._bases import BaseIterableValidator, T


class CollectionValidator(BaseIterableValidator):
    """
    Validátor pro typovou anotaci Collection[T]

    Collection reprezentuje kontejner, který kombinuje tři základní protokoly: Iterable (iterovatelnost),
    Container (testování členství) a Sized (známá konečná velikost). Jedná se o běžnou abstrakci
    pro většinu kolekcí v Pythonu jako seznamy, množiny a slovníky.

    Syntaxe:
        - Collection[T]              # Preferovaný zápis (vyžaduje import z typing)
        - collections.abc.Collection # Třída z collections.abc modulu

    Příklady použití:
        - Collection[int]            # Kolekce celých čísel
        - Collection[str]            # Kolekce řetězců
        - Collection[Dict[str, int]] # Kolekce slovníků

    Požadované metody:
        Collection vyžaduje, aby objekt implementoval tyto metody:
        - __iter__: Pro iteraci přes položky (implementuje Iterable)
        - __contains__: Pro testování členství - operátor 'in' (implementuje Container)
        - __len__: Pro získání počtu položek - funkce len() (implementuje Sized)

    Vnitřní typy:
        Collection vyžaduje specifikaci typu T pro své prvky, kde T může být
        libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Collection
        2. Pokud je požadována hloubková kontrola, ověří typy všech prvků v kolekci
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_items(items: Collection[int]) -> None
        - Pro návratové hodnoty: def get_data() -> Collection[str]
        - Pro typové anotace proměnných: container: Collection[float] = [1.0, 2.0, 3.0]

    Hierarchie typů:
        - Collection je nadřazený typ pro Sequence, Set a další konkrétní kolekce
        - Collection dědí z Iterable, Container a Sized
        - Collection je podřazený vůči Iterable (každá Collection je Iterable, ale ne naopak)

    Kompatibilní typy:
        Třídy, které splňují Collection: list, tuple, set, frozenset, dict, str, bytes, bytearray atd.

    Kdy použít:
        - Když funkce potřebuje pracovat s jakoukoliv kolekcí bez ohledu na její specifický typ
        - Když potřebujete iterovat přes kolekci, testovat členství a znát její délku

    Běžné chyby:
        - Záměna s konkrétními typy jako List nebo Set, kde Collection je obecnější
        - Zapomenutí na import: from typing import Collection
        - Použití Collection pro objekty, které nesplňují všechny tři požadované protokoly

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Collection
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection
    """

    VALIDATOR_KEY = "collection"
    ANNOTATION = Collection[T]
    INFO = "Definuje kolekci, která je iterovatelná, umožňuje testovat členství a má konečnou délku."
    ORIGIN = CollectionOrigin