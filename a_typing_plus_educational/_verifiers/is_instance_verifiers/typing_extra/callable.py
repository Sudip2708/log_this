from typing import Callable

from ..._bases import IsInstanceValidatorBase
from ...._exceptions import (
    VerifyCallableTypeError,
    VerifyInternalUnexpectedError,
    VerifyError,
)


class CallableValidator(IsInstanceValidatorBase):
    """
    Validátor pro typovou anotaci Callable[[ArgType1, ArgType2, ...], ReturnType]

    Callable reprezentuje volatelný objekt - funkci, metodu nebo objekt implementující
    metodu __call__. V Pythonu je objekt volatelný, pokud na něm lze zavolat operaci
    volání pomocí závorek.

    Syntaxe:
        - Callable                             # Obecný volatelný objekt bez specifikace argumentů a návratové hodnoty
        - Callable[..., ReturnType]            # Volatelný objekt s libovolnými argumenty a specifickou návratovou hodnotou
        - Callable[[ArgType1, ArgType2], ReturnType]  # Volatelný objekt s konkrétními typy argumentů a návratovou hodnotou

    Příklady použití:
        - Callable                           # Jakýkoliv volatelný objekt
        - Callable[[], None]                 # Funkce bez parametrů, která nic nevrací
        - Callable[[int, str], bool]         # Funkce přijímající int a str, vracející bool
        - Callable[..., Dict[str, Any]]      # Funkce s libovolnými parametry, vracející slovník

    Implementační detaily:
        Tento validátor kontroluje POUZE, zda je hodnota volatelná (callable),
        ale nekontroluje typy argumentů ani návratovou hodnotu. Pro plnou
        typovou kontrolu včetně signatury by byla potřeba pokročilejší
        implementace využívající inspect modul.

    Validační proces:
        1. Ověří, zda je hodnota callable pomocí vestavěné funkce callable()
        2. V případě neúspěchu buď vrátí False (bool_only=True) nebo vyvolá VerifyCallableTypeError

    Použití v kódu:
        - Pro parametry funkcí vyššího řádu: def apply(fn: Callable[[int], str], value: int) -> str
        - Pro callback funkce: def register_handler(event: str, handler: Callable)
        - Pro definici parametrů dekorátorů: def my_decorator(func: Callable) -> Callable

    Co je "volatelné" v Pythonu:
        - Funkce (definované pomocí def nebo lambda)
        - Metody (včetně statických a třídních)
        - Třídy (volání třídy vytváří instanci)
        - Instance tříd s metodou __call__
        - Vestavěné funkce (např. len, print)
        - Funkce z modulů (např. os.path.exists)

    Běžné chyby:
        - Předání výsledku volání funkce místo funkce samotné: process(func()) místo process(func)
        - Očekávání volatelného objektu od proměnné, která obsahuje jinou hodnotu
        - Zapomenutí implementovat metodu __call__ v třídě, jejíž instance má být volatelná

    Poznámky k výjimkám:
        - VerifyCallableTypeError - vyvolána když hodnota není volatelná
        - Obsahuje podrobné informace o očekávaném typu a skutečné hodnotě
        - Poskytuje návrhy k řešení problému

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Callable
        - https://docs.python.org/3/reference/datamodel.html#object.__call__
        - https://peps.python.org/pep-0484/#callables
    """

    # Definice klíče pro registr
    VALIDATOR_KEY = "callable"
    ANNOTATION = Callable
    INFO = "Definuje volatelný objekt."
    ORIGIN = callable

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):

        try:

            # Ověření, zda se jedná o volatelný objekt
            if callable(value):
                return True

            # Kontrola zda odpověď má být bool
            if bool_only:
                return False

            # Vyvolání výjimky s oznamem o nevalidní hodnotě
            raise VerifyCallableTypeError(value)

        # Propagace vyvolané výjimky
        except VerifyError:
            raise

        # Zachycení neočekávaných výjimek
        except Exception as e:
            raise VerifyInternalUnexpectedError(
                info="Nastala chyba při ověřování objektu.",
                modul="Zachyceno v třídě CallableValidator",
                original_exception=e
            ) from e