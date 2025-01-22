from pathlib import Path
from typing import Dict, Union, Set

from .init_mixins import CreateConfigFileMixin, LoadConfigMixin
from .singleton_meta import SingletonMeta
from log_this.manager.logger import cli_log
from .keys_data import (
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

class LogThisConfig(
    LoadConfigMixin,
    CreateConfigFileMixin,
    metaclass=SingletonMeta
):
    """
    Singleton konfigurace pro knihovnu logování s rozšířenými funkcemi.

    Hlavní vlastnosti:
    - Jedinečná instance konfigurace v aplikaci
    - Automatické načítání a validace konfigurace z JSON souboru
    - Dynamická správa konfiguračních parametrů
    - Podpora exportu, importu a resetu konfigurace
    """


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
            self.keys_data = {
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
            self._create_config_file = False
            self.config = self.load_config()
            self.create_config_file()
            self._initialized = True


    @property
    def defaults(self) -> Dict[str, Union[int, str, bool]]:
        """Vrátí slovník s výchozími hodnotami konfigurace."""
        return {
            key: config_key.default_value
            for key, config_key in self.keys_data.items()
        }

    @property
    def valid_keys(self) -> Set[str]:
        """Vrátí množinu s platnými klíči."""
        return set(self.keys_data.keys())


config = LogThisConfig()