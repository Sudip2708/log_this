import os
import json
from typing import Union, Dict, Any

from .mixins_data import (
    ConfigConstants,
    ensure_config_file,
    validate_and_update_config
)

class ConfigManager:
    """
    Rozšířená správa konfigurace pro log_this knihovnu.

    Poskytuje metody pro:
    - Změnu konfiguračních hodnot
    - Výpis aktuálního nastavení
    - Obnovení výchozích hodnot
    """

    @classmethod
    def set_config_value(cls, key: str, value: Any) -> bool:
        """
        Nastaví hodnotu v konfiguraci.

        Args:
            key (str): Klíč konfigurace pro změnu
            value (Any): Nová hodnota pro daný klíč

        Returns:
            bool: True pokud byla hodnota změněna, False pokud již byla nastavena
        """
        # Načtení cesty ke konfiguračnímu souboru
        config_dir = os.path.dirname(__file__)
        config_path = os.path.join(config_dir, 'config.json')

        # Kontrola existence klíče v defaultní konfiguraci
        if key not in ConfigConstants.DEFAULT_CONFIG:
            raise ValueError(f"Neplatný klíč konfigurace: {key}")

        # Validace hodnoty
        from .mixins_data import validate_value
        validated_value = validate_value(value, ConfigConstants.DEFAULT_CONFIG[key], key)

        # Načtení aktuální konfigurace
        with open(config_path, 'r') as config_file:
            current_config = json.load(config_file)

        # Kontrola, zda je hodnota již nastavena
        if current_config.get(key) == validated_value:
            return False

        # Aktualizace konfigurace
        current_config[key] = validated_value

        # Uložení aktualizované konfigurace
        with open(config_path, 'w') as config_file:
            json.dump(current_config, config_file, indent=2)

        # Aktualizace třídy LogThisConfig
        from .config import LogThisConfig
        config_instance = LogThisConfig()
        config_instance._load_config(config_path)

        return True

    @classmethod
    def get_config_value(cls, key: str = None) -> Union[Dict[str, Any], Any]:
        """
        Vrátí aktuální konfiguraci nebo hodnotu specifického klíče.

        Args:
            key (str, optional): Specifický klíč konfigurace

        Returns:
            Buď kompletní konfigurace nebo hodnota specifického klíče
        """
        # Načtení cesty ke konfiguračnímu souboru
        config_dir = os.path.dirname(__file__)
        config_path = os.path.join(config_dir, 'config.json')

        # Načtení aktuální konfigurace
        with open(config_path, 'r') as config_file:
            current_config = json.load(config_file)

        # Vrácení kompletní konfigurace nebo specifické hodnoty
        return current_config.get(key) if key else current_config

    @classmethod
    def reset_config(cls) -> None:
        """
        Obnoví konfiguraci na výchozí hodnoty z ConfigConstants.
        """
        # Načtení cesty ke konfiguračnímu souboru
        config_dir = os.path.dirname(__file__)
        config_path = os.path.join(config_dir, 'config.json')

        # Obnovení konfigurace na defaultní hodnoty
        with open(config_path, 'w') as config_file:
            json.dump(ConfigConstants.DEFAULT_CONFIG, config_file, indent=2)

        # Aktualizace třídy LogThisConfig
        from .config import LogThisConfig
        config_instance = LogThisConfig()
        config_instance._load_config(config_path)