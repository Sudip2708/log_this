from typing import Literal, get_args

from ..._bases import IsInstanceValidatorBase
from ...._exceptions import (
    VerifyLiteralTypeError,
    VerifyInternalUnexpectedError,
    VerifyError,
)


class LiteralValidator(IsInstanceValidatorBase):
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
    INFO = "Definuje povolené hodnoty"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):

        try:

            # Získání tuple s vnitřními typy
            inner_args = get_args(annotation)

            # Validace hodnoty vůči vnitřnímu typu
            if value in inner_args:
                return True

            # Kontrola zda odpověď má být bool
            if bool_only:
                return False

            # Vyvolání výjimky s oznamem o nevalidní hodnotě
            raise VerifyLiteralTypeError(value, inner_args)

        # Propagace vyvolané výjimky
        except VerifyError:
            raise

        # Zachycení neočekávaných výjimek
        except Exception as e:
            raise VerifyInternalUnexpectedError(
                info="Nastala chyba při ověřování objektu.",
                modul="Zachyceno v třídě LiteralValidator",
                original_exception=e
            ) from e