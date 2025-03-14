from abc import ABC

from cli_styler import styler
from abc_helper import abc_property


class ChangeValueMixin(ABC):

    config = abc_property("config")
    file_manager = abc_property("file_manager")
    items_manager = abc_property("items_manager")
    _history = abc_property("_history")


    def change_value(self, key, value):
        """Změna konfigurace"""

        # Zálohování aktuálního nastavení
        config_backup = self.config

        # Ověření hodnoty
        self.items_manager.value_validation(key, value)

        try:

            # Ověření, zda nebyla zadaná již platná hodnota
            if self.config[key] != value:
                self.config[key] = value
                print(f"Klíč {key} byl úspěšně nastaven na hodnotu {value}")

            # Pokud se hodnoty schodují
            else:
                print("Byla zadaná již nastavená hodoty. Žádná změna nebyla učiněna.")

            # Kontrola, zda je používán i konfigurační soubor:
            if self.file_manager:
                self.file_manager.save_configuration(self.config)
                print("Změna konfigurace úspěšně zaznamenána i do souboru.")

            # Uložení změny do hystorie
            self._history = config_backup


        except Exception as e:
            raise RuntimeError(
                f"Neočekávaná chyba při ukládání JSON souboru: {e}"
            ) from e