import logging
from typing import Optional, Dict, Any


from ._mixin_catch import CatchMixin
from ._mixin_handle import HandleMixin

from ._mixin_set_log_level import SetLogLevelMixin
from ._mixin_set_message import SetMessageMixin
from ._mixin_set_log_format import SetLogFormatMixin

from ._mixin_set_default_handler import SetDefaultHandlerMixin
from ._mixin_register_global_handler import RegisterGlobalHandlerMixin
from ._mixin_create_exception_group import CreateExceptionGroupMixin
from ._mixin_set_retry_strategy import SetRetryStrategyMixin

"""
Funkce:

    verify: Universální metoda pro ověřování podmínek.
    safe_verify: Bezpečná interní metoda pro ověřování vstupů.

    catch: Dekorátor pro zachytávání a zpracování výjimek.
    handle: Registrace vlastního handleru pro specifickou výjimku.

    set_log_level: Nastavení úrovně logování pro specifickou výjimku nebo globálně.
    set_message: Nastavení vlastní chybové zprávy pro specifickou výjimku.
    set_log_format: Nastavení formátu logování pro specifickou výjimku.

    set_default_handler: Nastavení globálního fallback handleru pro nezachycené výjimky.
    register_global_handler: Registrace globálního handleru pro specifické typy výjimek.
    create_exception_group: Vytvoření skupiny příbuzných výjimek.
    set_retry_strategy: Nastavení strategie opakování pro specifické výjimky.
"""

from .verify import verify

class ExceptionHandler(
    CatchMixin,
    HandleMixin,
    SetLogLevelMixin,
    SetMessageMixin,
    SetLogFormatMixin,
    SetDefaultHandlerMixin,
    RegisterGlobalHandlerMixin,
    CreateExceptionGroupMixin,
    SetRetryStrategyMixin
):
    """
    Třída pro zachycení a ošetření výjimek.

    Mixiny:

        CatchMixin: Dekorátor pro zachytávání a zpracování výjimek.
        HandleMixin: Registrace vlastního handleru pro specifickou výjimku.

        SetLogLevelMixin: Nastavení úrovně logování pro specifickou výjimku nebo globálně.
        SetMessageMixin: Nastavení vlastní chybové zprávy pro specifickou výjimku.
        SetLogFormatMixin: Nastavení formátu logování pro specifickou výjimku.

        SetDefaultHandlerMixin: Nastavení globálního fallback handleru pro nezachycené výjimky.
        RegisterGlobalHandlerMixin: Registrace globálního handleru pro specifické typy výjimek.
        CreateExceptionGroupMixin: Vytvoření skupiny příbuzných výjimek.
        SetRetryStrategyMixin: Nastavení strategie opakování pro specifické výjimky.

    """

    def __init__(
            self,
            logger: Optional[logging.Logger] = None,
            default_log_level: int = logging.ERROR
    ):
        self.logger = logger or logging.getLogger(__name__)
        self._default_log_level = default_log_level

        # Nové atributy pro ukládání nastavení
        self._log_formats: Dict[str, str] = {}
        self._custom_messages: Dict[type, str] = {}
        self._log_levels: Dict[type, int] = {}
        self._context_data: Dict[str, Any] = {}

        # Další nové atributy
        self._default_handler = None
        self._global_handlers = {}
        self._exception_groups = {}
        self._retry_strategies = {}

    def add_context(
            self,
            key: str,
            value: Any
    ) -> 'ExceptionHandler':
        """
        Přidání kontextové informace pro logování.

        :param key: Klíč kontextové informace
        :param value: Hodnota kontextové informace
        :return: Instance ExceptionHandleru pro řetězení volání
        """
        self._context_data[key] = value
        return self


# Globální instance
exception_handler = ExceptionHandler()
verify = verify
exception_catch = exception_handler.catch


# # Ukázka použití
# def example_usage():
#     # Vytvoření handleru s vlastním nastavením
#     handler = ExceptionHandler() \
#         .set_log_level(logging.WARNING, ValueError) \
#         .set_message("Kritická chyba validace", ValueError) \
#         .set_log_format("%(asctime)s - CUSTOM - %(message)s", ValueError) \
#         .add_context("application", "MyApp")
#
#
# # Příklad použití v kódu
# try:
#     # Nějaká riziková operace
#     raise ValueError("Testovací výjimka")
# except ValueError as e:
#     # Zde by byl vlastní logging s přizpůsobeným nastavením
#     pass


# # Příklad použití
# def example_usage():
#     handler = ExceptionHandler()
#
#     # Konfigurace před použitím
#     handler \
#         .set_log_level(logging.WARNING, ValueError) \
#         .set_message("Kritická chyba validace", ValueError) \
#         .set_log_format("CUSTOM: %(message)s", ValueError) \
#         .add_context("app_version", "1.0.0")
#
#     @handler.catch(ValueError, TypeError)
#     def example_function(x, y):
#         return x / y
#
#     try:
#         example_function(10, 0)  # Vyvolá ZeroDivisionError
#     except ZeroDivisionError:
#         print("Zachycena dělení nulou")


