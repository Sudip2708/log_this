from abc import ABC, abstractmethod
from typing import Union, Set, Dict

from .cli.styler import cli_print
from .zzz import validate_key_and_value, check_if_value_already_set


class SetNewValueMixin(ABC):

    @abstractmethod
    @property
    def config(self) -> dict:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    @abstractmethod
    def save_settings_to_history(self):
        """Metoda pro uložení předchozí konfigurace do historie"""
        pass

    @abstractmethod
    def save_to_config_file(self):
        """Metoda pro uložení aktuální konfigurace do konfiguračního souboru (je-li používán)"""
        pass

    def set_new_value(
            self,
            key: str,
            value: Union[int, str, bool],
            value_check: bool = False
    ) -> None:

        # Kontrola zda ještě není provedena validace
        if not value_check:
            validate_key_and_value(key, value)

        # Kontrola, zda nebyla zadaná již existující hodnota
        if check_if_value_already_set(key, value, self.config[key]):
            return

        # Uložení předešlé verze do historie
        self.save_settings_to_history()

        # Uložení změny do konfiguračního slovníku
        self.config[key] = value
        cli_print(
            style="success",
            info=f"Úspěšné nastavení klíče '{key}' na hodnotu: {value}"
        )

        # Uložení změn do konfiguračního souboru (je-li používán)
        self.save_to_config_file()




