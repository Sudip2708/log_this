from typing import Generic

from ...._bases import BaseIsInstanceValidator, T


class GenericValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci Generic[T]

    Generic je základní konstrukt pro generické programování v Pythonu, umožňující 
    definovat třídy a funkce, které pracují s různými typy při zachování typové
    bezpečnosti. Používá se jako základní třída při vytváření vlastních generických
    typů.

    Syntaxe:
        - class MyGeneric(Generic[T]): ...     # Definice generické třídy s jedním parametrem
        - class KeyValue(Generic[K, V]): ...   # Definice s více parametry
        - T = TypeVar('T')                     # Deklarace typové proměnné (vždy nutná)

    Příklady použití:
        - class Stack(Generic[T]): ...         # Generický zásobník pro libovolný typ
        - class Mapping(Generic[K, V]): ...    # Generické mapování klíč-hodnota
        - class BinaryTree(Generic[T]): ...    # Generický binární strom

    Validační proces:
        1. Ověří, zda hodnota je instance typu Generic
        2. Generic je primárně určen pro použití jako předek třídy, nikoliv jako přímá
           anotace pro proměnné nebo parametry

    Použití v kódu:
        ```python
        from typing import Generic, TypeVar

        T = TypeVar('T')

        # Generický kontejner pro jeden prvek typu T.
        class Box(Generic[T]):
            def __init__(self, content: T):
                self.content: T = content

            def get(self) -> T:
                return self.content

        # Použití
        int_box = Box[int](123)        # Vytvoří Box s celým číslem
        str_box = Box[str]("hello")    # Vytvoří Box s řetězcem
        ```

    Specifické informace:
        - Typové proměnné: Generic musí být parametrizován typovými proměnnými (TypeVar)
        - Dědičnost: Při dědění z generické třídy je nutné specifikovat typové parametry
        - Vztah k Protocol: Generic a Protocol se mohou kombinovat pro vytváření
          generických protokolů
        - Řetězení: Generické typy lze řetězit (např. List[Box[int]])
        - Omezení: TypeVar může mít omezení (např. T = TypeVar('T', int, float))

    Běžné chyby:
        - Zapomenutí definovat TypeVar před použitím v Generic
        - Záměna pořadí typových proměnných (TypeVar) v Generic
        - Použití Generic jako přímé anotace místo jako předka třídy
        - Myšlení, že Generic automaticky upravuje chování instance
        - Překrytí typových proměnných v dědičnosti

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Generic
        - https://peps.python.org/pep-0484/#generics
        - https://mypy.readthedocs.io/en/stable/generics.html
    """

    VALIDATOR_KEY = "generic"
    ANNOTATION = Generic[T]

    IS_INSTANCE = Generic
    DUCK_TYPING = None

    DESCRIPTION = "Základní třída pro generické typy"
    LONG_DESCRIPTION = (
            "Validuje, že třída dědí z Generic, což umožňuje definovat "
            "generické třídy s typovými parametry. "
            "Je základem pro vytváření vlastních generických typů."
        )
