from typing import Callable

from ....._bases import BaseCustomLogicValidator
from ....._verifiers import callable_verifier

class CallableValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci Callable

    Callable reprezentuje volatelný objekt (funkci, metodu, lambda výraz nebo třídu s metodou
    __call__). Typová anotace Callable umožňuje specifikovat typy argumentů a návratové
    hodnoty volatelného objektu.

    Syntaxe:
        - Callable                        # Obecný volatelný objekt bez specifikace typů
        - Callable[..., ReturnType]       # Volatelný objekt s libovolnými argumenty a daným návratovým typem
        - Callable[[Arg1Type, Arg2Type], ReturnType]  # Volatelný objekt s konkrétními typy argumentů

    Příklady použití:
        - Callable                        # Jakákoliv funkce nebo volatelný objekt
        - Callable[..., None]             # Funkce s libovolnými argumenty, která nevrací hodnotu
        - Callable[[int, str], bool]      # Funkce přijímající int a str, vracející bool
        - Callable[[Dict[str, Any]], List[int]]  # Funkce přijímající slovník a vracející seznam celých čísel

    Implementační detaily:
        Tento validátor využívá BaseCustomLogicValidator jako základ a pro samotnou validaci
        volá funkci callable_verifier, která ověřuje, zda je objekt volatelný pomocí funkce
        callable().

    Validační proces:
        1. Ověří, zda je hodnota volatelná (funkce, metoda, objekt s metodou __call__)
        2. Nevaliduje signaturu funkce (typy argumentů a návratových hodnot)
        3. Pro základní validaci stačí, že objekt je volatelný

    Použití v kódu:
        - Pro parametry funkcí: def apply_function(func: Callable[[int], str]) -> None
        - Pro návratové hodnoty: def get_processor() -> Callable[[str], List[str]]
        - Pro typování proměnných: handler: Callable = lambda x: x * 2

    Specifické informace:
        - Callable v typových anotacích pouze určuje, že objekt je volatelný, ale negarantuje
          kompatibilitu argumentů nebo návratových hodnot
        - Pro plnou validaci typů argumentů a návratové hodnoty by byla potřeba inspekce
          signatury funkce, což tento validátor neprovádí
        - Od Python 3.10 lze použít i zápis pomocí |, např.: def foo(cb: Callable[[int], str] | None)

    Běžné chyby:
        - Záměna zápisu Callable[[ArgType], ReturnType] za Callable[ArgType, ReturnType]
        - Vynechání druhého páru hranatých závorek pro argumenty
        - Nesprávné předpokládání, že validátor kontroluje i typy argumentů a návratovou hodnotu
        - Zapomenutí importu: from typing import Callable

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Callable
        - https://peps.python.org/pep-0484/#callables
        - https://mypy.readthedocs.io/en/stable/kinds_of_types.html#callable-types-and-lambdas
    """

    VALIDATOR_KEY = "callable"
    ANNOTATION = Callable

    IS_INSTANCE = callable
    DUCK_TYPING = None

    DESCRIPTION = "Volatelný objekt (funkce, metoda)"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je Callable, tj. může být volán jako funkce. "
            "Lze specifikovat vstupní i návratové typy."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření volatelnosti objektu."""

        return callable_verifier(
            value
        )
