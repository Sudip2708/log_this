from typing import Iterable
from collections.abc import Iterable as IterableOrigin

from ...._bases import BaseIsInstanceValidator, T


class IterableValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci Iterable[T]

    Iterable reprezentuje jakýkoli objekt, přes který lze iterovat (pomocí for cyklu).
    Jedná se o základní abstrakci pro všechny objekty, které implementují metodu __iter__
    a vracejí iterátor.

    Syntaxe:
        - Iterable[T]              # Preferovaný zápis (vyžaduje import z typing)
        - collections.abc.Iterable # Třída z collections.abc modulu

    Příklady použití:
        - Iterable[int]            # Iterovatelný objekt obsahující celá čísla
        - Iterable[str]            # Iterovatelný objekt obsahující řetězce
        - Iterable[Any]            # Iterovatelný objekt s libovolnými prvky

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Iterable
        2. Vnitřní typy NEJSOU validovány, aby nedošlo k vyčerpání jednorázových iterátorů
           (např. generátorů)

    Použití v kódu:
        - Pro parametry funkcí: def process_all(data: Iterable[int]) -> None
        - Pro návratové hodnoty: def get_results() -> Iterable[str]
        - Pro typové anotace proměnných: elements: Iterable[float] = [1.0, 2.0, 3.0]

    Požadované metody:
        Iterable vyžaduje, aby objekt implementoval:
        - __iter__: Vrací iterátor pro procházení prvků

    Hierarchie typů:
        - Iterable je základní rozhraní pro všechny iterovatelné typy
        - Collection, Sequence, Set, atd. všechny dědí z Iterable
        - Iterator je speciální typ Iterable s rozšířenou funkcionalitou

    Kompatibilní typy:
        - Všechny běžné kolekce: list, tuple, set, dict, str
        - Generátory, iterátory, zobrazení (views)
        - Vlastní třídy implementující __iter__

    Kdy použít:
        - Když funkce potřebuje pouze iterovat přes prvky
        - Pro nejobecnější možný typ při příjmu jakýchkoliv iterovatelných dat
        - Pro funkce, které by měly přijímat generátory, iterátory i kolekce

    Implementační detaily:
        - Na rozdíl od specifických iterovatelných typů (List, Set atd.), u obecného
          Iterable validátor neprovádí hloubkovou kontrolu vnitřních typů, aby nedošlo
          k vyčerpání jednorázových iterátorů. Pro validaci vnitřních typů použijte
          specifičtější typy jako List[T], Tuple[T, ...] nebo Set[T].

    Běžné chyby:
        - Záměna s Iterator - Iterable lze použít vícekrát, Iterator je jednorázový
        - Předpoklad indexování nebo délky - Iterable garantuje pouze iteraci
        - Zapomenutí na import: from typing import Iterable
        - Spoléhání na kontrolu vnitřních typů, která u tohoto validátoru neprobíhá

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Iterable
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable
    """

    VALIDATOR_KEY = "iterable"
    ANNOTATION = Iterable[T]

    IS_INSTANCE = IterableOrigin
    DUCK_TYPING = {
        "has_callable_attr": "__iter__"
    }

    DESCRIPTION = "Objekt podporující iteraci"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní Iterable z collections.abc, "
            "tedy že implementuje metodu __iter__ a může být použit "
            "v cyklu for nebo ve funkcích jako iter()."
        )
