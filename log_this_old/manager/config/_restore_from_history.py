from abc import ABC, abstractmethod
from typing import Dict, Union
from collections import deque

from .cli.styler import cli_print
from .keys import validate_config_dictionary

class RestoreFromHistoryMixin(ABC):
    """Mixin pro správu historie konfigurace pomocí snapshotů."""

    @abstractmethod
    @property
    def config(self) -> Dict[str, Union[int, str, bool]]:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    @abstractmethod
    @config.setter
    def config(self, config_dict: Dict[str, Union[int, str, bool]]) -> None:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    @abstractmethod
    @property
    def _history(self) -> deque[Dict[str, Union[int, str, bool]]]:
        """Atribut se seznamem historických snapshotů."""
        pass

    @abstractmethod
    def save_to_config_file(self):
        """Metoda pro uložení aktuální konfigurace do konfiguračního souboru (je-li používán)"""
        pass


    def restore_last_set_from_history(self):
        """Obnoví poslední uložený snapshot, pokud existuje."""

        # Kontrola zda historie obsahuje nějaký záznam
        if not self._history:

            # Oznámení prázdné historie
            no_history_cli_warning()

            # Ukončení procesu
            return

        # Načtení slovníku pro obnovu
        previous_config = self._history.pop()

        # Kontrola zda slovník obsahuje validní hodnoty
        if validate_config_dictionary(previous_config) is False:

            # Oznámení o nevalidních datech
            not_valid_config_dict_cli_warning()

            # Vymazání celé historie
            self._history.clear()

            # Ukončení procesu
            return

        # Přepsání konfigurace a oznam o změně
        self.config = previous_config

        # Výpis o úspěšném úkonu
        restore_previous_settings_sli_success()

        # Uložení změn do konfiguračního souboru (je-li používán)
        self.save_to_config_file()


def no_history_cli_warning():
    """Výpis do konzole pro případ, že je historie změn prázdná"""
    cli_print(
        style="warning",
        info=f"Žádný předchozí snapshot historie neexistuje.",
        detail=(
            "Došli jste nakonec ukládané historie změn.",
            "Historie změn ukládá pouze posledních 10 stavů."
        ),
        hint=(
            "Pokud si přejete pokračovat ve změně, využijte interaktivní režim: ",
            "log-this-config interactive"
        ),
        conclusion="Žádná změna nebyla učiněna."
    )

def not_valid_config_dict_cli_warning():
    cli_print(
        style="error",
        info=f"Předchozí uložená konfigurace neprošla validací.",
        detail=(
            "Toto může být způsobené nekonzistností dat a nebo poškozením souboru.",
            "Předchozí uloženou konfigurace nelze načíst."
        ),
        hint=(
            "Pokud si přejete pokračovat ve změně, můžete nahrát defaultní nastavení: ",
            "log-this-config reset-default",
            "Případně pro další změny můžete využít interaktivní režim: ",
            "log-this-config interactive"
        ),
        conclusion="Žádná změna nebyla učiněna."
    )

def restore_previous_settings_sli_success():
    cli_print(
        style="success",
        info=f"Konfigurace byla obnovena na předchozí stav.",
        hint=(
            "Pokud si přejete zobrazit aktuální nastavení použijte příkaz:",
            "log-this-config show-current",
            "Případně pro další změny můžete využít interaktivní režim: ",
            "log-this-config interactive"
        )
    )