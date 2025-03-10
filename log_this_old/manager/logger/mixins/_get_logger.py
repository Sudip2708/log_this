import logging
from typing import Optional

class GetLoggerMixin:

    # Konstanty pro formátování
    DEFAULT_CONSOLE_FORMAT = '%(message)s'

    @classmethod
    def get_logger(
            cls,
            name: str,
            level: int = logging.DEBUG,
            formatter: Optional[logging.Formatter] = None,
            propagate: bool = False,
            log_to_file: bool = False,
            filename: Optional[str] = None,
    ) -> logging.Logger:
        """
        Vrátí logger s daným názvem, nebo vytvoří nový, pokud neexistuje.

        Args:
            name: Název loggeru
            level: Úroveň logování (např. DEBUG, INFO)
            formatter: Vlastní formátování logů
            propagate: Nastavení propisování logů
            log_to_file: Zda logovat také do souboru
            filename: Cesta k souboru pro logování (pouze pokud log_to_file=True)

        Returns:
            Nakonfigurovaný logger
        """

        if name not in cls._loggers:
            logger = logging.getLogger(name)
            logger.propagate = propagate

            # Odstraň všechny existující handlery (pro případ, že logger už nějaké má)
            logger.handlers = []

            # File handler (pokud je požadován)
            if log_to_file:
                if filename is None:
                    filename = f"{name.replace('.', '_')}.log"
                file_handler = cls._create_file_handler(filename)
                logger.addHandler(file_handler)
            else:
                # Console handler (pouze pokud není logování do souboru)
                console_handler = logging.StreamHandler()
                console_formatter = formatter or logging.Formatter(
                    cls.DEFAULT_CONSOLE_FORMAT)
                console_handler.setFormatter(console_formatter)
                logger.addHandler(console_handler)

            logger.setLevel(level)
            cls._loggers[name] = logger

        return cls._loggers[name]
