import os
import json
import logging
from typing import Dict, Union


class LoadDefaultConfigMixin:

    def _load_default_config(self) -> Dict[str, Union[int, str, bool]]:
        """
        Načte konfiguraci ze souboru nebo vytvoří výchozí.

        Metoda nejprve načte cestu k souboru.
        Po té ověří její existenci a obsah.
        Když vše proběhne v pořádku, vrátí konfigurační slovník ze souboru.
        Když soubor neexistuje, vytvoří nový s výchozími hodnotami.

        Returns:
            Dict: Načtená nebo výchozí konfigurace
        """

        # Načtení cesty ke konfiguračnímu souboru
        config_path = os.path.join(self._config_dir, 'config.json')

        # Kontrola, zda soubor existuje
        if os.path.exists(config_path):

            try:
                # Načtení, kontrola a vrácení konfiguračního slovníku ze souboru
                config = self._read_config_file(config_path)
                if self._validate_config_dict(config):
                    return config

            except json.JSONDecodeError as e:
                logging.warning(f"Chyba při načítání konfigurace: {e}")

        # Pokud soubor neexistuje, bude vytvořen nový s výchozími hodnotami
        self._save_config_to_file(config_path, self.DEFAULTS)
        return self.DEFAULTS.copy()

