from typing import ParamSpec

from ...._bases import BaseIsInstanceValidator


class ParamSpecValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci ParamSpec

    ParamSpec je speciální konstrukt Pythonu pro typovou anotaci parametrů funkcí
    vyšších řádů. Umožňuje zachovat a přenášet informace o signaturách funkcí
    včetně klíčových a poziční parametrů, což je zásadní pro správnou typovou
    kontrolu dekorátorů a funkcí pracujících s jinými funkcemi.

    Syntaxe:
        - P = ParamSpec('P')             # Definice proměnné typu ParamSpec
        - def func(*args: P.args, **kwargs: P.kwargs) -> RetType: ...
        - def wrapper(f: Callable[P, R]) -> Callable[P, R]: ...

    Příklady použití:
        - Pro dekorátory:
          ```python
          P = ParamSpec('P')
          R = TypeVar('R')

          def logging_decorator(f: Callable[P, R]) -> Callable[P, R]:
              def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
                  print(f"Calling {f.__name__}")
                  return f(*args, **kwargs)
              return wrapped
          ```
        - Pro funkce vyššího řádu:
          ```python
          def with_retry(f: Callable[P, R]) -> Callable[P, R]: ...
          ```

    Validační proces:
        1. Ověří, zda hodnota je instance typu ParamSpec
        2. ParamSpec je primárně určen pro použití v anotacích funkcí vyššího řádu
           a není určen k přímé validaci hodnot

    Použití v kódu:
        - P = ParamSpec('P')
        - R = TypeVar('R')
        - def map_result(func: Callable[P, int]) -> Callable[P, str]:
              def inner(*args: P.args, **kwargs: P.kwargs) -> str:
                  return str(func(*args, **kwargs))
              return inner

    Specifické informace:
        - ParamSpec.args a ParamSpec.kwargs: Speciální atributy pro přístup k
          pozičním a klíčovým argumentům
        - Concatenate[ParamSpec, ...]: Lze kombinovat s Concatenate pro přidání
          dalších parametrů k existující signaturě
        - Od Python 3.10: ParamSpec byl přidán v Pythonu 3.10
        - Vztah k TypeVar: ParamSpec je podobný TypeVar, ale specializovaný na
          parametry funkcí místo běžných hodnot

    Běžné chyby:
        - Záměna s TypeVar: ParamSpec má jiný účel než TypeVar a měl by být používán
          pouze pro parametry funkcí
        - Nesprávné použití P.args a P.kwargs: Tyto musí být použity s operátory
          * a ** v definici funkce
        - Nekonzistence v názvosloví: Konvence je používat 'P' jako název pro
          ParamSpec proměnné
        - Použití v nesprávném kontextu: ParamSpec je určen pro funkce vyššího řádu,
          nikoliv běžné typové anotace

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.ParamSpec
        - https://peps.python.org/pep-0612/ (Parameter Specification Variables)
        - https://mypy.readthedocs.io/en/stable/generics.html#paramspec
    """

    VALIDATOR_KEY = "paramspec"
    ANNOTATION = ParamSpec  # P = ParamSpec('P')

    IS_INSTANCE = ParamSpec
    DUCK_TYPING = {
        "has_attr": ("__name__", "__args__"),
    }

    DESCRIPTION = "Specifikace parametrů funkce"
    LONG_DESCRIPTION = (
            "Validuje, že typ používá ParamSpec, který zachycuje "
            "kompletní specifikaci parametrů funkce. "
            "Používá se při definici generických dekorátorů a vyšších funkcí."
        )
