from typing import Any, Callable, Type

from abc_helper import ABC, abc_property


class HandleMixin(ABC):

    _exception_handlers = abc_property("_exception_handlers")

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


# # Ukázka custom exception handleru
# @exception_catch(KeyError)
# def example_function():
#     exception_handler.handle(
#         KeyError,
#         handler=lambda e: print(f"Zachycen KeyError: {e}"),
#         reraise=False
#     )
#
#     # Vyvolání KeyError
#     return {}['neexistující_klíč']