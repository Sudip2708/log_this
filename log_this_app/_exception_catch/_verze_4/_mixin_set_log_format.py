from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .exception_handler import ExceptionHandler

from abc_helper import ABC


class SetLogFormatMixin(ABC):


    def set_log_format(
            self,
            format_string: str,
            exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        """
        Nastavení formátu logování pro specifickou výjimku.

        :param format_string: Formátovací řetězec pro logging
        :param exception_type: Typ výjimky (None pro globální nastavení)
        :return: Instance ExceptionHandleru pro řetězení volání
        """

        if exception_type:
            self._log_formats[exception_type] = format_string
        else:
            # Globální výchozí formát
            self._log_formats[Exception] = format_string

        return self

