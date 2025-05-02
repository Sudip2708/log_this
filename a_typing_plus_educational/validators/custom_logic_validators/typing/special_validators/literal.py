from typing import Literal

from ....._bases import BaseCustomLogicValidator
from ....._verifiers import literal_verifier


class LiteralValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci Literal[val1, val2, ...]

    Literal reprezentuje konkrétní doslovné hodnoty místo třídy typů. Definuje, že
    proměnná nebo parametr může nabývat pouze jedné z předem daných hodnot - podobně
    jako výčtový typ (enum) v jiných jazycích, ale jednodušeji.

    Syntaxe:
        - Literal[val1, val2, ...]  # Přesně definované povolené hodnoty

    Příklady použití:
        - Literal["red", "green", "blue"]     # Pouze tři specifické řetězce
        - Literal[1, 2, 3]                    # Pouze tři konkrétní čísla
        - Literal[True]                       # Pouze hodnota True
        - Literal["success", b"binary", 42]   # Kombinace různých typů hodnot

    Vlastnosti:
        - Literál je strukturální typ - kontroluje hodnotu, ne jen typ
        - Hodnotami literálu mohou být řetězce, čísla, True, False, None a některé další neměnné typy
        - Nelze použít proměnné jako hodnoty Literal - hodnoty musí být zadány přímo v kódu

    Validační proces:
        1. Získá konkrétní hodnoty z anotace pomocí get_args(annotation)
        2. Kontroluje, zda validovaná hodnota je mezi těmito povolenými hodnotami
        3. V případě neúspěchu buď vrátí False (bool_only=True) nebo vyvolá VerifyLiteralTypeError

    Použití v kódu:
        - Pro parametry s omezeným výběrem: def set_color(color: Literal["red", "green", "blue"])
        - Pro stavové proměnné: status: Literal["pending", "success", "error"] = "pending"
        - Pro API s přesnými požadavky: def api_call(method: Literal["GET", "POST", "PUT"])
        - Pro návratové hodnoty s přesnými stavy: def check() -> Literal[True]  # Může vrátit jen True

    Výhody Literal oproti Enum:
        - Jednodušší syntax bez nutnosti definovat třídu
        - Přímo používá běžné datové typy místo vlastních instancí
        - Přímočařejší pro jednoduché případy užití

    Kdy použít Literal:
        - Pro validaci proměnných, které mohou nabývat jen několika konkrétních hodnot
        - Pro zlepšení typových kontrol u funkcí s přesně definovanými vstupy/výstupy
        - Pro dokumentování API, které přijímá pouze konkrétní hodnoty

    Běžné chyby:
        - Pokus použít proměnnou v definici: Literal[SOME_CONSTANT]  # Nefunguje!
        - Použití mutable objektů v Literal (seznamy, slovníky) - není podporováno
        - Zaměnění s Union - Literal[int, str] NENÍ totéž co Union[int, str]

    Poznámky k výjimkám:
        - VerifyLiteralTypeError poskytuje informace o neplatné hodnotě a seznam povolených hodnot
        - Obsahuje informace pro řešení problému - které hodnoty jsou přijatelné

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Literal
        - https://peps.python.org/pep-0586/ (Literal Types)
        - https://mypy.readthedocs.io/en/stable/literal_types.html
    """

    VALIDATOR_KEY = "literal"
    ANNOTATION = Literal["a", "b", "c"]

    IS_INSTANCE = None
    HAS_ATTRS = None  # Nepodporuje validaci přes Duck Typing.
    CALLABLE_ATTRS = None  # Nepodporuje validaci přes Duck Typing.

    DESCRIPTION = "Doslovná hodnota jako typ"
    LONG_DESCRIPTION = (
            "Validuje, že typ je Literal, tedy že hodnota může nabývat "
            "jen konkrétních hodnot (např. Literal['a', 'b']). "
            "Používá se pro omezení hodnot."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření Literal."""

        return literal_verifier(
            value, annotation, bool_only
        )