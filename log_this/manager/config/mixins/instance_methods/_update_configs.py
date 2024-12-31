import logging
from typing import Dict, Union


class UpdateConfigsMixin:


    def update_configs(
            self,
            updates: Dict[str, Union[int, str, bool]]
    ) -> None:
        """
        Aktualizuje více konfiguračních hodnot najednou.

        Args:
            updates (Dict): Slovník s klíči a hodnotami pro aktualizaci

        Raises:
            KeyError: Při pokusu o aktualizaci neexistujícího klíče
            ValueError: Při pokusu o nastavení neplatné hodnoty
        """

        # Validace klíčů a hodnot
        if self._validate_config_dict(updates):

            # Přepis hodnot do konfigurace instance
            for key, value in updates.items():
                self.config[key] = value

            # Přepis hodnot do konfiguračního souboru
            config_path = self._get_config_file_path()
            self._save_config_to_file(config_path, self.config)

            logging.info(f"Aktualizovány konfigurace: {list(updates.keys())}")

        else:
            logging.error(f"Aktualizace  se nezdařila z důvodu neplatných hodnot.")


