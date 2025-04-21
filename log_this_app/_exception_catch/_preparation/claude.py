import functools
import logging
import traceback
from typing import Union, Type, Callable, Optional, Any
from xdrlib import raise_conversion_error


class ExceptionHandler:
    """Pokročilý nástroj pro komplexní zpracování výjimek."""

    def __init__(
            self,
            logger: Optional[logging.Logger] = None,
            default_log_level: int = logging.ERROR,
            reraise: bool = True,
            fallback_return: Any = None
    ):
        """
        Inicializace pokročilého exception handleru.

        :param logger: Vlastní logger (nebo None pro základní)
        :param default_log_level: Výchozí úroveň logování
        :param reraise: Zda znovu vyvolat výjimku po zalogování
        :param fallback_return: Hodnota vrácená při zachycení výjimky
        """
        self.logger = logger or logging.getLogger(__name__)
        self.default_log_level = default_log_level
        self.reraise = reraise
        self.fallback_return = fallback_return

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

    @classmethod
    def create_context_logger(
            cls,
            log_file: Optional[str] = None,
            log_level: int = logging.INFO
    ) -> logging.Logger:
        """
        Vytvoří konfigurovatelný logger s možností výstupu do souboru.

        :param log_file: Cesta k log souboru
        :param log_level: Úroveň logování
        :return: Nakonfigurovaný logger
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(log_level)

        # Formátování logu
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Konzolový handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Volitelný souborový handler
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger


# Globální instance pro snadné použití
exception_handler = ExceptionHandler()
exception_catch = exception_handler.catch

value = "text"
if not isinstance(value, str):
    raise VerifyError(f"Chyba ověření. Hodnota {value}, neodpovídá podmínce {zde by měla být nějak předaná podmínka}")

verify(isinstance(value, str))

@exception_catch(ValueError, KeyError*)
@exception_catch(ValueError, [KeyError])
@exception_catch(ValueError, eh.(KeyError))

exception_handler.handle(KeyError, my_key_error_handler())

@exception_catch(ValueError, KeyError)
def _some_function_or_method(self):

    # Definice co se má stát uvedená na začátku funkce, aby se načetla před jejím vykonáním
    exception_handler.handle(
        KeyError,
        print("some mesage"), raise()  # stop()
    )

    # Následuje funkce která když projde nic se neděje, když výjimka provede se předem stanovaná logika
    do_this if some_logik else do_something_else
