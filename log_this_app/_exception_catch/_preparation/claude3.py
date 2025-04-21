import logging
from typing import Optional, Union, Dict, Any


class ExceptionHandler:
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
        if exception_type:
            self._log_levels[exception_type] = level
        else:
            self._default_log_level = level
        return self

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


# Ukázka použití
def example_usage():
    # Vytvoření handleru s vlastním nastavením
    handler = ExceptionHandler() \
        .set_log_level(logging.WARNING, ValueError) \
        .set_message("Kritická chyba validace", ValueError) \
        .set_log_format("%(asctime)s - CUSTOM - %(message)s", ValueError) \
        .add_context("application", "MyApp")


# Příklad použití v kódu
try:
    # Nějaká riziková operace
    raise ValueError("Testovací výjimka")
except ValueError as e:
    # Zde by byl vlastní logging s přizpůsobeným nastavením
    pass