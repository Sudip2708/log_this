from pathlib import Path
from typing import Dict, Union, Set

from .init_mixins import CreateConfigFileMixin, LoadConfigMixin
from .singleton_meta import SingletonMeta
from .utils import cli_print
from .keys_data import KEYS_DATA

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
            self.keys_data = KEYS_DATA
            self.cli_print = cli_print
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

    @property
    def get_valid_keys_with_descriptions(self) -> str:
        """Vrátí výpis klíčů s krátkým popisem."""
        text = (
            f"\nSeznam konfiguračních klíčů:\n"
        )
        for key in self.keys_data:
            text += f"'  {key}' - {self.keys_data[key].info}\n"
        return text


config = LogThisConfig()