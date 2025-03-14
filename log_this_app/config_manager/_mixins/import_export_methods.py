from abc import ABC
from pathlib import Path


from cli_styler import styler
from abc_helper import abc_property

from .._file_manager import ConfigFileManager


class ImportExportMethodsMixin(ABC):

    config = abc_property("config")
    file_manager = abc_property("file_manager")
    _access_tester = abc_property("_access_tester")


    def export_current_configuration(self, path: Path):
        """Metoda uloží aktuální konfiguraci do souboru"""
        try:

            # Ověření cesty
            if self._access_tester(path):

                # Načtení managera
                file_manager = self.file_manager or ConfigFileManager(self)

                # Uložení konfigurace
                file_manager.save_configuration(self.config, path)

            else:
                print(f"Zapisování do souboru není možné: {e}")

        except Exception as e:
            raise RuntimeError(
                f"Neočekávaná chyba při ukládání JSON souboru: {e}"
            ) from e

    def import_configuration(self, path: Path):
        """Metoda načte konfiguraci ze souboru"""
        try:

            # Načtení managera
            file_manager = self.file_manager or ConfigFileManager(self)

            # Uložení konfigurace
            file_manager.get_configuration(path)

        except Exception as e:
            raise RuntimeError(
                f"Neočekávaná chyba při ukládání JSON souboru: {e}"
            ) from e