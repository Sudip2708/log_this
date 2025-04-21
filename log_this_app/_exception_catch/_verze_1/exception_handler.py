import logging
from typing import Optional

from .verify import verify
from ._mixin_catch import CatchMixin
from ._mixin_handle import HandleMixin



class ExceptionHandler(CatchMixin, HandleMixin):
    """
    Třída pro zachycení a ošetření výjimek.

    Mixiny:
        CatchMixin: Dekorátor pro zachytávání a zpracování výjimek.
        HandleMixin: Registrace vlastního handleru pro specifickou výjimku.
    """

    def __init__(
            self,
            logger: Optional[logging.Logger] = None,
            default_log_level: int = logging.ERROR
    ):
        self.logger = logger or logging.getLogger(__name__)
        self.default_log_level = default_log_level
        self._exception_handlers = {}


# Globální instance
exception_handler = ExceptionHandler()
verify = verify
exception_catch = exception_handler.catch


