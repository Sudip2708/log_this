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

        # Kontrola, zda již hodnota nebyla aktualizovaná
        if self.config[key] == value:
            logging.debug(
                f"Info for update config: "
                f"The configuration key {key} is already set to {value} "
                f"No change was made."
            )
            return

        # Kontrola klíče a hodnoty
        if self._validate_key_and_value(key, value):

            # Uložení změny do instance třídy
            self.config[key] = value
            logging.debug(
                f"Success with update config: "
                f"The configuration for the key {key} has been changed to {value} "
            )

            # Uložení změny do konfiguračního souboru
            if self._create_config_file(self.config):
                logging.debug(
                    f"Success with update config file: "
                    f"The current configuration has been saved to a file: "
                    f"{self._config_path} "
                )

            # Pokud uložení změny neproběhlo v pořádku
            else:
                logging.error(
                    f"Error while update config: "
                    f"The configuration file could not be updated. \n"
                    f"Running info for this Error: "
                    f"The library will run without a configuration file. \n"
                    f"Possible limitations: "
                    f"Default values will be loaded, which can be changed, "
                    f"but they will not be saved for next time."
                )

            # Dodatečná úprava pro nastavení maximální rekurze pro serializer
            if key == "max_depth":
                from log_this.manager.serializer import get_serializer
                serializer = get_serializer()
                serializer.max_depth = value
                logging.debug(
                    f"Success with update config file: "
                    f"The SafeSerializer class attribute 'max_depth' "
                    f"was changed to {value} "
                )

        # Pokud validace neproběhne úspěšně
        else:
            logging.error(
                f"Error while update config: "
                f"Could not update key {key} to value {value}. "
                f"The values provided are not valid."
            )
