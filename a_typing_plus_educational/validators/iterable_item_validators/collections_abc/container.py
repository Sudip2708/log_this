from typing import Container
from collections.abc import Container as ContainerOrigin

from ...._bases import IterableValidatorBase, T
from ....validators import iterable_validator_for_container


class ContainerValidator(IterableValidatorBase):
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
        2. Pokud je požadována hloubková kontrola, validace prvků se provádí
        pouze pokud má Container definovanou i iteraci.
        To probýhá na základu ověření isinstance pro Iterable.

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
        - https://peps.python.org/pep-0544/ (protokoly a strukturální subtypování)
    """

    VALIDATOR_KEY = "container"
    ANNOTATION = Container[T]

    IS_INSTANCE = ContainerOrigin
    HAS_ATTRS = "__contains__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Objekt podporující operátor 'in'"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní Container z collections.abc, "
            "tedy že implementuje metodu __contains__, "
            "která umožňuje testovat přítomnost prvku pomocí operátoru 'in'."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Přetížení metody __call__."""

        return iterable_validator_for_container(
            value, self.ORIGIN, annotation, depth_check, custom_types, bool_only
        )