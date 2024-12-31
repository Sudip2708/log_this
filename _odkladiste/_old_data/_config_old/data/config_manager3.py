import os
import json
import logging
from typing import Union, Dict, Any, Optional

from .mixins_data import ConfigConstants
from ..modes.utils import loger_settings  # Import vašeho existujícího loggeru
from ..local_manager import \
    LocalManager  # Import LocalManageru pro konzistentní formátování


class ConfigChangeLogger:
    """
    Třída pro logování změn konfigurace s respektováním stávajícího logovacího systému.
    """

    def __init__(self):
        """
        Inicializace loggeru a lokálního manažera pro konzistentní formátování.
        """
        self.logger = loger_settings()
        self.manager = LocalManager()

    def log_config_change(
            self,
            key: str,
            old_value: Any,
            new_value: Any,
            mode: int = 2  # Defaultní mód pro logování změn
    ):
        """
        Zaloguje změnu konfigurace s využitím stávajícího logovacího systému.

        Args:
            key (str): Klíč, jehož hodnota byla změněna
            old_value (Any): Původní hodnota
            new_value (Any): Nová hodnota
            mode (int): Úroveň detailu logování
        """
        # Získání odsazení a nastavení blank lines
        indent = self.manager.get_indent()
        start_blank, end_blank = self.manager.get_blank_lines()

        # Logování změny konfigurace v konzistentním formátu
        self.logger.debug(f"{start_blank}{indent}"
                          f"# CONFIG CHANGE: {key}")

        if mode >= 2:
            self.logger.debug(f"{indent}# Old value: {old_value}")
            self.logger.debug(f"{indent}# New value: {new_value}")

        self.logger.debug(f"{indent}# Configuration updated{end_blank}")


class ConfigManager:
    """
    Rozšířený ConfigManager s podporou logování změn konfigurace.
    """

    def __init__(self):
        """
        Inicializace ConfigManageru s loggováním změn.
        """
        self.config_change_logger = ConfigChangeLogger()

    @classmethod
    def set_config_value(
            cls,
            key: str,
            value: Any,
            validate: bool = True,
            log_change: bool = True
    ) -> Optional[bool]:
        """
        Rozšířená metoda pro nastavení konfigurace s volitelným logováním.

        Args:
            key (str): Klíč konfigurace pro změnu
            value (Any): Nová hodnota pro daný klíč
            validate (bool): Zda provést validaci hodnoty
            log_change (bool): Zda zaznamenat změnu do logu

        Returns:
            Optional[bool]: Výsledek nastavení konfigurace
        """
        try:
            # Konfigurace a cesty (shodné s předchozí implementací)
            config_dir = os.path.dirname(__file__)
            config_path = os.path.join(config_dir, 'config.json')

            # Kontrola existence klíče
            if key not in ConfigConstants.DEFAULT_CONFIG:
                raise ValueError(f"Neplatný klíč konfigurace: {key}")

            # Validace hodnoty
            from .mixins_data import validate_value
            validated_value = (
                validate_value(value, ConfigConstants.DEFAULT_CONFIG[key], key)
                if validate
                else value
            )

            # Načtení aktuální konfigurace
            with open(config_path, 'r') as config_file:
                current_config = json.load(config_file)

            # Kontrola, zda je hodnota již nastavena
            if current_config.get(key) == validated_value:
                return False

            # Uložení původní hodnoty pro logging
            old_value = current_config.get(key)

            # Aktualizace konfigurace
            current_config[key] = validated_value

            # Uložení aktualizované konfigurace
            with open(config_path, 'w') as config_file:
                json.dump(current_config, config_file, indent=2)

            # Volitelné logování změny
            if log_change:
                instance = cls()
                instance.config_change_logger.log_config_change(
                    key, old_value, validated_value
                )

            # Aktualizace třídy LogThisConfig
            from .config import LogThisConfig
            config_instance = LogThisConfig()
            config_instance._load_config(config_path)

            return True

        except Exception as e:
            logging.error(f"Chyba při nastavování konfigurace: {e}")
            raise

