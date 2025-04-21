import logging
from typing import Optional, Dict, Any

from .verify import verify
from ._mixin_catch import CatchMixin
from ._mixin_handle import HandleMixin
from ._mixin_set_log_level import SetLogLevelMixin
from ._mixin_set_message import SetMessageMixin
from ._mixin_set_log_format import SetLogFormatMixin



class ExceptionHandler(
    CatchMixin,
    HandleMixin,
    SetLogLevelMixin,
    SetMessageMixin,
    SetLogFormatMixin
):
    """
    Třída pro zachycení a ošetření výjimek.

    Mixiny:
        CatchMixin: Dekorátor pro zachytávání a zpracování výjimek.
        HandleMixin: Registrace vlastního handleru pro specifickou výjimku.
        SetLogLevelMixin: Nastavení úrovně logování pro specifickou výjimku nebo globálně.
        SetMessageMixin: Nastavení vlastní chybové zprávy pro specifickou výjimku.
        SetLogFormatMixin: Nastavení formátu logování pro specifickou výjimku.
    """

    def __init__(
            self,
            logger: Optional[logging.Logger] = None,
            default_log_level: int = logging.ERROR
    ):
        self.logger = logger or logging.getLogger(__name__)
        self._default_log_level = default_log_level

        # Nové atributy pro ukládání nastavení
        self._log_formats: Dict[str, str] = {}
        self._custom_messages: Dict[type, str] = {}
        self._log_levels: Dict[type, int] = {}
        self._context_data: Dict[str, Any] = {}


    def add_context(
            self,
            key: str,
            value: Any
    ) -> 'ExceptionHandler':
        """
        Přidání kontextové informace pro logování.

        :param key: Klíč kontextové informace
        :param value: Hodnota kontextové informace
        :return: Instance ExceptionHandleru pro řetězení volání
        """
        self._context_data[key] = value
        return self




# Globální instance
exception_handler = ExceptionHandler()
verify = verify
exception_catch = exception_handler.catch


# # Ukázka použití
# def example_usage():
#     # Vytvoření handleru s vlastním nastavením
#     handler = ExceptionHandler() \
#         .set_log_level(logging.WARNING, ValueError) \
#         .set_message("Kritická chyba validace", ValueError) \
#         .set_log_format("%(asctime)s - CUSTOM - %(message)s", ValueError) \
#         .add_context("application", "MyApp")
#
#
# # Příklad použití v kódu
# try:
#     # Nějaká riziková operace
#     raise ValueError("Testovací výjimka")
# except ValueError as e:
#     # Zde by byl vlastní logging s přizpůsobeným nastavením
#     pass
