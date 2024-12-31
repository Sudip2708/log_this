from pathlib import Path
from typing import Dict, Union

from .mixins import ConfigMixin

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

        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._config_dir = Path(__file__).parent
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

        if not hasattr(self, '_initialized'):
            self.config = self._load_default_config()
            self._initialized = True

