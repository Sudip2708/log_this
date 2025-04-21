from typing import Container

from ..._bases import BaseHasAttrValidator


class ContainerValidator(BaseHasAttrValidator):
    """
    Validátor pro typovou anotaci Container[T]

    Container reprezentuje objekty, které podporují test příslušnosti prvku pomocí operátoru 'in'.
    Jedná se o objekt, který implementuje metodu __contains__, která určuje, zda daný objekt
    obsahuje specifický prvek.

    Syntaxe:
        - Container[T]      # Preferovaný zápis (vyžaduje import z typing)
        - Container         # Obecný kontejner bez specifikace typu prvků

    Příklady použití:
        - Container[int]    # Kontejner obsahující celá čísla
        - Container[str]    # Kontejner obsahující řetězce
        - Container[Any]    # Kontejner s libovolnými typy prvků

    Vnitřní typy:
        Anotace Container typicky vyžaduje specifikaci typu T, který reprezentuje
        typ prvků, jež kontejner může obsahovat. T může být libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda objekt implementuje metodu '__contains__'
        2. Neprovádí hloubkovou kontrolu typů obsažených prvků

    Použití v kódu:
        - Pro parametry funkcí: def check_presence(value: int, container: Container[int]) -> bool
        - Pro návratové hodnoty: def get_container() -> Container[str]
        - Pro typování proměnných: valid_values: Container[int] = {1, 2, 3}

    Protokolové požadavky:
        Pro správnou implementaci Container[T] objekt musí:
        - Implementovat metodu '__contains__(self, item)', která vrací boolean hodnotu
        - Metoda '__contains__' musí přijímat parametr typu T a vracet bool

    Příklad implementace:
        ```python
        class EvenNumbers(Container[int]):
            def __contains__(self, item: int) -> bool:
                return isinstance(item, int) and item % 2 == 0
        ```

    Běžné použití:
        ```python
        def is_present(value: int, container: Container[int]) -> bool:
            return value in container  # Využívá operátor 'in', který volá __contains__
        ```

    Konkrétní příklady implementujících objektů:
        - list, tuple, set, dict (klíče), str, bytes - všechny implementují Container
        - Vlastní datové struktury implementující protokol Container

    Srovnání s jinými typy:
        - Iterable: Na rozdíl od Container, Iterable umožňuje procházet prvky, ale nemusí podporovat test příslušnosti
        - Collection: Kombinace Container, Sized a Iterable
        - Sequence: Rozšiřuje Collection o přístup k prvkům pomocí indexu

    Běžné chyby:
        - Předpoklad, že Container musí být iterovatelný (nemusí implementovat __iter__)
        - Zaměňování Container s Collection (Collection vyžaduje více protokolů)
        - Nesprávná implementace __contains__, která nevrací boolean hodnotu

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Container
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Container
        - https://peps.python.org/pep-0544/ (protokoly a strukturální subtypování)
    """

    VALIDATOR_KEY = "container"
    ANNOTATION = Container
    INFO = "Definuje, že objekt musí implementovat metodu __contains__"
    ORIGIN = "__contains__"