from typing import Hashable, Any, Tuple, Union

from ..._bases import BaseHasAttrValidator
from .exceptions import (
    VerifyValueHasAttributeError,
    VerifyExpectedHasAttributeError,
    VerifyInternalUnexpectedError,
    VerifyError
)


class HashableValidator(BaseHasAttrValidator):
    """
    Validátor pro typovou anotaci Hashable

    Hashable reprezentuje objekty, které lze použít jako klíče ve slovníku nebo jako prvky množiny.
    Jedná se o objekty implementující metodu __hash__, která vrací celé číslo (hash hodnotu objektu),
    a mají také definovanou metodu __eq__ pro porovnávání ekvivalence.

    Syntaxe:
        - Hashable          # Preferovaný zápis (vyžaduje import z typing)

    Příklady použití:
        - Hashable          # Hashable objekt použitelný jako klíč ve slovníku

    Poznámka k typům:
        Na rozdíl od většiny ostatních generických typů, Hashable není parametrizovaný.
        Typ hodnoty reprezentované hashovatelným objektem není součástí typové anotace.

    Validační proces:
        1. Ověří, zda objekt implementuje metodu '__hash__'
        2. Ověří, zda hodnota __hash__ není None (u tříd, kde je hashovatelnost zakázána)
        3. Neprovádí kontrolu návratové hodnoty metody '__hash__'

    Použití v kódu:
        - Pro parametry funkcí: def process_key(key: Hashable) -> int
        - Pro návratové hodnoty: def get_dict_key() -> Hashable
        - Pro typování proměnných: cache_key: Hashable = (1, "a", True)

    Protokolové požadavky:
        Pro správnou implementaci Hashable objekt musí:
        - Implementovat metodu '__hash__', která vrací celé číslo
        - Implementovat metodu '__eq__' pro porovnávání ekvivalence
        - Zajistit konzistenci: pokud a == b, pak hash(a) == hash(b)
        - Objekty, které jsou si rovny, musí mít stejné hash hodnoty

    Příklad implementace:
        ```python
        class Point(Hashable):
            def __init__(self, x: int, y: int):
                self.x = x
                self.y = y

            def __hash__(self) -> int:
                return hash((self.x, self.y))

            def __eq__(self, other) -> bool:
                if not isinstance(other, Point):
                    return NotImplemented
                return self.x == other.x and self.y == other.y
        ```

    Běžné použití:
        ```python
        def add_to_set(item: Hashable, collection: Set[Hashable]) -> None:
            collection.add(item)  # Pouze hashable objekty lze přidat do množiny

        def use_as_key(key: Hashable, value: Any, mapping: Dict[Hashable, Any]) -> None:
            mapping[key] = value  # Pouze hashable objekty lze použít jako klíče
        ```

    Konkrétní příklady hashovatelných objektů:
        - Neměnné objekty: int, float, str, bytes, complex, tuple (s hashable obsahem)
        - Frozenset (s hashable obsahem)
        - None, True, False
        - Vlastní třídy s implementovanými __hash__ a __eq__

    Nehashable objekty:
        - Měnitelné objekty: list, dict, set
        - Vlastní třídy bez __hash__ nebo s __hash__ = None

    Vlastnosti hashovatelných typů:
        - Obecně by měly být neměnné (immutable), nebo se minimálně chovat jako neměnné
        - Pokud se objekt změní, jeho hash hodnota by měla zůstat stejná
        - Běžná konvence je, že měnitelné objekty nejsou hashovatelné

    Běžné chyby:
        - Pokus o použití měnitelného objektu jako klíče ve slovníku
        - Implementace __hash__ bez odpovídající implementace __eq__
        - Změna stavu hashovatelného objektu, což může vést k nekonzistentnosti
        - Nesprávná implementace __hash__, která porušuje pravidlo hash(a) == hash(b) pro a == b

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Hashable
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable
        - https://docs.python.org/3/glossary.html#term-hashable
    """

    VALIDATOR_KEY = "hashable"
    ANNOTATION = Hashable
    INFO = "Definuje, že objekt musí implementovat metodu __hash__"
    ORIGIN = "__hash__",

    def __call__(
            self,
            value: Any,
            annotation: Any,
            inner_check: Union[bool, int],
            custom_types: Tuple[Any, ...],
            bool_only: bool
    ) -> Union[bool, Any]:

        try:

            # Ověření, zda objekt má všechny požadované atributy
            if hasattr(value, "__hash__") and value.__hash__ is not None:
                return True

            # Kontrola zda odpověď má být bool
            if bool_only:
                return False

            # Zjištění chybějících atributů pro lepší výpis chyby
            raise VerifyValueHasAttributeError(
                value, self.ORIGIN, self.ANNOTATION
            )

        except VerifyError:
            raise

        except TypeError as e:
            raise VerifyExpectedHasAttributeError(expected) from e

        except Exception as e:
            raise VerifyInternalUnexpectedError(
                info="Chyba nastala při validaci přítomnosti atributů.",
                modul="Zachyceno v metodě __call__ třídy ValidateHasAttribute.",
                original_exception=e
            ) from e