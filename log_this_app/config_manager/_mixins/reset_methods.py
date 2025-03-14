from abc import ABC

from cli_styler import styler
from abc_helper import abc_property


class ResetMethodsMixin(ABC):

    config = abc_property("config")
    file_manager = abc_property("file_manager")
    items_manager = abc_property("items_manager")
    _history = abc_property("_history")


    def reset_to_default_configuration(self):
        self.config = self.items_manager.default_values()
        if self.file_manager:
            self.file_manager.save_configuration()

    def reset_to_previous_configuration(self):

        # Ověření zda existuje předchozí uložené nastavení
        if self._history:
            self._history, self.config = self.config, self._history
            print("Došlo k změně konfigurace na předchozí. Nastavení před změnou je nyní k dispozici jako předešlé.")

            # Kontrola, zda je používán i konfigurační soubor:
            if self.file_manager:
                self.file_manager.save_configuration(self.config)
                print("Změna konfigurace úspěšně zaznamenána i do souboru.")

        else:
            print("Historie nemá uložené žádné nastavení")