from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .exception_handler import ExceptionHandler

from abc_helper import ABC, abc_property

from .verify_safe import safe_verify


class SetLogLevelMixin(ABC):

    _log_levels = abc_property("_log_levels")
    _default_log_level = abc_property("_default_log_level")

    def set_log_level(
            self,
            level: int,
            exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        """
        Nastavení úrovně logování pro specifickou výjimku nebo globálně.

        :param level: Úroveň logování (logging.DEBUG, logging.INFO, atd.)
        :param exception_type: Typ výjimky (None pro globální nastavení)
        :return: Instance ExceptionHandleru pro řetězení volání
        """

        # Ověření levelu na int
        safe_verify(
            lambda: isinstance(level, int),
            "Úroveň logování musí být celočíselná hodnota"
        )

        # Ověření výjimky dle typu (je-li)
        if exception_type:
            safe_verify(
                lambda: isinstance(exception_type, type),
                "Typ výjimky musí být platný typ"
            )

        # Logika pro nastavení úrovně logování
        if exception_type:
            self._log_levels[exception_type] = level
        else:
            self._default_log_level = level

        return self
