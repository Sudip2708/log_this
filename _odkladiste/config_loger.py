import logging
from .ansi_styler import cli_format


class ConfigLogManager:
    """Třída pro správu logování s použitím Rich pro barevné výstupy"""

    # Atribut pro singleton instanci třídy:
    _instance = None

    # Vytvoření instance:
    def __new__(cls) -> 'ConfigLogManager':
        """
        Vytvoření singleton instance.

        Metoda nejprve ověří existenci instance.
        Pokud existuje vrátí existující.
        Pokud neexistuje, vytvoří novou.

        Returns:
            LogThisConfig: Singleton instance konfigurace
        """

        # Pokud instance ještě není vytvořená
        if not cls._instance:
            # Vytvoření a navrácení singleton instance
            cls._instance = super().__new__(cls)
        return cls._instance

    # Základní inicializace instance
    def __init__(self) -> None:

        # Pokud instance nebvyla ještě inicializovaná
        if not hasattr(self, '_initialized'):

            # Vytvoření loggeru
            self.logger = logging.getLogger('LogThisConfig')

            # Zamezení aby se nastavení přepisovalo do root loggeru
            self.logger.propagate = False

            # Vytvoření handleru pro výstup na konzoli
            console_handler = logging.StreamHandler()

            # Nastavení formátování logů (formát bez času, úroveň a zpráva)
            # INFO: This is a log message.
            formatter = logging.Formatter(
                cli_format('%(levelname)s', '%(levelname)s')
            )

            # Přidání formátování logů do handleru
            console_handler.setFormatter(formatter)

            # Přidání handleru do loggeru
            self.logger.addHandler(console_handler)

            # Nastavení logování od minimální úrovně
            self.logger.setLevel(logging.DEBUG)

            # Záznam o inicializaci
            self._initialized = True


    def get_logger(self):
        """Vrátí loger pro aplikaci"""
        return self.logger


logger =ConfigLogManager().get_logger()