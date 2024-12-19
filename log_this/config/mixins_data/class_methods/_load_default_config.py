import os
import json
import logging
from typing import Dict, Union


class LoadDefaultConfigMixin:


    @classmethod
    def _load_default_config(cls) -> Dict[str, Union[int, str, bool]]:
        """
        Načte konfiguraci ze souboru nebo vytvoří výchozí.

        Metoda nejprve načte cestu k souboru.
        Po té ověří její existenci a obsah.
        Když vše proběhne v pořádku vrátí konfigurační slovník ze souboru.
        Když soubor neexistuje vytvoří nový s defaultními hodnotami.

        Returns:
            Dict: Načtená nebo výchozí konfigurace
        """

        # Načtení ceesty ke konfiguračnímu souboru
        config_path = cls._get_config_file_path()

        # Kontrola zda soubor existuje
        if os.path.exists(config_path):

            # Načtení, kontrola a vrácení konfiguračního slovníku ze souboru
            try:
                config = cls._reed_config_file(config_path)
                if cls._validate_config_dict(config):
                    return config

            # Zpracování výjimek
            except json.JSONDecodeError as e:
                logging.warning(f"Chyba při načítání konfigurace: {e}")

        # Pokud soubor neexistuje bude vytvořen nový s defaultními hodnotami
        cls._save_config_to_file(config_path, cls.DEFAULTS)
        return cls.DEFAULTS.copy()
