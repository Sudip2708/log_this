from typing import Container
from collections.abc import Container as ContainerOrigin

from ..._bases import BaseIterableValidator, T


class ContainerValidator(BaseIterableValidator):
    """
    Validátor pro typovou anotaci Container[T]

    Container reprezentuje jednoduché rozhraní pro objekty, které umožňují testovat
    přítomnost prvku pomocí operátoru 'in'. Je to nejjednodušší forma kontejneru,
    která vyžaduje pouze implementaci metody __contains__.

    Syntaxe:
        - Container[T]              # Preferovaný zápis (vyžaduje import z typing)
        - collections.abc.Container # Třída z collections.abc modulu

    Příklady použití:
        - Container[int]            # Kontejner obsahující celá čísla
        - Container[str]            # Kontejner obsahující řetězce
        - Container[Tuple[int, str]] # Kontejner obsahující n-tice

    Požadované metody:
        Container vyžaduje, aby objekt implementoval pouze:
        - __contains__: Pro testování přítomnosti prvku (operátor 'in')

    Vnitřní typy:
        Container vyžaduje specifikaci typu T pro své prvky, kde T může být
        libovolný podporovaný typ, vůči kterému bude testována přítomnost v kontejneru.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Container
        2. Pokud je požadována hloubková kontrola, validace prvků se neprovádí,
           protože Container obecně nemá definovanou iteraci

    Použití v kódu:
        - Pro parametry funkcí: def has_element(container: Container[int], element: int) -> bool
        - Pro návratové hodnoty: def get_lookup_table() -> Container[str]
        - Pro typové anotace proměnných: lookup: Container[str] = {'a', 'b', 'c'}

    Hierarchie typů:
        - Container je základní stavební blok pro komplexnější kontejnery
        - Collection dědí z Container (přidává iterovatelnost a velikost)
        - Set, Sequence, Mapping atd. jsou všechny Container

    Kompatibilní typy:
        - Třídy, které implementují __contains__: list, tuple, set, frozenset, dict, str

    Kdy použít:
        - Když funkce potřebuje pouze testovat přítomnost prvků, nikoliv iterovat
        - Pro vytváření vlastních jednoduchých kontejnerů
        - Jako základní abstrakci pro lookup struktury

    Běžné chyby:
        - Záměna s Collection nebo Iterable, Container neposkytuje iterační protokol
        - Předpoklad, že Container umožňuje přístup k prvkům nebo iteraci
        - Zapomenutí na import: from typing import Container

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Container
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Container
    """

    VALIDATOR_KEY = "container"
    ANNOTATION = Container[T]
    INFO = "Definuje kontejner, který umožňuje testovat členství prvků."
    ORIGIN = ContainerOrigin