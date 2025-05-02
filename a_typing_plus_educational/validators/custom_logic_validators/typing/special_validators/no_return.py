from typing import Any, Tuple, Union, NoReturn

from ....._bases import BaseCustomLogicValidator
from ....._verifiers import no_return_verifier


class NoReturnValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci typing.NoReturn

    Typ NoReturn označuje, že funkce nikdy nevrátí žádnou hodnotu, obvykle protože
    vždy vyvolá výjimku nebo ukončí program. Je to speciální anotace návratové hodnoty,
    která informuje typový systém, že daný kód nikdy nedokončí normální provádění.

    Syntaxe:
        - NoReturn               # Vyžaduje import z modulu typing (from typing import NoReturn)
        - typing.NoReturn        # Alternativní zápis (import typing)

    Příklady použití:
        - def exit_program(code: int) -> NoReturn: ...
        - def raise_error(message: str) -> NoReturn: ...
        - def infinite_loop() -> NoReturn: ...

    Implementační detaily:
        NoReturn je speciální typ, který se používá pouze jako návratová anotace funkcí.
        Označuje, že funkce nikdy normálně nevrátí hodnotu, ale místo toho vyvolá výjimku,
        ukončí program nebo vstoupí do nekonečné smyčky.

    Validační proces:
        1. NoReturn je pouze anotace návratové hodnoty, nemá smysl validovat vstupní hodnoty
        2. Validátor vždy vrátí False, protože žádná hodnota nemůže být typu NoReturn
        3. Používá se primárně pro statickou analýzu, ne runtime validaci

    Použití v kódu:
        - Pro návratové hodnoty: def exit(code: int) -> NoReturn: sys.exit(code)
        - Pro funkce vyhazující výjimky: def fail(msg: str) -> NoReturn: raise ValueError(msg)

    Srovnání s podobnými typy:
        - Never: Novější a obecnější koncept, který rozšiřuje myšlenku NoReturn
        - None: Označuje, že funkce vrací None, zatímco NoReturn označuje, že funkce nikdy nevrátí

    Běžné vzory použití:
        - Označení funkcí pro ukončení programu
        - Označení pomocných funkcí, které vždy vyvolají výjimku
        - Označení funkcí, které nikdy nedokončí provádění

    Běžné chyby:
        - Použití NoReturn jako běžného typu pro proměnné nebo parametry
        - Použití NoReturn pro funkce, které ve skutečnosti vracejí hodnotu
        - Záměna s None nebo Never

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.NoReturn
        - https://peps.python.org/pep-0484/ (Type Hints)
    """

    VALIDATOR_KEY = "noreturn"
    ANNOTATION = NoReturn

    IS_INSTANCE = NoReturn
    HAS_ATTRS = None  # Nepodporuje validaci přes Duck Typing.
    CALLABLE_ATTRS = None  # Nepodporuje validaci přes Duck Typing.

    DESCRIPTION = "Funkce, která nikdy nevrací"
    LONG_DESCRIPTION = (
            "Validuje, že funkce označená jako NoReturn nikdy nevrací "
            "hodnotu – typicky končí výjimkou nebo ukončením programu."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření volatelnosti objektu."""

        return no_return_verifier(
            value
        )