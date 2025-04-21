from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .exception_handler import ExceptionHandler

from abc_helper import ABC


class SetMessageMixin(ABC):

    def set_message(
            self,
            message: str,
            exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        """
        Nastavení vlastní chybové zprávy pro specifickou výjimku.

        :param message: Vlastní chybová zpráva
        :param exception_type: Typ výjimky (None pro globální nastavení)
        :return: Instance ExceptionHandleru pro řetězení volání
        """
        if exception_type:
            self._custom_messages[exception_type] = message
        else:
            # Globální výchozí zpráva
            self._custom_messages[Exception] = message
        return self
