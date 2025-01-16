from pathlib import Path
from typing import Dict, Union

from .config_mixin import ConfigMixin
from log_this.manager.logger import cli_log
from .config_keys import (
    SkipThisKey,
    OneLineKey,
    SimpleKey,
    DetailedKey,
    ReportKey,
    TrueKey,
    FalseKey,
    NoneKey,
    EmptyKey,
    IndentKey,
    BlankLinesKey,
    DocstringLinesKey,
    MaxDepthKey,
)

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

            """Inicializace správce konfigurace"""
            self._config_keys = {
                'skip_this': SkipThisKey(),
                'one_line': OneLineKey(),
                'simple': SimpleKey(),
                'detailed': DetailedKey(),
                'report': ReportKey(),
                'true': TrueKey(),
                'false': FalseKey(),
                'none': NoneKey(),
                'empty': EmptyKey(),
                'indent': IndentKey(),
                'blank_lines': BlankLinesKey(),
                'docstring_lines': DocstringLinesKey(),
                'max_depth': MaxDepthKey()
            }

            self.cli_log = cli_log
            self.config_path = Path(__file__).parent / "config.json"
            self.config = self._load_config_dict()
            self._initialized = True


    @property
    def defaults(self) -> Dict[str, Union[int, str, bool]]:
        """Vrátí slovník s výchozími hodnotami konfigurace."""
        return {
            key: config_key.default_value
            for key, config_key in self._config_keys.items()
        }

config = LogThisConfig()