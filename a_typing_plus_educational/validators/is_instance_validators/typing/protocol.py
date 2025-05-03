from typing import Protocol

from ...._bases import BaseIsInstanceValidator


class ProtocolValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci Protocol

    Protocol definuje strukturální podtypový vztah v Pythonu, kde třídy jsou kompatibilní
    s protokolem, pokud implementují všechny požadované metody a atributy,
    bez nutnosti explicitního dědění. Je to způsob, jak v Pythonu implementovat
    duck typing s podporou typové kontroly.

    Syntaxe:
        - class MyProtocol(Protocol): ...            # Definice protokolu
        - class MyGenericProtocol(Protocol[T]): ...  # Generický protokol

    Příklady použití:
        - Definice protokolu:
          ```python
          class Renderable(Protocol):
              def render(self) -> str: ...
          ```
        - Použití jako typová anotace:
          ```python
          def display(obj: Renderable) -> None:
              print(obj.render())
          ```
        - Generický protokol:
          ```python
          class SupportsGet(Protocol[T]):
              def get(self) -> T: ...
          ```

    Validační proces:
        1. Ověří, zda hodnota je instance typu Protocol
        2. Protocol se většinou používá jako báze pro definici protokolů, nikoliv
           jako přímá anotace hodnot
        3. Skutečná validace proti protokolu by měla ověřit, zda objekt implementuje
           všechny požadované metody a atributy

    Použití v kódu:
        - Pro definici rozhraní:
          ```python
          class Sized(Protocol):
              def __len__(self) -> int: ...

          def process(obj: Sized) -> None:
              print(f"Object size: {len(obj)}")
          ```
        - Pro abstraktní definici chování:
          ```python
          class Iterator(Protocol[T]):
              def __next__(self) -> T: ...
          ```

    Specifické informace:
        - Strukturální typování: Protocol umožňuje strukturální typování oproti
          nominálnímu typování běžnému v Pythonu
        - Runtime Protocols: S @runtime_checkable dekoratorem lze protokoly
          použít s isinstance()
        - Implicitní implementace: Třída nemusí explicitně dědit z protokolu
        - Protokoly jsou vhodné pro: Definici rozhraní, testování s mock objekty,
          zajištění kompatibility různých knihoven

    Běžné chyby:
        - Zapomenutí na Protocol dědičnost: class MyProto(Protocol): ...
        - Neimplementace všech metod při použití protokolu
        - Spoléhání na isinstance() bez @runtime_checkable dekoratoru
        - Nesprávná myšlenka, že Protocol vynutí implementaci metod (není to ABC)

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Protocol
        - https://peps.python.org/pep-0544/ (Protocols)
        - https://mypy.readthedocs.io/en/stable/protocols.html
    """

    VALIDATOR_KEY = "protocol"
    ANNOTATION = Protocol

    IS_INSTANCE = Protocol
    DUCK_TYPING = None

    DESCRIPTION = "Definice strukturálního typu"
    LONG_DESCRIPTION = (
            "Validuje, že třída dědí z Protocol, což umožňuje definovat "
            "strukturální typy namísto nominálních. "
            "Objekt odpovídá Protokolu, pokud implementuje požadované atributy a metody."
        )

