from pathlib import Path
from typing import Dict, Union
from collections import deque

from ._singleton_meta import SingletonMeta
from ._load_config import LoadConfigMixin
from ._set_new_value import SetNewValueMixin
from ._save_to_config_file import SaveToConfigFileMixin
from ._save_to_history import SaveToHistoryMixin
from ._restore_from_history import RestoreFromHistoryMixin
from ._reset_to_defaults import ResetToDefaultMixin
from ._import_config_from_file import ImportConfigFromFileMixin
from ._export_config_to_file import ExportConfigToFileMixin
from ._print_current_settings import PrintCurrentSettingsMixin

from .access_tester import system_access_tester
from .keys import default_values


class LogThisConfig(
    LoadConfigMixin,
    SaveToConfigFileMixin,
    SaveToHistoryMixin,
    RestoreFromHistoryMixin,
    ResetToDefaultMixin,
    SetNewValueMixin,
    ImportConfigFromFileMixin,
    ExportConfigToFileMixin,
    PrintCurrentSettingsMixin,
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

    HISTORY_SNAPSHOT_LIMIT = 10  # Počet uchovaných verzí

    # Definice základních atributů
    config_file: bool = True
    config_file_path: Path = None
    default_values: Dict[str, Union[int, str, bool]] = {}
    config: Dict[str, Union[int, str, bool]] = {}
    _history: deque[Dict[str, Union[int, str, bool]]] = deque()

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

            # Vytvoření adresy pro případný konfigurační soubor
            self.config_file_path = Path(__file__).parent / "config.json"

            # Vytvoření hodnoty pro atribut signalizující zda je k dispozici ukládání na toto umístění
            self.config_file = system_access_tester(self.config_file_path)

            # Vytvoření atributu pro defaultní hodnoty
            self.default_values = default_values()

            # Načtení konfigurace
            self.config = self.load_config()

            # Vytvoření atributu pro zachycení změn nastavení
            self._history = deque(maxlen=self.HISTORY_SNAPSHOT_LIMIT)

            # Nastavení oznamu o provedené inicializaci
            self._initialized = True

    def __call__(self):
        """Vrátí konfigurační slovník při volání instance"""
        return self.config

    def __getitem__(self, key):
        """Umožní přístup pomocí config[key]"""
        return self.config[key]

    def get(self, key, default=None):
        """Umožní použití metody get() jako u slovníku"""
        return self.config.get(key, default)


config = LogThisConfig()
set_new_value = config.set_new_value
reset_previous = config.restore_last_set_from_history
reset_default = config.reset_to_default_settings
import_config_from_file = config.import_config_from_file
export_config_to_file = config.export_config_to_file
print_current_settings = config.print_current_settings