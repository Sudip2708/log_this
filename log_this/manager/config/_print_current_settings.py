from abc import ABC, abstractmethod
from typing import Dict, Union

from log_this.manager.config.keys import KEYS_DATA

class PrintCurrentSettingsMixin(ABC):
    """Mixin pro správu historie konfigurace pomocí snapshotů."""

    @abstractmethod
    @property
    def config(self) -> Dict[str, Union[int, str, bool]]:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    def print_current_settings(self):
        """
        Funkce pro navrácení aktuálních hodnot s popisem

        Ukázka výstupu:
        indent - 2 (Odsazení o 2 mezery) - Nastavení počtu mezer odsazení od kraje pro zanořené logování.
        """

        # Výsledný seznam řetězců
        outcome = ["Current settings:",]

        # Cyklus procházející klíče
        for key, key_data in KEYS_DATA.items():

            # Vytažení popisu klíče
            key_description = key_data.INFO

            # Vytažení aktuální hodnoty
            actual_value = self.config.get(key, "Klíč v konfiguraci nebyl nalezen")

            # Kontrolní validace hodnoty
            is_valid_value = key_data.validate(actual_value)

            # Doplnění popisu hodnoty
            value_description = key_data.DEFAULT_VALUE.get(
                actual_value,
                "manually entered value"
            ) if is_valid_value else "Hodnota není validní hodnotou"

            # Vytvoření výstupního řádku pro daný klíč
            outcome.append(
                f"{key} - {actual_value} ({value_description}) - {key_description}"
            )

        # Vypsání celého seznamu
        print(*outcome, sep='\n')


