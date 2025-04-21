from typing import Any, Callable, Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .exception_handler import ExceptionHandler

from abc_helper import ABC, abc_property


class SetDefaultHandlerMixin(ABC):

    _default_handler = abc_property("_default_handler")


    def set_default_handler(
            self,
            handler: Optional[Callable[[Exception], Any]] = None
    ) -> 'ExceptionHandler':
        """
        Nastavení globálního fallback handleru pro nezachycené výjimky.

        :param handler: Callable handler pro zpracování výjimek
        :return: Instance ExceptionHandleru
        """

        self._default_handler = handler
        return self