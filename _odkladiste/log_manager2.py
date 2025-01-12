import logging
from typing import Optional, Dict
from log_this.manager.ansi_styler import cli_format

class LogManager:
    """Třída pro správu loggerů s podporou Singleton patternu."""

    _loggers: Dict[str, logging.Logger] = {}

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
                console_formatter = formatter or logging.Formatter('%(message)s')
                console_handler.setFormatter(console_formatter)
                logger.addHandler(console_handler)

                # File handler (pokud je požadován)
                if log_to_file:
                    file_handler = logging.FileHandler(
                        filename or f"{name.lower()}.log",
                        encoding='utf-8'
                    )
                    file_formatter = logging.Formatter(
                        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S'
                    )
                    file_handler.setFormatter(file_formatter)
                    logger.addHandler(file_handler)

            logger.setLevel(level)
            cls._loggers[name] = logger

        return cls._loggers[name]


    @classmethod
    def app_logger(cls) -> logging.Logger:
        """Logger pro hlavní aplikační logy."""
        return cls.get_logger('LogThis')

    @classmethod
    def cli_logger(cls) -> logging.Logger:
        """Logger pro CLI komunikaci."""
        return cls.get_logger(
            'LogThisConfig',
            level=logging.WARNING,
            formatter=logging.Formatter(
                cli_format('%(levelname)s', '%(message)s'))
        )


# Použití:
log_this_logger = LogManager.app_logger()
cli_logger = LogManager.cli_logger()
