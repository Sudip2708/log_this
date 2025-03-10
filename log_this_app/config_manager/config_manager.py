from pathlib import Path

from abc_helper import AbcSingletonMeta  # type: ignore
from cli_styler import styler  # type: ignore

from ._config_items_settings import ConfigItemsRegistry
from ._access_tester import AccessTester



from ._mixins import (
    InitMethodsMixin,
    ResetMethodsMixin,
    ImportExportMethodsMixin,
    ChangeValueMixin,
    PrintActualConfigurationMixin
)

class ConfigManager(

    InitMethodsMixin,
    # Přidává metody: _create_file_manager(), _load_config()
    # Používá atributy: CONFIG_FILE_PATH, _file_manager, items_manager

    ResetMethodsMixin,
    # Přidává metody: reset_to_default_configuration(), reset_to_previous_configuration()
    # Používá atributy: config, _file_manager, items_manager, _history

    ImportExportMethodsMixin,
    # Přidává metody: export_current_configuration(path), import_configuration(path)
    # Používá atributy: config, _file_manager, _access_tester

    ChangeValueMixin,
    # Přidává metody: change_value(key, value)
    # Používá atributy: config, _file_manager, items_manager, _history

    PrintActualConfigurationMixin,
    # Přidává metody: print_actual_configuration()
    # Používá atributy: config, items_manager

    metaclass=AbcSingletonMeta
):
    """Singleton správce konfigurace knihovny"""

    # Definice adresy konfiguračního souboru
    CONFIG_FILE_PATH = Path(__file__).parent / "config.json"

    # Definica tributu pro ukládání konfigurace před změnou
    _history = None

    # Připojení instance pro testování cesty
    _access_tester = AccessTester()

    _file_manager = None
    items_manager = None
    config = None

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

            # Napojení třídy starající definici jednotlivých položek konfigurace
            self.items_manager = ConfigItemsRegistry(self)

            # Napojení třídy starající se o správu konfiguračního souboru
            self._file_manager = self._create_file_manager()

            # Načtení konfigurace
            self.config = self._load_config()

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













