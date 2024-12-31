import logging
from typing import Union


class UpdateConfigMixin:


    def update_config(
            self,
            key: str,
            value: Union[int, str, bool]
    ) -> None:
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
        if self._validate_key_and_value(key, value):

            # Uložení změny do instance třídy
            self.config[key] = value

            # Uložení změny do konfiguračního souboru
            path = self._get_config_file_path()
            if not self._save_config_to_file(path, self.config):
                self._load_default_config()

            # Dodatečná úprava pro nastavení maximální rekurze pro serializer
            if key == "max_depth":
                from log_this.manager.serializer import get_serializer
                serializer = get_serializer()
                serializer.max_depth = value

            logging.info(
                f"Úspěšná změna hodnoty pro klíč {key} "
                f"na hodnotu {value}.")

        else:
            logging.error(
                f"Úprava konfigurace pro klíč {key} "
                f"a hodnotu {value} se nezdařila."
            )

