import functools
from typing import Any, Callable, Optional, Union, Type

from abc_helper import ABC, abc_property


class CatchMixin(ABC):

    default_log_level = abc_property("default_log_level")
    logger = abc_property("logger")
    reraise = abc_property("reraise")
    fallback_return = abc_property("fallback_return")

    def catch(
            self,
            *exceptions: Type[Exception],
            log_level: Optional[int] = None,
            message: Optional[str] = None
    ):
        """
        Dekorátor pro zachytávání a zpracování výjimek.

        :param exceptions: Typy výjimek k zachycení
        :param log_level: Úroveň logování pro tento konkrétní případ
        :param message: Vlastní chybová zpráva
        """

        # Validace vstupních výjimek
        for exc in exceptions:
            if not isinstance(exc, type) or not issubclass(exc, BaseException):
                raise TypeError(f"{exc} není platná výjimka")

        # Definice dekorátoru
        def decorator(func: Callable):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    # Příprava kontextových informací
                    exc_type = type(e).__name__
                    exc_message = str(e)

                    # Volba úrovně logování
                    current_log_level = log_level or self.default_log_level

                    # Příprava zprávy
                    log_msg = message or (
                        f"Výjimka v metodě {func.__name__}: "
                        f"{exc_type} - {exc_message}"
                    )

                    # Rozhodnutí o logování
                    if not exceptions or any(
                            isinstance(e, exc) for exc in exceptions):
                        self.logger.log(
                            current_log_level,
                            log_msg,
                            exc_info=True
                        )

                        # Rozhodnutí o znovuvyvolání
                        if self.reraise:
                            raise

                        # Fallback návratová hodnota
                        return self.fallback_return

                    # Pokud výjimka nespadá do specifikovaných, znovu vyvolej
                    raise

            return wrapper

        return decorator


# # Ukázka custom exception handleru
# @exception_catch(KeyError)
# def example_function():
#     return {}['neexistující_klíč']