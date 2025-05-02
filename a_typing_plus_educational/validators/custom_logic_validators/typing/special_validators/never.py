try:
    from typing import Never
except ImportError:
    Never = type("NeverUnavailable", (), {})  # fallback pro starší Python

from ....._bases import BaseCustomLogicValidator
from ....._verifiers import never_verifier


class NeverValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci typing.Never

    Typ Never reprezentuje hodnotu, která nikdy nemůže existovat. Je používán pro označení
    kódu, který by nikdy neměl být dosažen, a to buď protože funkce vždy vyvolá výjimku,
    nebo kvůli logice typového systému, která vylučuje určité hodnoty.

    Syntaxe:
        - Never               # Vyžaduje import z modulu typing (from typing import Never)
        - typing.Never       # Alternativní zápis (import typing)

    Příklady použití:
        - def process_exhaustive_match(value: str) -> Never:  # Funkce, která vždy vyvolá výjimku
        - def assert_never(value: Never) -> Never:  # Pomocná funkce pro vyčerpávající kontrolu union typů
        - def impossible_case() -> Never:  # Označení větve kódu, která by nikdy neměla být dosažena

    Implementační detaily:
        Never je speciální typ, který označuje, že daný kód by nikdy neměl být dosažen nebo
        že funkce by nikdy neměla normálně vrátit hodnotu. Je to podtyp každého jiného typu,
        ale žádná hodnota není typu Never.

    Validační proces:
        1. Ověření Never není založeno na hodnotě, ale na kontextu použití
        2. Validátor vždy vrátí False, protože žádná hodnota nemůže být typu Never
        3. Používá se primárně pro statickou analýzu, ne runtime validaci

    Použití v kódu:
        - Pro návratové hodnoty: def fail(msg: str) -> Never: raise Exception(msg)
        - Pro pomocné funkce při vyčerpávajícím zpracování union typů:
          def assert_never(x: Never) -> Never: raise AssertionError("Unreachable")
        - Pro označení míst, která by neměla být dosažena: unreachable: Never  # mypy: error

    Srovnání s podobnými typy:
        - NoReturn: Podobný koncept, ale Never je novější a robustnější v typovém systému
        - None: Reprezentuje absenci hodnoty, zatímco Never reprezentuje nemožnost hodnoty
        - Any: Opak Never - kompatibilní s jakýmkoliv typem

    Běžné vzory použití:
        - Vyčerpávající kontrola variant (exhaustiveness checking):
          ```
          def process(value: Union[A, B, C]):
              if isinstance(value, A): ...
              elif isinstance(value, B): ...
              elif isinstance(value, C): ...
              else: assert_never(value)  # Statická kontrola že jsme pokryli všechny případy
          ```
        - Označení funkcí, které vždy vyvolají výjimku
        - Označení kódu, který by nikdy neměl být spuštěn

    Běžné chyby:
        - Použití Never jako běžného typu pro hodnoty
        - Záměna s NoReturn (starší ekvivalent)
        - Předpoklad, že Never je nějakým způsobem validovatelný za běhu

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Never
        - https://peps.python.org/pep-0661/ (Never type)
    """

    VALIDATOR_KEY = "never"
    ANNOTATION = Never

    IS_INSTANCE = Never
    HAS_ATTRS = None  # Nepodporuje validaci přes Duck Typing.
    CALLABLE_ATTRS = None  # Nepodporuje validaci přes Duck Typing.

    DESCRIPTION = "Typ, který nikdy nenastane"
    LONG_DESCRIPTION = (
            "Validuje, že typ je Never, tedy že daná větev kódu nebo funkce "
            "nikdy nevrací – např. nekonečná smyčka nebo výjimka."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření volatelnosti objektu."""

        return never_verifier(
            value
        )