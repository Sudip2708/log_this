from typing import Container
from collections.abc import Container as ContainerOrigin

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class ContainerValidator(BaseIterableValidator):
    """
    Validátor pro zápis Container[T]

    Container reprezentuje kontejner, který implementuje metodu __contains__.
    Umožňuje testovat přítomnost prvku pomocí operátoru 'in'.

    Hint:
        Container[T] = Kontejner, který umožňuje testovat členství prvků typu T.

    Reprezentuje kontejner:
        Container je abstraktní třída definující základní rozhraní pro kontejnery,
        které umožňují testovat přítomnost prvků pomocí operátoru 'in'.

    Základní operace:
        * Testování členství: item in container

    Vztah s ostatními abstrakcemi:
        Container je základní abstrakce, která je součástí složitějších abstrakcí jako Collection,
        Set nebo Mapping. Samotný Container definuje pouze operaci testování členství.

    Příklady konkrétních typů:
        Seznamy (list), tuple (tuple), množiny (set), slovníky (dict pro klíče).

    Použití v typových anotacích:
        Používá se k označení, že funkce nebo proměnná očekává objekt,
        který umožňuje testovat členství prvků.
    """

    VALIDATOR_KEY = "container"
    ANNOTATION = Container[T]
    INFO = "Definuje kontejner, který umožňuje testovat členství prvků."
    GET_ORIGIN = ContainerOrigin