import os
import json
import logging
from typing import Dict, Union, Any


class InstanceMethodMixin:


    def update_config(self, key: str, value: Union[int, str, bool]) -> None:
        """
        Aktualizuje hodnotu konfigurace a uloží ji.

        Metoda nejprve zkontroluje přítomnos klíče v defaultním slovníku,
        a ověří platnost hodnoty.
        Následně metoda změní hodnotu pro daný klíč v instanční konfiguraci.
        Nakonec metoda uloží hodnoty do konfiguračního souboru.
        Pokud se to nepovede, metoda načte zpět původní hodnoty.

        Args:
            key (str): Klíč konfigurace pro aktualizaci
            value (Union[int, str, bool]): Nová hodnota konfigurace

        Raises:
            KeyError: Při pokusu o aktualizaci neexistujícího klíče
            ValueError: Při pokusu o nastavení neplatné hodnoty
        """

        # Kontrola klíče a hodnoty
        self._key_and_value_check(key, value)

        # Uložení změny do instance třídy
        self.config[key] = value

        # Uložení změny do konfiguračního souboru
        path = self._get_config_file_path()
        if not self._save_config_to_file(path, self.config):
            self._load_default_config()

        logging.info(f"Úprava konfigurace pro klíč {key} na hodnotu {value}.")



    def update_configs(self, updates: Dict[
        str, Union[int, str, bool]]) -> None:
        """
        Aktualizuje více konfiguračních hodnot najednou.

        Args:
            updates (Dict): Slovník s klíči a hodnotami pro aktualizaci

        Raises:
            KeyError: Při pokusu o aktualizaci neexistujícího klíče
            ValueError: Při pokusu o nastavení neplatné hodnoty
        """

        # Validace klíčů a hodnot
        self._validate_config_dict(updates)

        # Přepis hodnot do konfigurace instance
        for key, value in updates.items():
            self.config[key] = value

        # Přepis hodnot do konfiguračního souboru
        config_path = self._get_config_file_path()
        self._save_config_to_file(config_path, self.config)

        logging.info(f"Aktualizovány konfigurace: {list(updates.keys())}")


    def reset_config(self) -> None:
        """
        Resetuje konfiguraci na výchozí hodnoty.

        Metoda nejprve přepíše hodnoty v instančním slovníku.
        Nakonec metoda uloží hodnoty do konfiguračního souboru.
        Pokud se to nepovede, metoda načte zpět původní hodnoty.
        """

        # Nastavení konfigurace na defaultní hodnoty
        self.config = self.DEFAULTS.copy()

        # Uložení hodnot do konfiguračního souboru
        path = self._get_config_file_path()
        if not self._save_config_to_file(path, self.config):
            self._load_default_config()

        logging.info("Konfigurace byla resetována na výchozí hodnoty.")




