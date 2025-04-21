import functools
import logging
from typing import Any, Callable, Optional, Union, Type

from abc_helper import ABC, abc_property


class CatchMixin(ABC):

    logger = abc_property("logger")

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



# # Ukázka custom exception handleru
# @exception_catch(KeyError)
# def example_function():
#     return {}['neexistující_klíč']