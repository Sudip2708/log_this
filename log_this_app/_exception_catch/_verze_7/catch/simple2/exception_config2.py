import logging
from typing import Dict, List, Optional, Type, Union, Callable, Any

from .config_mixins.log_exception import LogExceptionMixin


class ExceptionConfig:
    """Konfigurační třída pro správu chování dekorátoru exception_catch."""

    # Statická proměnná pro uchování globální instance
    _global_instance = None

    @classmethod
    def get_global_instance(cls) -> Optional['ExceptionConfig']:
        """Vrátí globální instanci, pokud existuje."""
        return cls._global_instance

    @classmethod
    def set_global_instance(cls, instance: 'ExceptionConfig') -> None:
        """Nastaví globální instanci konfigurace."""
        if cls._global_instance is not None:
            raise PermissionError(
                "Zachycen pokus o druhou definici globálního nastavení. "
                "Globální nastavení může být definované jen jednou."
            )
        cls._global_instance = instance

    def __init__(
            self,
            logger=None,
            log_to_file=False,
            log_file_path=None,
            log_level=logging.ERROR,
            log_format=None,
            exception_handlers=None,
            prefix=None,
            message=None,
            raise_exception=True,
            action=None
    ):
        """
        Inicializace konfigurační třídy.

        Args:
            logger: Vlastní logger pro použití (pokud není zadán, použije se root logger)
            log_to_file: Zda logovat do souboru
            log_file_path: Cesta k souboru pro logování
            log_level: Výchozí úroveň logování
            log_format: Vlastní formát logování
            exception_handlers: Slovník {exception_type: handler_config} pro specifické zpracování výjimek
        """
        self.logger = logger or logging.getLogger()
        self.log_to_file = log_to_file
        self.log_file_path = log_file_path
        self.log_level = log_level

        # Slovník pro specifické zpracování výjimek
        self.exception_handlers = exception_handlers or {}

        # Nastavení pro výstup
        self.log_format = log_format
        self.prefix = prefix
        self.message = message
        self.raise_exception = raise_exception
        self.action = action

        # Inicializace logování
        self._setup_logging()

    def _setup_logging(self):
        """Nastavení logování podle konfigurace."""
        # Základní nastavení
        handlers = []
        formatter = logging.Formatter(self.log_format)

        # Nastavení console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        handlers.append(console_handler)

        # Nastavení file handler, pokud je požadováno
        if self.log_to_file and self.log_file_path:
            file_handler = logging.FileHandler(self.log_file_path)
            file_handler.setFormatter(formatter)
            handlers.append(file_handler)

        # Nastavení loggeru
        if not self.logger.handlers:  # Přidáme handlery pouze pokud ještě žádné nemá
            for handler in handlers:
                self.logger.addHandler(handler)

        self.logger.setLevel(self.log_level)

    def add_exception_handler(
            self,
            exception_type: Type[Exception],
            log_level: int = None,
            message_prefix: str = None,
            custom_formatter: logging.Formatter = None,
            handle_func: Callable[[Exception, Any], None] = None
    ) -> None:
        """
        Přidá konfigurace pro zpracování konkrétního typu výjimky.

        Args:
            exception_type: Typ výjimky
            log_level: Úroveň logování pro tuto výjimku
            message_prefix: Prefix zprávy pro logování
            custom_formatter: Vlastní formatter pro tuto výjimku
            handle_func: Vlastní funkce pro zpracování výjimky
        """
        if not issubclass(exception_type, BaseException):
            raise TypeError(f"{exception_type} není platná výjimka")

        self.exception_handlers[exception_type] = {
            'log_level': log_level or self.log_level,
            'message_prefix': message_prefix or '',
            'custom_formatter': custom_formatter,
            'handle_func': handle_func
        }


    def get_exception_handler(self, exception):
        """Vrátí konfiguraci potřebnou pro vyřízení výjimky."""




