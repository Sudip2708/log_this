from pathlib import Path
from typing import Dict, Union

from .mixins import ConfigMixin
from ._config_log_manager import ConfigLogManager

class LogThisConfig(ConfigMixin):
    """
    Singleton konfigurace pro knihovnu logování s rozšířenými funkcemi.

    Hlavní vlastnosti:
    - Jedinečná instance konfigurace v aplikaci
    - Automatické načítání a validace konfigurace z JSON souboru
    - Dynamická správa konfiguračních parametrů
    - Podpora exportu, importu a resetu konfigurace
    """


    # Atribut pro singleton instanci třídy:
    _instance = None

    # Atribut pro cstu ke konfiguračnímu souboru
    _config_path = Path(__file__).parent / "config.json"

    # Inicializace loggeru na úrovni třídy
    logger = ConfigLogManager().get_logger()

    # Defaultní hodnoty:
    DEFAULTS: Dict[str, Union[int, str, bool]] = {
        'skip_this': 0,
        'one_line': 1,
        'simple': 2,
        'detailed': 3,
        'report': 4,
        'true': 1,
        'false': 0,
        'none': 0,
        'empty': 0,
        'indent': 2,
        'blank_lines': True,
        'docstring_lines': 3,
        'max_depth': 100,
    }


    # Vytvoření instance:
    def __new__(cls) -> 'LogThisConfig':
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

            # Validace dat z defaultního slovníků hodnot
            if not cls._validate_config_dict(cls.DEFAULTS):
                raise ValueError("Chyba při validaci defaultních hodnot.")

            # Vytvoření a navrácení singleton instance
            cls._instance = super().__new__(cls)
        return cls._instance


    # Základní inicializace instance
    def __init__(self) -> None:
        """
        Inicializace instance třídy.

        Metoda nejprve ověří, zda není instance již inicializovaná.
        Pokud ne, vytvoří atribut s cestou k tomuto soubou.
        Následně vytvoří atribut pro konfigurační slovník,
        na který je spuštěn proces pro načtení konfigurece ze souboru.
        Metoda následně nastaví atribut potvrzující proběhlou inicializaci.
        """

        # Pokud instance nebvyla ještě inicializovaná
        if not hasattr(self, '_initialized'):
            self.config = self._load_config_dict()
            self._initialized = True

