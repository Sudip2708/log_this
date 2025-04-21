from abc_helper import AbcSingletonMeta
import logging

from typing import Dict, List, Optional, Type, Union, Callable, Any, Set

from .handle_exception import HandleException

class ExceptionHandler(
    HandleException,
    metaclass=AbcSingletonMeta
):

    def __init__(
            self,
            exception: Type[Exception] = Exception
    ) -> None:

        # Kontrola singleton instance
        if not hasattr(self, "_initialized"):

            # Podědění logiky z rodiče
            super().__init__(exception)

            # Atribut pro globání nastavení pro jednotlivé výjimky
            self._exception_handlers = {}

            # Potvrzení o singleton inicializaci
            self._initialized = True

    def define_exc_handler(self,
             exception: Type[Exception],
             prefix: str = None,
             message: str = None,
             log_level: Union[int, str] = None,
             include_traceback: bool = None,
             blank_line: bool = None,
             raise_exception: bool = None,
             actions: List[Callable] = None):
        """Zkopíruje předanou konfiguraci a vrátí novou instanci s možností přepsání atributů."""

        def chose(first_option, second_option):
            """Vybere hodnotu"""
            return first_option if first_option is not None else second_option

        return HandleException(
            exception=exception,
            prefix=chose(prefix, self.prefix),
            message=chose(message, self.message),
            log_level=chose(log_level, self.log_level),
            include_traceback=chose(include_traceback, self.include_traceback),
            blank_line=chose(blank_line, self.blank_line),
            raise_exception=chose(raise_exception, self.raise_exception),
            actions=chose(actions, self.actions)
        )

    def set_exception_handler(self, *exc_handles: HandleException):
        """Přidá globální nastavení pro konkrétní výjimku do slovníku"""

        # Cyklus procházející jednotlivé položky
        for exc_handle in exc_handles:

            # Kontrola vstupní hodnoty
            if not isinstance(exc_handle, HandleException):
                raise TypeError("Nebyla předaná instance HandleException.")

            # Načtení klíče
            key = str(exc_handle)

            # Kontrola, zda slovník již obsahuje klíč
            if key in self._exception_handlers:
                raise ValueError(f"Přidávaný klíč {key} již ve slovníku existuje.")

            # Přidání klíče do slovníku
            self._exception_handlers[key] = exc_handle


    def exception_catch(self, *exceptions):
        """
        Dekorátor pro zachytávání specifikovaných výjimek a logování chyb.
        """

        # Validace výjimek
        for exc in exceptions:
            if not issubclass(exc, HandleException):
                raise TypeError(f"{exc} není instance HandleException.")

        # Definice dekorátoru
        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    self.handle_exception(e, func, *exceptions)
            return wrapper
        return decorator


    def handle_exception(self, e, func, *exceptions):
        """Vytvoří výstup pro danou výjimku"""
        pass


"""
from exception_handler import (
    global_handler,  # Přístup ke globálnímu nastavení
    define_exc_handler,  # Metoda pro kolii globáního nstavení a definici nového na jeho základě
    exc_catch,  # Dekorátor peo zachycení výjimek
)

# Změna v globáním nastavení (společné pro všechny zachycené výjimky)
global_handler.set_prefix("[Něco jiného]").set_message("Něco jiného")

# Nebo vše najednou
global_handler.set(prefix = "[Něco jiného]", message = "Něco jiného")

# Vytvoření vlastní saty pravidel
_ValueError = define_exc_handler(ValueError, message="Něco jiného")

# Alternativní zápis
_ValueError = define_exc_handler(ValueError).set_message("Něco jiného")
set_message(_ValueError, "[Něco jiného]")

# Lokální použití v rámci dekorátoru (přebíjí ostatní)
@exc_catch(_ValueError)
def funkce():

# Zápis sady do globálního nastavení
global_handler.set_exc_handlers(_ValueError)
"""

