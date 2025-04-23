from typing import Sequence
from collections.abc import Sequence as SequenceOrigin

from ..._bases import BaseIterableValidator, T


class SequenceValidator(BaseIterableValidator):
    """
    Validátor pro typovou anotaci Sequence[T]

    Sequence reprezentuje sekvenční kolekci, která podporuje efektivní přístup k prvkům
    pomocí indexů, iteraci a má definovanou délku. Na rozdíl od MutableSequence,
    Sequence garantuje pouze operace pro čtení (nemůže být změněna).

    Syntaxe:
        - Sequence[T]              # Preferovaný zápis (vyžaduje import z typing)
        - collections.abc.Sequence # Třída z collections.abc modulu

    Příklady použití:
        - Sequence[int]            # Sekvence celých čísel
        - Sequence[str]            # Sekvence řetězců
        - Sequence[Tuple[int, str]] # Sekvence n-tic

    Požadované metody:
        Sequence vyžaduje, aby objekt implementoval:
        - __getitem__: Pro přístup k prvkům pomocí indexu
        - __len__: Pro získání délky sekvence
        A dědí požadavky:
        - __iter__: Pro iteraci (z Iterable)
        - __contains__: Pro operátor 'in' (z Container)

    Vnitřní typy:
        Sequence vyžaduje specifikaci typu T pro své prvky, kde T může být
        libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Sequence
        2. Pokud je požadována hloubková kontrola, ověří typy všech prvků v sekvenci
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_data(data: Sequence[int]) -> None
        - Pro návratové hodnoty: def get_items() -> Sequence[str]
        - Pro typové anotace proměnných: items: Sequence[float] = (1.0, 2.0, 3.0)

    Hierarchie typů:
        - Sequence dědí z Collection (tedy i z Iterable, Container, Sized)
        - MutableSequence je podtypem Sequence (přidává mutační operace)
        - Konkrétní typy jako list, tuple jsou implementace Sequence

    Kompatibilní typy:
        - tuple, list, str, bytes, bytearray a další sekvenční typy
        - MutableSequence a jeho implementace

    Kdy použít:
        - Když funkce potřebuje pouze číst z sekvenčních dat (nezměnit je)
        - Pro funkce, které vyžadují indexování a délku, ale nepotřebují konkrétní typ
        - Pro parametry, které mohou přijímat jak tuples, tak i lists

    Běžné chyby:
        - Záměna s List, kde Sequence je obecnější a může být i immutable
        - Předpoklad možnosti změny obsahu (Sequence je jen pro čtení)
        - Zapomenutí na import: from typing import Sequence

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Sequence
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence
    """

    VALIDATOR_KEY = "sequence"
    ANNOTATION = Sequence[T]
    INFO = "Definuje čtecí sekvenci položek"
    ORIGIN = SequenceOrigin