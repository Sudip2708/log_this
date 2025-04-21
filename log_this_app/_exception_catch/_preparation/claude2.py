import functools
import logging
import inspect
from typing import Any, Callable, Optional, Union, Type


class VerifyError(Exception):
    """Vlastní výjimka pro selhání ověření."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class ExceptionHandler:
    def __init__(
            self,
            logger: Optional[logging.Logger] = None,
            default_log_level: int = logging.ERROR
    ):
        self.logger = logger or logging.getLogger(__name__)
        self.default_log_level = default_log_level
        self._exception_handlers = {}

    @staticmethod
    def verify(
            condition: bool,
            message: Optional[str] = None,
            exception_type: Type[Exception] = VerifyError
    ) -> bool:
        """
        Universální metoda pro ověřování podmínek.

        :param condition: Podmínka k ověření
        :param message: Volitelná vlastní chybová zpráva
        :param exception_type: Typ výjimky (defaultně VerifyError)
        :return: True pokud je podmínka splněna
        :raises: Specifikovaná výjimka pokud podmínka selhá
        """
        # Zjištění kontextu volání
        frame = inspect.currentframe().f_back
        caller_info = inspect.getframeinfo(frame)

        # Automatická tvorba zprávy pokud není poskytnuta
        if message is None:
            message = (
                f"Ověření selhalo v metodě {caller_info.function} "
                f"v souboru {caller_info.filename}:{caller_info.lineno}"
            )

        # Pokud podmínka nesplněna, vyvolej výjimku
        if not condition:
            raise exception_type(message)

        return True

    def handle(
            self,
            exception_type: Type[Exception],
            handler: Callable[[Exception], Any] = None,
            reraise: bool = True
    ):
        """
        Registrace vlastního handleru pro specifickou výjimku.

        :param exception_type: Typ výjimky k ošetření
        :param handler: Callable pro zpracování výjimky
        :param reraise: Zda znovu vyvolat výjimku po zpracování
        """
        self._exception_handlers[exception_type] = {
            'handler': handler,
            'reraise': reraise
        }
        return self

    def catch(
            self,
            *exceptions: Type[Exception],
            custom_handler: bool = False
    ):
        """
        Dekorátor pro zachytávání a zpracování výjimek.

        :param exceptions: Typy výjimek k zachycení
        :param custom_handler: Zda použít custom handler
        """

        def decorator(func: Callable):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Kontrola registrovaných handlerů
                    for exc_type, config in self._exception_handlers.items():
                        if isinstance(e, exc_type):
                            handler = config['handler']

                            # Volání custom handleru
                            if handler:
                                result = handler(e)

                                # Rozhodnutí o znovuvyvolání
                                if config['reraise']:
                                    raise
                                return result

                    # Standardní logování pro nezachycené výjimky
                    self.logger.error(
                        f"Výjimka v metodě {func.__name__}: {type(e).__name__} - {str(e)}",
                        exc_info=True
                    )
                    raise

            return wrapper

        return decorator


# Globální instance
exception_handler = ExceptionHandler()
verify = exception_handler.verify
exception_catch = exception_handler.catch


# Příklady použití
def example_usage():
    # Ukázka verify
    try:
        verify(isinstance("text", str), "Musí být řetězec")
        verify(5 > 3, "Neplatná matematická podmínka")
    except VerifyError as e:
        print(f"Ověření selhalo: {e}")

    # Ukázka custom exception handleru
    @exception_catch(KeyError)
    def example_function():
        exception_handler.handle(
            KeyError,
            handler=lambda e: print(f"Zachycen KeyError: {e}"),
            reraise=False
        )

        # Vyvolání KeyError
        return {}['neexistující_klíč']

    example_function()