# # Příklad použití
# def example_usage():
#     handler = ExceptionHandler()
#
#     # Nastavení globálního handleru
#     handler.register_global_handler(
#         lambda e: print(f"Zachycena globální výjimka: {e}"),
#         ValueError, TypeError
#     )
#
#     # Nastavení default handleru
#     handler.set_default_handler(
#         lambda e: print(f"Nezachycená výjimka: {e}")
#     )
#
#     # Vytvoření skupiny výjimek
#     handler.create_exception_group(
#         "data_errors",
#         ValueError, TypeError, KeyError
#     )
#
#     # Nastavení strategie opakování
#     handler.set_retry_strategy(
#         ValueError,
#         max_attempts=3,
#         delay=0.5
#     )
#
#     @handler.catch()
#     def example_function(x, y):
#         return x / y

@exc_catch(ValueError, KeyError)
def example_function(x, y):
    return x / y

example_function.eset(
    set_log_level(logging.WARNING, ValueError),
    set_message("Kritická chyba validace", ValueError),
    set_log_format("%(asctime)s - CUSTOM - %(message)s", ValueError),
    add_context("application", "MyApp")
)

example_function.eset(
    {
        ValueError: {
            "message": "Chyba nesprávné hodnoty",
            "log_format": "%(asctime)s - CUSTOM - %(message)s",
            "log_level": logging.WARNING
        },
        KeyError: {
            "message": "Kritická chyba validace",
            "log_format": "%(asctime)s - CUSTOM - %(message)s",
            "log_level": logging.INFO
        },
    }
)

example_function.eset({
        ValueError: {"message": "Chyba nesprávné hodnoty",},
        KeyError: {"message": "Kritická chyba validace",},
    })

exc = example_function.handle(ValueError)
exc.set_log_level(logging.WARNING)
exc.set_message("Kritická chyba validace")
exc.set_log_format("%(asctime)s - CUSTOM - %(message)s")
exc.add_context("application", "MyApp")


# except KeyboardInterrupt:
#     cli_print.error.title("Zadávání přerušeno uživatelem...")
#     return None
#
# except ValueError:
#     raise ValidationError(
#         message="Zadaná hodnota musí bý celé číslo.")
#
# except Exception as e:
#     logging.error(f"Chyba v _go_up: {e}", exc_info=True)
#
# except FileExistsError:
#     return f"Chyba: Některá z rodičovských složek je soubor: {target_dir}"
#
# except (OSError, PermissionError) as e:
#     print("Po testu zůstal testovací soubor, který nelze smazat.")
#     print(f"Cesta k souboru: {self._test_file}")
#     print(f"Zachycené podrobnosti: {e}")
#     print("Možné řešení: Zkontrolujte umístění a pokuste se soubor smazat ručně.")
#
# except AttributeError as e:
#     attribute_error_handler(e)
#     return False

example_function2.eset({
    ValueError: {
        "action": cli_print.error.title("Zadávání přerušeno uživatelem..."),
        "return": None,
        "raise": False
    },
    KeyboardInterrupt: {
        "raise": ValidationError("Zadaná hodnota musí bý celé číslo.")
    },
    AttributeError: {
        "action": attribute_error_handler(e)
        "return": False,
    },
    (OSError, PermissionError): {
        "property": {
            test_file: self._test_file
        },
        "action": (
            print("Po testu zůstal testovací soubor, který nelze smazat."),
            print(f"Cesta k souboru: {self._test_file}"),
            print(f"Zachycené podrobnosti: {e}"),
            print("Možné řešení: Zkontrolujte umístění a pokuste se soubor smazat ručně.")
        ),
        "return": False,
    },
})

from error_handler import catch_exc, set_message, raise_exc


@catch_exc(KeyboardInterrupt, OSError, PermissionError)
def example_function(x, y):
    return x / y


example_function.handle(
    (OSError, PermissionError),
    set_message("Kritická chyba validace"),
    raise_exc(ValidationError("Zadaná hodnota musí bý celé číslo."))
)

example_function.handle(
    OSError, PermissionError
).set_message(
    "Kritická chyba validace"
).set_raise(
    ValidationError("Zadaná hodnota musí bý celé číslo.")
)

example_function.handle(
    set_action(
        KeyboardInterrupt,
        ValidationError("Zadaná hodnota musí bý celé číslo."),
    ),
    set_message(
        KeyboardInterrupt,
        "Kritická chyba validace"
    )

)

example_function.eset({
    KeyboardInterrupt: {
        "raise": ValidationError("Zadaná hodnota musí bý celé číslo.")
    },
})



@exc_catch(KeyboardInterrupt, OSError, PermissionError)
def example_function(x, y):
    return x / y

@e_catch(KeyboardInterrupt, OSError, PermissionError)
def example_function(x, y):
    return x / y

@ecatch(KeyboardInterrupt, OSError, PermissionError)
def example_function(x, y):
    return x / y

@catch_exc(KeyboardInterrupt, OSError, PermissionError)
def example_function(x, y):
    return x / y

@catch_exc(KeyboardInterrupt, OSError, PermissionError)
def example_function(x, y):
    return x / y

example_function.handle_exc(
    KeyboardInterrupt,
    set_messagge("Zadaná hodnota musí bý celé číslo."),
    raise_exc(),
)

example_function.handle_exc(
    (OSError, PermissionError),
    set_action(cli_print.error.title("Zadávání přerušeno uživatelem...")),
    set_return(None)
)

@handle_exc(handle_exc_for_example_function)
@catch_exc(KeyboardInterrupt, OSError, PermissionError)
def example_function(x, y):
    return x / y

def handle_exc_for_example_function():
    if KeyboardInterrupt:
        cli_print.error.title("Zadávání přerušeno uživatelem...")
        return None
