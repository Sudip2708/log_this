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

        # Načtení singleton instance konfugurace a získání slovníku s aktuálními hodnotami
        from log_this.config import get_config
        config = get_config()
        actual_value = config.get_attributes_dict()

        # Ověření hodnoty, zda se nachází klíč ve slovníku:
        if key not in actual_value:
            raise ValueError(f"Neplatný klíč konfigurace: {key}")

        # Ověření, zda je hodnota nová
        if actual_value[key] == value:
            return False

        # Ověření, že je hodnota planá
        from log_this.config.data.mixins_data._validate_value import validate_value
        if validate_value(value, False, key):
            raise ValueError(f"Uvedená hodnota není validní. Hodnota: {value} Klíč: {key} ")

        # Načtení cesty ke konfiguračnímu souboru
        config_dir = os.path.dirname(__file__)
        config_path = os.path.join(config_dir, 'config.json')

        # Načtení aktuální konfigurace
        with open(config_path, 'r') as config_file:
            current_config = json.load(config_file)

        # Aktualizace konfigurace
        current_config[key] = value

        # Uložení aktualizované konfigurace
        with open(config_path, 'w') as config_file:
            json.dump(current_config, config_file, indent=2)

        # Aktualizace třídy LogThisConfig
        config.set_value(key, value)

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