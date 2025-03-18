from abc import ABC

from cli_styler import styler
from abc_helper import abc_property


class ChangeValueMixin(ABC):

    config = abc_property("config")
    file_manager = abc_property("file_manager")
    items_manager = abc_property("items_manager")
    _history = abc_property("_history")


    def change_value(self, key, value, silent=False):
        """Změna konfigurace"""

        # Zálohování aktuálního nastavení
        self._history = self.config.copy()

        # Ověření hodnoty
        self.items_manager.value_validation(key, value)

        try:

            # Ověření, zda nebyla zadaná již platná hodnota
            if self.config[key] != value:

                # Nastavení hodnoty v konfiguračním slovníku
                self.config[key] = value

                # Výpis o změně
                key_class = self.items_manager.KEYS_DATA.get(key)
                value_str = key_class.VALUES_DICT.get(value, value)
                if not silent:
                    styler.cli_print.success.title(
                        f"Klíč '{key}' byl úspěšně nastaven na hodnotu '{value_str}'"
                    )

                # Zapsání změny do konfiguračního souboru:
                if self.file_manager:
                    self.file_manager.save_configuration(self.config)
                    if not silent:
                        styler.cli_print.success.text(
                            "Změna konfigurace úspěšně zaznamenána i do souboru."
                        )

            # Pokud se hodnoty schodují
            else:
                if not silent:
                    styler.cli_print.info.title("Byla zadaná již nastavená hodoty.")
                    styler.cli_print.info.text("Žádná změna nebyla učiněna.")

            # Vytisknutí prázdného řádku
            if not silent:
                styler.cli_print.empty_line()

        except Exception as e:
            raise RuntimeError(
                f"Neočekávaná chyba při ukládání JSON souboru: {e}"
            ) from e