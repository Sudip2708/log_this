from typing import Collection
from collections.abc import Collection as CollectionOrigin

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class CollectionValidator(BaseIterableValidator):
    """
    Validátor pro zápis Collection[T]

    Collection reprezentuje kontejner, který implementuje metody __iter__, __contains__ a __len__.
    Je to tedy iterovatelný kontejner s konečnou délkou.

    Hint:
        Collection[T] = Kontejner, který je iterovatelný, testovatelný na členství a má konečnou délku.

    Reprezentuje kontejner:
        Collection je abstraktní třída definující základní rozhraní pro kontejnery,
        které kombinují vlastnosti Sized, Iterable a Container.

    Základní operace:
        * Můžeš zjistit délku (len(x))
        * Můžeš iterovat prvky (for i in x)
        * Můžeš testovat členství (item in x)

    Vztah s ostatními abstrakcemi:
        Collection je základem pro konkrétnější abstrakce jako Sequence a Set.
        Je nadřazenou třídou pro většinu standardních kontejnerů v Pythonu.

    Příklady konkrétních typů:
        Seznamy (list), tuple (tuple), množiny (set), slovníky (dict).

    Použití v typových anotacích:
        Používá se k označení, že funkce nebo proměnná očekává obecný kontejner
        s možností iterace, testování členství a určení velikosti.
    """

    VALIDATOR_KEY = "collection"
    ANNOTATION = Collection[T]
    INFO = "Definuje kolekci, která je iterovatelná, umožňuje testovat členství a má konečnou délku."
    GET_ORIGIN = CollectionOrigin