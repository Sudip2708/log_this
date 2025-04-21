import logging
from typing import Optional, Dict, Any

from .verify import verify
from ._mixin_catch import CatchMixin
from ._mixin_handle import HandleMixin
from ._mixin_set_log_level import SetLogLevelMixin
from ._mixin_set_message import SetMessageMixin
from ._mixin_set_log_format import SetLogFormatMixin



class ExceptionHandler(
    CatchMixin,
    HandleMixin,
    SetLogLevelMixin,
    SetMessageMixin,
    SetLogFormatMixin
):
    """
    Třída pro zachycení a ošetření výjimek.

    Mixiny:
        CatchMixin: Dekorátor pro zachytávání a zpracování výjimek.
        HandleMixin: Registrace vlastního handleru pro specifickou výjimku.
        SetLogLevelMixin: Nastavení úrovně logování pro specifickou výjimku nebo globálně.
        SetMessageMixin: Nastavení vlastní chybové zprávy pro specifickou výjimku.
        SetLogFormatMixin: Nastavení formátu logování pro specifickou výjimku.
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

import functools
import logging
from typing import Any, Callable, Optional, Type, Union


class ExceptionHandler:
    def catch(
            self,
            *exceptions: Type[Exception],
            log_level: Optional[int] = None,
            message: Optional[str] = None
    ):
        """
        Dekorátor pro zachytávání a zpracování výjimek s rozšířenou konfigurací.

        :param exceptions: Typy výjimek k zachycení
        :param log_level: Volitelná úroveň logování
        :param message: Volitelná vlastní chybová zpráva
        """

        def decorator(func: Callable):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Priorita: Parametry dekorátoru > Globální nastavení > Výchozí hodnoty

                    # Výběr úrovně logování
                    current_log_level = (
                            log_level or
                            self._log_levels.get(type(e), None) or
                            self._default_log_level
                    )

                    # Výběr chybové zprávy
                    error_message = (
                            message or
                            self._custom_messages.get(type(e), None) or
                            self._custom_messages.get(Exception, None) or
                            f"Výjimka v metodě {func.__name__}: {type(e).__name__} - {str(e)}"
                    )

                    # Výběr formátu logování
                    log_format = (
                            self._log_formats.get(type(e), None) or
                            self._log_formats.get(Exception, None) or
                            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    )

                    # Nastavení formátování loggeru
                    formatter = logging.Formatter(log_format)
                    for handler in self.logger.handlers:
                        handler.setFormatter(formatter)

                    # Přidání kontextových informací
                    extra = {
                        'function': func.__name__,
                        **self._context_data
                    }

                    # Logování s vybranou úrovní a zvolenými parametry
                    self.logger.log(
                        current_log_level,
                        error_message,
                        exc_info=True,
                        extra=extra
                    )

                    # Rozhodnutí o výjimkách k zachycení
                    if not exceptions or any(
                            isinstance(e, exc) for exc in exceptions):
                        raise

            return wrapper

        return decorator


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