from typing import Any, Callable, Type

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .exception_handler import ExceptionHandler

from abc_helper import ABC, abc_property


class RegisterGlobalHandlerMixin(ABC):


    def register_global_handler(
            self,
            handler: Callable[[Exception], Any],
            *exception_types: Type[Exception]
    ) -> 'ExceptionHandler':
        """
        Registrace globálního handleru pro specifické typy výjimek.

        :param handler: Callable handler pro zpracování výjimek
        :param exception_types: Typy výjimek k zachycení
        :return: Instance ExceptionHandleru
        """

        for exc_type in exception_types:
            self._global_handlers[exc_type] = handler

        return self