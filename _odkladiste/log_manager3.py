import logging
from typing import Optional, Dict
from log_this_old.manager.ansi_styler import cli_format
from pathlib import Path
import atexit


class LogManager:
    """Třída pro správu loggerů s podporou Singleton patternu."""
    _instance = None
    _loggers: Dict[str, logging.Logger] = {}

    # Konstanty pro formátování
    DEFAULT_FILE_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    DEFAULT_CONSOLE_FORMAT = '%(message)s'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Registrace cleanup metody při první inicializaci
            atexit.register(cls.cleanup)
        return cls._instance

    def __init__(self):
        # Init se zavolá při každém vytvoření instance,
        # ale díky __new__ máme jistotu, že cleanup registrujeme jen jednou
        pass

    @classmethod
    def _create_file_handler(
            cls,
            filename: str,
            formatter_str: str = DEFAULT_FILE_FORMAT,
            date_format: str = DEFAULT_DATE_FORMAT
    ) -> logging.FileHandler:
        """
        Vytvoří a nakonfiguruje handler pro logování do souboru.

        Args:
            filename: Cesta k logovacímu souboru
            formatter_str: Formát logovacích zpráv
            date_format: Formát data a času

        Returns:
            Nakonfigurovaný FileHandler
        """
        file_handler = logging.FileHandler(filename, encoding='utf-8')
        file_formatter = logging.Formatter(formatter_str, datefmt=date_format)
        file_handler.setFormatter(file_formatter)
        return file_handler

    @classmethod
    def get_logger(
            cls,
            name: str,
            level: int = logging.DEBUG,
            formatter: Optional[logging.Formatter] = None,
            log_to_file: bool = False,
            filename: Optional[str] = None
    ) -> logging.Logger:
        """
        Vrátí logger s daným názvem, nebo vytvoří nový, pokud neexistuje.

        Args:
            name: Název loggeru
            level: Úroveň logování (např. DEBUG, INFO)
            formatter: Vlastní formátování logů
            log_to_file: Zda logovat také do souboru
            filename: Cesta k souboru pro logování (pouze pokud log_to_file=True)

        Returns:
            Nakonfigurovaný logger
        """
        if name not in cls._loggers:
            logger = logging.getLogger(name)
            logger.propagate = False

            if not logger.handlers:
                # Console handler
                console_handler = logging.StreamHandler()
                console_formatter = formatter or logging.Formatter(
                    cls.DEFAULT_CONSOLE_FORMAT)
                console_handler.setFormatter(console_formatter)
                logger.addHandler(console_handler)

                # File handler (pokud je požadován)
                if log_to_file:
                    file_handler = cls._create_file_handler(
                        filename or f"{name.lower().replace('.', '_')}.log"
                    )
                    logger.addHandler(file_handler)

            logger.setLevel(level)
            cls._loggers[name] = logger

        return cls._loggers[name]

    # Předkonfigurované loggery
    APP_LOGGER_CONFIG = {
        'name': 'LogThis',
        'level': logging.DEBUG,
        'log_to_file': False
    }

    CLI_LOGGER_CONFIG = {
        'name': 'LogThis.CLI',
        'level': logging.WARNING,
        'formatter': logging.Formatter(
            cli_format('%(levelname)s', '%(message)s'))
    }

    @classmethod
    def app_logger(cls) -> logging.Logger:
        """Logger pro hlavní aplikační logy."""
        return cls.get_logger(**cls.APP_LOGGER_CONFIG)

    @classmethod
    def cli_logger(cls) -> logging.Logger:
        """Logger pro CLI komunikaci."""
        return cls.get_logger(**cls.CLI_LOGGER_CONFIG)

    @classmethod
    def cleanup(cls) -> None:
        """
        Vyčistí všechny handlery a zavře soubory.
        Vhodné volat při ukončení aplikace.
        """
        for logger in cls._loggers.values():
            for handler in logger.handlers[:]:
                if isinstance(handler, logging.FileHandler):
                    handler.close()
                logger.removeHandler(handler)
        cls._loggers.clear()