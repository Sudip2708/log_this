from typing import Iterable
from collections.abc import Iterator as IteratorOrigin

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class IterableValidator(BaseIterableValidator):
    """
    Validátor pro zápis Iterator[T]

    Iterator reprezentuje jakýkoli objekt, který implementuje metody __iter__ a __next__
    (získaný funkcí iter(), generátory, atd.).

    U iterátorů nemůžeme provádět hloubkovou kontrolu typů prvků,
    protože bychom je tím spotřebovali. Proto vždy vracíme True.

    Hint:
        Iterator[T] = Libovolný iterátor s prvky typu T

    Reprezentuje iterovatelný objekt:
        Iterable označuje typ objektu, který je možné iterovat.
        To znamená, že takový objekt implementuje metodu __iter__(), která vrací iterátor.

    Může být iterován vícekrát:
        Objekt typu Iterable může být obecně iterován vícekrát.
        Pokaždé, když zavoláš iter() na iterovatelném objektu, získáš nový iterátor,
        který začíná od začátku sekvence (pokud se nejedná o iterátor sám o sobě).

    Příklady:
        Seznamy (list), tuple (tuple), řetězce (str), množiny (set), slovníky (dict),
        generátory (které jsou zároveň iterable i iterátory), objekty implementující __iter__().

    Použití v typových anotacích:
        Používá se k označení, že funkce nebo proměnná očekává objekt, přes který
        je možné procházet jeho prvky pomocí smyčky for nebo funkce iter().

    Vztah mezi Iterable a Iterator:
        Můžeš si představit, že Iterable je "kontejner" nebo "zdroj" prvků,
        ze kterého můžeš získat "průvodce" pro procházení těchto prvků,
        a tím "průvodcem" je Iterator.

    Zjednodušeně:
        Iterable: "Něco, přes co se dá iterovat."
        Iterator: "Objekt, který provádí samotnou iteraci a vrací prvky jeden po druhém."
    """

    VALIDATOR_KEY = "iterable"
    ANNOTATION = Iterable[T]
    INFO = "Definuje jakýkoli objekt, který implementuje metody iterace."
    ORIGIN = IteratorOrigin
