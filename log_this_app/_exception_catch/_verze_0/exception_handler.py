import logging
from typing import Optional

from ._mixin_catch import CatchMixin


class ExceptionHandler(CatchMixin):
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




# Globální instance pro snadné použití
exception_handler = ExceptionHandler()
exception_catch = exception_handler.catch