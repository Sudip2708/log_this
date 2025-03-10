import logging
from log_this_old.manager.ansi_styler import cli_format


class LogManager:
    """Třída pro správu loggerů s podporou Singleton patternu."""

    # Statický atribut pro ukládání existujících loggerů
    _loggers = {}

    @classmethod
    def get_logger(cls, name: str, level=logging.DEBUG, formatter=None) -> logging.Logger:
        """
        Vrátí logger s daným názvem, nebo vytvoří nový, pokud neexistuje.

        Args:
            name (str): Název loggeru.
            level (int): Úroveň logování (např. DEBUG, INFO).
            formatter (logging.Formatter, optional): Vlastní formátování logů. Pokud není zadáno,
                                                     použije se výchozí formát.

        Returns:
            logging.Logger: Nakonfigurovaný logger.
        """
        if name not in cls._loggers:
            # Vytvoření nového loggeru
            logger = logging.getLogger(name)
            logger.propagate = False

            # Kontrola, zda má logger již handler
            if not logger.handlers:
                # Vytvoření handleru pro výstup na konzoli
                console_handler = logging.StreamHandler()

                # Použití vlastního nebo výchozího formátu
                if not formatter:
                    formatter = logging.Formatter('%(message)s')

                console_handler.setFormatter(formatter)
                logger.addHandler(console_handler)

            # Nastavení úrovně logování
            logger.setLevel(level)

            # Uložení loggeru do mapy
            cls._loggers[name] = logger

        return cls._loggers[name]


# Definice logerrů
log_this_logger = LogManager.get_logger('LogThis')
cli_config_logger = LogManager.get_logger(
    'LogThisConfig',
    formatter=logging.Formatter(cli_format('%(levelname)s', '%(levelname)s'))
)
