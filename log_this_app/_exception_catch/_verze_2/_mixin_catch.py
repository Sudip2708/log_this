import functools
from typing import Any, Callable, Optional, Union, Type

from abc_helper import ABC, abc_property


class CatchMixin(ABC):

    _exception_handlers = abc_property("_exception_handlers")
    logger = abc_property("logger")

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


# # Ukázka custom exception handleru
# @exception_catch(KeyError)
# def example_function():
#     return {}['neexistující_klíč']