from abc import ABC, abstractmethod
from typing import Union, Set, Dict

from .keys import default_values, validate_config_dictionary
from .cli.styler import cli_print

class ResetToDefaultMixin(ABC):

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
    def save_to_config_file(self):
        """Metoda pro uložení aktuální konfigurace do konfiguračního souboru (je-li používán)"""
        pass


    def reset_to_default_settings(self):
        """Metoda vrátí nastavení na defaultní hodnoty"""

        # Načtení defaultních hodnot
        default_config = default_values()

        # Kontrola zda jde o slovník
        if not isinstance(default_config, dict):
            cli_print(
                style="error",
                info="Chyba při načítání defaultních hodnot! Konfigurace nebyla změněna."
            )
            return

        # Pokud je konfigurace již v defaultním stavu, neprovádíme zbytečné změny
        if self.config == default_config:
            cli_print(
                style="info",
                info="Konfigurace je již nastavena na defaultní hodnoty, žádná změna nebyla provedena."
            )
            return

        # Kontrola zda slovník obsahuje validní hodnoty
        if validate_config_dictionary(default_config) is False:
            cli_print(
                style="error",
                info="Data v defaultních hodnotá neprošli validací.",
                hint=(
                    "To je pravděpodobně zapříčiněno, že došlo k ruční změně defaultních hodnot.",
                    "Zkontrolujte kod pro třídy s daty pro klíče."
                )
            )
            return

        # Přepsání slovníku
        self.config = default_values()
        cli_print(
            style="success",
            info=f"Úspěšné přepsání celé konfigurace na defaultní hodnoty"
        )

        # Uložení změn do konfiguračního souboru (je-li používán)
        self.save_to_config_file()