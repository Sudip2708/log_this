from typing import Iterator
from collections.abc import Iterator as IteratorOrigin

from ...._bases import BaseIsInstanceValidator, T


class IteratorValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci Iterator[T]

    Iterator reprezentuje objekty, které umožňují postupné procházení prvků sekvence.
    Jedná se o objekty implementující metody __iter__ a __next__, přičemž __iter__
    typicky vrací sama sebe a __next__ poskytuje další prvek sekvence.

    Syntaxe:
        - Iterator[T]       # Preferovaný zápis (vyžaduje import z typing)
        - Iterator          # Obecný iterátor bez specifikace typu prvků
        - collections.abc.Iterator  # Třída z collections.abc modulu

    Příklady použití:
        - Iterator[int]     # Iterátor poskytující celá čísla
        - Iterator[str]     # Iterátor poskytující řetězce
        - Iterator[Tuple[str, int]]  # Iterátor poskytující n-tice

    Vnitřní typy:
        Anotace Iterator typicky vyžaduje specifikaci typu T, který reprezentuje
        typ prvků, jež iterátor poskytuje při volání __next__. T může být libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Iterator
        2. Neprovádí hloubkovou kontrolu typů poskytovaných prvků

    Použití v kódu:
        - Pro parametry funkcí: def consume_next(it: Iterator[int]) -> int
        - Pro návratové hodnoty: def create_iterator() -> Iterator[str]
        - Pro typování proměnných: counter: Iterator[int] = iter(range(10))

    Protokolové požadavky:
        Pro správnou implementaci Iterator[T] objekt musí:
        - Implementovat metodu '__iter__', která typicky vrací self
        - Implementovat metodu '__next__', která vrací další prvek typu T
        - Metoda '__next__' musí vyhodit výjimku StopIteration, když jsou prvky vyčerpány

    Příklad implementace:
        ```python
        class CountDown(Iterator[int]):
            def __init__(self, start: int):
                self.current = start

            def __iter__(self):
                return self

            def __next__(self):
                if self.current > 0:
                    value = self.current
                    self.current -= 1
                    return value
                raise StopIteration
        ```

    Běžné použití:
        ```python
        def process_iterator(it: Iterator[int]) -> int:
            try:
                # Získání dalšího prvku z iterátoru
                value = next(it)  # Volá metodu __next__
                return value
            except StopIteration:
                return -1  # Iterátor je vyčerpán
        ```

    Konkrétní příklady iterátorů:
        - Objekty vrácené funkcí iter() na iterovatelných objektech
        - Generátorové objekty (vytvořené funkcí s yield)
        - Objekty vracené vestavěnými funkcemi jako map(), filter(), zip()
        - File objekty pro čtení řádků souboru

    Srovnání s jinými typy:
        - Iterable: Iterator je speciálním případem Iterable s přidanou metodou __next__
        - AsyncIterator: Asynchronní verze pro použití s 'async for' a 'await'
        - Generator: Speciální typ Iterator vytvořený pomocí klíčového slova yield

    Běžné chyby:
        - Neošetření StopIteration výjimky při ručním volání next()
        - Opakované použití vyčerpaného iterátoru (iterátory jsou typicky jednorázové)
        - Zaměňování Iterable a Iterator (list je Iterable, ale ne Iterator)
        - Chybějící implementace __iter__ u vlastního iterátoru

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Iterator
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator
        - https://peps.python.org/pep-0234/ (iterátory a for cyklus)
    """

    VALIDATOR_KEY = "iterator"
    ANNOTATION = Iterator[T]

    IS_INSTANCE = IteratorOrigin
    DUCK_TYPING = {
        "has_callable_attr": ("__iter__", "__next__")
    }

    DESCRIPTION = "Iterátor s metodami __iter__ a __next__"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní Iterator z collections.abc, "
            "tedy že implementuje jak metodu __iter__, tak __next__ "
            "a může být použit pro postupné procházení hodnot."
        )
