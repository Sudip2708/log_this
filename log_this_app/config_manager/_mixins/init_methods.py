from abc import ABC

from cli_styler import styler
from abc_helper import abc_property

from .._file_manager import ConfigFileManager
from .._access_tester import path_access_tester


class InitMethodsMixin(ABC):

    CONFIG_FILE_PATH = abc_property("CONFIG_FILE_PATH")
    file_manager = abc_property("file_manager")
    items_manager = abc_property("items_manager")


    def _create_file_manager_or_none(self):
        """Vrátí instanci ConfigFileManager, pokud je možné zapisovat, jinak None."""
        if path_access_tester(self.CONFIG_FILE_PATH):
            return ConfigFileManager(self)
        else:
            styler.cli_print.warning.direction(
                "Aplikace je možné normálně používat bez omezení, "
                "pouze provedené změny se neuloží a při dalším zpuštění "
                "aplikace budou načteny defaultní hodnoty"
            )
            return None


    def _load_config(self):
        """Vrátí buď defaultní konfiguraci, nebo konfiguraci načtenou ze souboru."""
        return (
            self.file_manager.get_configuration()
            if self.file_manager
            else self.items_manager.default_values()
        )

