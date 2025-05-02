from typing import Concatenate

from ....._bases import BaseCustomLogicValidator, P, T
from ....._verifiers import concatenate_verifier


class ConcatenateValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci Concatenate[P, Ts, ...]

    Concatenate je speciální konstrukt používaný v kombinaci s ParamSpec pro reprezentaci
    typové manipulace s argumenty funkcí. Slouží k přesné typové specifikaci při vytváření
    dekorátorů nebo vyšších řádových funkcí, které mění nebo rozšiřují signaturu funkcí.

    Syntaxe:
        - Concatenate[P, Arg1Type, Arg2Type, ...]  # P je ParamSpec
        - Concatenate[P, Arg1Type]                 # Jednoduchá konkatenace jednoho argumentu

    Příklady použití:
        - Concatenate[P, int]                      # Připojuje int argument před P
        - Concatenate[P, str, bool]                # Připojuje str a bool argumenty před P
        - Concatenate[P, Callable[..., T]]         # Připojuje callback před P
        - Concatenate[P, Self]                     # Připojuje Self typ (pro metody)

    Specifika typu:
        Concatenate se používá výhradně s ParamSpec a slouží jako operátor, který
        umožňuje "připojit" další typy argumentů před parametry reprezentované ParamSpec.
        Není určen pro běžné anotace proměnných, ale především pro typovou specifikaci
        při transformaci funkcí (dekorátory, wrappery, currying).

    Validační proces:
        1. Ověří, zda hodnota je instance typu Callable
        2. Pokud je požadována hloubková kontrola, bylo by teoreticky nutné ověřit
           signaturu funkce a validovat typy parametrů dle specifikace

    Použití v kódu:
        ```python
        from typing import Callable, Concatenate, ParamSpec, TypeVar

        P = ParamSpec('P')
        R = TypeVar('R')

        # Dekorátor, který přidává int parametr před původní parametry
        def add_context(
            f: Callable[Concatenate[int, P], R]
        ) -> Callable[P, R]:
            def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
                return f(42, *args, **kwargs)
            return wrapper

        @add_context
        def greet(context: int, name: str) -> str:
            return f"[{context}] Hello, {name}!"
        ```

    Vztah k ParamSpec:
        Concatenate lze použít pouze v kombinaci s ParamSpec. ParamSpec zachycuje
        všechny parametry funkce, zatímco Concatenate umožňuje specifikovat dodatečné
        parametry, které budou přidány před tyto zachycené parametry.

    Praktické využití:
        - Implementace dekorátorů, které přidávají argumenty k funkcím
        - Vytváření wrapperů a vyšších řádových funkcí se zachováním typové bezpečnosti
        - Typové anotace při funkcionálním programování (currying, partial application)
        - Middleware v webových aplikacích, které rozšiřují kontext funkcí

    Běžné chyby:
        - Použití bez ParamSpec (musí být vždy první parametr)
        - Použití pro anotace proměnných místo funkcí
        - Záměna s Union nebo Tuple (zcela jiné účely)
        - Nesprávné pochopení směru "concatenate" (přidává PŘED parametry, ne za)

    Omezení:
        - Funguje pouze s jednoduchými pozičními argumenty (nelze použít s klíčovými argumenty)
        - Nelze použít samostatně, vždy vyžaduje ParamSpec jako první argument

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Concatenate
        - https://peps.python.org/pep-0612/ (Parameter Specification Variables)
        - https://mypy.readthedocs.io/en/stable/generics.html#parameter-specification-variables
    """

    VALIDATOR_KEY = "concatenate"
    ANNOTATION = Concatenate[P, T]

    IS_INSTANCE = Concatenate
    HAS_ATTRS = None  # Nepodporuje validaci přes Duck Typing.
    CALLABLE_ATTRS = None  # Nepodporuje validaci přes Duck Typing.

    DESCRIPTION = "Rozšíření argumentů pro Callable"
    LONG_DESCRIPTION = (
            "Validuje, že Callable používá Concatenate, což umožňuje specifikovat "
            "další argumenty před ParamSpec – užitečné pro dekorátory."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření volatelnosti objektu."""

        return concatenate_verifier(
            value, annotation, depth_check, bool_only
        )
