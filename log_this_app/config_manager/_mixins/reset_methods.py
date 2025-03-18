from abc import ABC

from cli_styler import styler
from abc_helper import abc_property


class ResetMethodsMixin(ABC):

    config = abc_property("config")
    file_manager = abc_property("file_manager")
    items_manager = abc_property("items_manager")
    _history = abc_property("_history")


    def reset_to_default_configuration(self, silent=False):

        # Zálohování aktuálního nastavení
        self._history = self.config.copy()

        # Změna konfigurace
        self.config = self.items_manager.default_values()
        if not silent:
            styler.cli_print.success.title(
                f"Konfigurace byla změněna na výchozí hodnoty"
            )

        # Zápis do souboru
        if self.file_manager:
            self.file_manager.save_configuration()
            if not silent:
                styler.cli_print.success.text(
                    "Změna konfigurace úspěšně zaznamenána i do souboru."
                )

        styler.cli_print.success.text(
            "Předchozí konfiguraci můžete vrátit přes reset na předchozí nastavení."
        )

        # Vytisknutí prázdného řádku
        if not silent:
            styler.cli_print.empty_line()

    def reset_to_previous_configuration(self, silent=False):

        # Ověření zda existuje předchozí uložené nastavení
        if self._history:

            # Změna configurace
            self._history, self.config = self.config, self._history
            if not silent:
                styler.cli_print.success.title(
                    f"Došlo k změně konfigurace na předchozí uloženou"
                )

            # Kontrola, zda je používán i konfigurační soubor:
            if self.file_manager:
                self.file_manager.save_configuration(self.config)
                styler.cli_print.success.text(
                    "Změna konfigurace úspěšně zaznamenána i do souboru."
                )

            styler.cli_print.success.text(
                "Předchozí nastavení můžete vrátit opakováním tohoto kroku."
            )

            # Vytisknutí prázdného řádku
            if not silent:
                styler.cli_print.empty_line()

        else:
            if not silent:
                styler.cli_print.info.title(
                    "Historie nemá uložené žádné nastavení"
                )
                styler.cli_print.info.text(
                    "Žádná změna nebyla učiněna."
                )

                # Vytisknutí prázdného řádku
                styler.cli_print.empty_line()
