from typing import Iterator
from collections.abc import Iterator as IteratorOrigin

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class IteratorValidator(BaseIterableValidator):
    """
    Validátor pro zápis Iterator[T]

    Iterator reprezentuje jakýkoli objekt, který implementuje metody __iter__ a __next__
    (získaný funkcí iter(), generátory, atd.).

    Hint:
        Iterator[T] = Libovolný iterátor s prvky typu T

    Reprezentuje iterátor:
        Iterator označuje typ objektu, který implementuje metody __iter__()
        (která vrací self) a __next__(), a který postupně vrací prvky sekvence.

    Může být iterován pouze jednou (obvykle):
        Iterátor si udržuje svůj vnitřní stav a po vyčerpání prvků přestane vracet další.
        Pokud se pokusíš iterovat přes vyčerpaný iterátor znovu, nedostaneš žádné další prvky.

    Vzniká z Iterable:
        Iterátor je objekt, který získáš voláním funkce iter() na iterovatelném objektu.

    Příklady: 
        Objekt vrácený funkcí iter() na seznamu, iterátor generátoru.

    Použití v typových anotacích:
        Používá se k označení, že funkce nebo proměnná pracuje přímo s objektem,
        který vrací prvky jeden po druhém pomocí metody __next__().

    Vztah mezi Iterable a Iterator:
        Můžeš si představit, že Iterable je "kontejner" nebo "zdroj" prvků,
        ze kterého můžeš získat "průvodce" pro procházení těchto prvků,
        a tím "průvodcem" je Iterator.

    Zjednodušeně:
        Iterable: "Něco, přes co se dá iterovat."
        Iterator: "Objekt, který provádí samotnou iteraci a vrací prvky jeden po druhém."
    """

    VALIDATOR_KEY = "iterator"
    ANNOTATION = Iterator[T]
    INFO = "Definuje jakýkoli objekt, který implementuje metody iterace."
    GET_ORIGIN = IteratorOrigin

