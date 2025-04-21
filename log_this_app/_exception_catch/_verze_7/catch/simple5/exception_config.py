import logging
from typing import Dict, List, Optional, Type, Union, Callable, Any, Set
from copy import deepcopy

from .exception_handler_settings import ExceptionHandlerSettings

class ExceptionConfig:
    """Konfigurační třída pro správu chování zpracování výjimek."""

    # Globální instance pro sdílené nastavení
    _global_instance = None

    def __init__(
            self,
            logger=None,
            log_level=logging.ERROR,
            log_file_path=None,
            log_format=None,
            prefix="[CATCH]",
            message="Chyba při vykonávání",
            include_traceback=C,
            blank_line=True,
            raise_exception=True,
            actions=None
    ):
        # Nastavení logování
        self.logger = logger or logging.getLogger()
        self.log_level = log_level
        self.log_file_path = log_file_path
        self.log_format = log_format

        # Nastavení formátu výstupu
        self.prefix = prefix
        self.message = message
        self.include_traceback = include_traceback
        self.blank_line = blank_line
        self.raise_exception = raise_exception
        self.actions = actions or []

        # Slovník pro specifická nastavení výjimek
        self.exception_handlers: Dict[
            Type[Exception], ExceptionHandlerSettings] = {}

        # Inicializace logování pokud je to potřeba
        if log_file_path:
            self._setup_logging()

    def _setup_logging(self):
        """Nastavení logování do souboru, pokud je to požadováno."""
        if self.log_file_path:
            file_handler = logging.FileHandler(self.log_file_path)
            if self.log_format:
                formatter = logging.Formatter(self.log_format)
                file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def copy(self):
        """Vytvoří kopii této konfigurace."""
        # Vytvoření mělké kopie
        new_config = ExceptionConfig(
            logger=self.logger,
            log_level=self.log_level,
            log_file_path=self.log_file_path,
            log_format=self.log_format,
            prefix=self.prefix,
            message=self.message,
            include_traceback=self.include_traceback,
            blank_line=self.blank_line,
            raise_exception=self.raise_exception,
            actions=self.actions.copy()
        )

        # Kopírování nastavení pro konkrétní výjimky
        for exc_type, settings in self.exception_handlers.items():
            new_config.exception_handlers[exc_type] = deepcopy(settings)

        return new_config

    def set_handler_for_exc(self, *exception_types):
        """
        Vytvoří nebo vrátí nastavení pro konkrétní typ výjimky.

        Args:
            *exception_types: Typy výjimek, pro které se má vytvořit nastavení

        Returns:
            ExceptionHandlerSettings pro první zadaný typ výjimky
        """
        result = None

        for exc_type in exception_types:
            if not issubclass(exc_type, BaseException):
                raise TypeError(f"{exc_type} není platná výjimka")

            # Pokud nastavení pro tento typ výjimky ještě neexistuje, vytvoř ho
            if exc_type not in self.exception_handlers:
                settings = ExceptionHandlerSettings(
                    exception_type=exc_type,
                    prefix=self.prefix,
                    message=self.message,
                    log_level=self.log_level,
                    include_traceback=self.include_traceback,
                    blank_line=self.blank_line,
                    raise_exception=self.raise_exception,
                    actions=self.actions.copy()
                )
                self.exception_handlers[exc_type] = settings

            # Pro první výjimku vrať nastavení
            if result is None:
                result = self.exception_handlers[exc_type]

        return result

    def get_settings_for_exception(self, exception):
        """
        Vrátí nastavení pro konkrétní výjimku.

        Args:
            exception: Instance výjimky nebo třída výjimky

        Returns:
            Tuple obsahující hodnoty pro zpracování výjimky
        """
        # Získej typ výjimky
        if isinstance(exception, type) and issubclass(exception, BaseException):
            exc_type = exception
        else:
            exc_type = exception.__class__

        # Pokud existuje specifické nastavení pro tento typ výjimky, použij ho
        handler_settings = self.exception_handlers.get(exc_type)

        if handler_settings:
            # Vytvoř slovník s hodnotami z nastavení pro konkrétní výjimku
            settings = {
                'prefix': handler_settings.prefix or self.prefix,
                'message': handler_settings.message or self.message,
                'log_level': handler_settings.log_level or self.log_level,
                'include_traceback': handler_settings.include_traceback if handler_settings.include_traceback is not None else self.include_traceback,
                'blank_line': handler_settings.blank_line if handler_settings.blank_line is not None else self.blank_line,
                'raise_exception': handler_settings.raise_exception if handler_settings.raise_exception is not None else self.raise_exception,
                'actions': handler_settings.actions
            }
        else:
            # Použij výchozí nastavení
            settings = {
                'prefix': self.prefix,
                'message': self.message,
                'log_level': self.log_level,
                'include_traceback': self.include_traceback,
                'blank_line': self.blank_line,
                'raise_exception': self.raise_exception,
                'actions': self.actions
            }

        return settings

    @classmethod
    def set_global_config(cls, config):
        """Nastaví globální konfiguraci pro všechny handlery."""
        if not isinstance(config, cls):
            raise TypeError(f"Konfigurace musí být instancí {cls.__name__}")
        cls._global_instance = config

    @classmethod
    def get_global_config(cls):
        """Získá globální konfiguraci, nebo vytvoří novou s výchozími hodnotami."""
        if cls._global_instance is None:
            cls._global_instance = cls()
        return cls._global_instance
