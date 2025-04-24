from typing import Iterable

from ...._bases import HasAttributeValidatorBase


class IterableValidator(HasAttributeValidatorBase):
    """
    Validátor pro typovou anotaci Iterable[T]

    Iterable reprezentuje objekty, které lze iterovat (procházet) pomocí for cyklu.
    Jedná se o objekty implementující metodu __iter__, která vrací iterátor.

    Syntaxe:
        - Iterable[T]       # Preferovaný zápis (vyžaduje import z typing)
        - Iterable          # Obecný iterovatelný objekt bez specifikace typu prvků

    Příklady použití:
        - Iterable[int]     # Iterovatelný objekt s celými čísly
        - Iterable[str]     # Iterovatelný objekt s řetězci
        - Iterable[Dict[str, Any]]  # Iterovatelný objekt s komplexními typy

    Vnitřní typy:
        Anotace Iterable typicky vyžaduje specifikaci typu T, který reprezentuje
        typ prvků, jež objekt poskytuje při iteraci. T může být libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda objekt implementuje metodu '__iter__'
        2. Neprovádí hloubkovou kontrolu typů iterovaných prvků

    Použití v kódu:
        - Pro parametry funkcí: def process_items(data: Iterable[int]) -> int
        - Pro návratové hodnoty: def get_data() -> Iterable[str]
        - Pro typování proměnných: values: Iterable[float] = [1.0, 2.5, 3.7]

    Protokolové požadavky:
        Pro správnou implementaci Iterable[T] objekt musí:
        - Implementovat metodu '__iter__', která vrací iterátor (objekt s metodou '__next__')
        - Iterátor vrácený metodou '__iter__' musí poskytovat prvky typu T

    Příklad implementace:
        ```python
        class CountUp(Iterable[int]):
            def __init__(self, limit: int):
                self.limit = limit

            def __iter__(self):
                return CountUpIterator(self.limit)

        class CountUpIterator:
            def __init__(self, limit: int):
                self.limit = limit
                self.current = 0

            def __next__(self):
                if self.current < self.limit:
                    value = self.current
                    self.current += 1
                    return value
                raise StopIteration
        ```

    Běžné použití:
        ```python
        def sum_values(values: Iterable[int]) -> int:
            total = 0
            for value in values:  # Využívá __iter__ pro získání iterátoru
                total += value
            return total
        ```

    Konkrétní příklady implementujících objektů:
        - list, tuple, set, dict, str, bytes, bytearray
        - Generátory vytvořené pomocí yield
        - Objekty vracené funkcí range()
        - Vlastní třídy implementující __iter__

    Srovnání s jinými typy:
        - Iterator: Je speciálním případem Iterable, který navíc implementuje __next__
        - AsyncIterable: Asynchronní verze pro použití s 'async for'
        - Sequence: Rozšiřuje Iterable o přístup k prvkům pomocí indexu a znalost délky

    Běžné chyby:
        - Záměna Iterable a Iterator (Iterable pouze poskytuje Iterator, sám jím není)
        - Předpoklad, že Iterable podporuje operátor 'in' (to vyžaduje Container)
        - Nesprávná implementace __iter__, která nevrací objekt s metodou __next__

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Iterable
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable
        - https://peps.python.org/pep-0544/ (protokoly a strukturální subtypování)
    """

    VALIDATOR_KEY = "iterable"
    ANNOTATION = Iterable
    INFO = "Definuje, že objekt musí implementovat __iter__"
    ORIGIN = "__iter__"