import os
import json
import logging
from typing import Union, Dict, Any, Optional

from .mixins_data import (
    ConfigConstants,
    ensure_config_file,
    validate_and_update_config
)

# Nastavení základního loggingu
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='log_this_config.log'
)
logger = logging.getLogger('log_this.config')


class ConfigManagerError(Exception):
    """Vlastní výjimka pro chyby v ConfigManageru."""
    pass


class ConfigManager:
    """
    Rozšířená správa konfigurace pro log_this knihovnu s rozšířenými možnostmi.

    Poskytuje pokročilé metody pro:
    - Bezpečnou správu konfiguračních hodnot
    - Robustní error handling
    - Logování změn konfigurace
    """

    @classmethod
    def set_config_value(
            cls,
            key: str,
            value: Any,
            validate: bool = True
    ) -> Optional[bool]:
        """
        Nastaví hodnotu v konfiguraci s rozšířenou validací a bezpečností.

        Args:
            key (str): Klíč konfigurace pro změnu
            value (Any): Nová hodnota pro daný klíč
            validate (bool, optional): Zda provést validaci hodnoty. Defaults to True.

        Returns:
            Optional[bool]: True pokud byla hodnota změněna, False pokud již byla nastavena,
                            None v případě chyby

        Raises:
            ConfigManagerError: Pro neočekávané chyby při nastavování konfigurace
        """
        try:
            # Načtení cesty ke konfiguračnímu souboru
            config_dir = os.path.dirname(__file__)
            config_path = os.path.join(config_dir, 'config.json')

            # Kontrola existence klíče v defaultní konfiguraci
            if key not in ConfigConstants.DEFAULT_CONFIG:
                logger.error(f"Neplatný klíč konfigurace: {key}")
                raise ConfigManagerError(f"Neplatný klíč konfigurace: {key}")

            # Validace hodnoty (pokud je povolena)
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
                logger.info(
                    f"Hodnota pro klíč {key} je již nastavena na {validated_value}")
                return False

            # Aktualizace konfigurace
            current_config[key] = validated_value

            # Uložení aktualizované konfigurace
            with open(config_path, 'w') as config_file:
                json.dump(current_config, config_file, indent=2)

            # Logování změny
            logger.info(
                f"Změna konfigurace: {key} nastaven na {validated_value}")

            # Aktualizace třídy LogThisConfig
            from .config import LogThisConfig
            config_instance = LogThisConfig()
            config_instance._load_config(config_path)

            return True

        except (IOError, PermissionError) as e:
            logger.error(f"Chyba při zápisu konfigurace: {e}")
            raise ConfigManagerError(f"Nelze zapsat konfiguraci: {e}")
        except Exception as e:
            logger.error(f"Neočekávaná chyba při nastavování konfigurace: {e}")
            raise ConfigManagerError(f"Chyba nastavení konfigurace: {e}")

    @classmethod
    def get_config_value(
            cls,
            key: Optional[str] = None
    ) -> Union[Dict[str, Any], Any, None]:
        """
        Vrátí aktuální konfiguraci nebo hodnotu specifického klíče.

        Args:
            key (Optional[str], optional): Specifický klíč konfigurace.
                                           Pokud None, vrátí kompletní konfiguraci.

        Returns:
            Union[Dict[str, Any], Any, None]:
                - Kompletní konfigurace, pokud key je None
                - Hodnota specifického klíče
                - None, pokud klíč neexistuje

        Raises:
            ConfigManagerError: Pro neočekávané chyby při čtení konfigurace
        """
        try:
            # Načtení cesty ke konfiguračnímu souboru
            config_dir = os.path.dirname(__file__)
            config_path = os.path.join(config_dir, 'config.json')

            # Načtení aktuální konfigurace
            with open(config_path, 'r') as config_file:
                current_config = json.load(config_file)

            # Vrácení kompletní konfigurace nebo specifické hodnoty
            if key is None:
                return current_config

            # Kontrola existence klíče
            if key not in current_config:
                logger.warning(f"Klíč {key} nebyl nalezen v konfiguraci")
                return None

            return current_config.get(key)

        except FileNotFoundError:
            logger.error("Konfigurační soubor nebyl nalezen")
            raise ConfigManagerError("Konfigurační soubor nebyl nalezen")
        except json.JSONDecodeError:
            logger.error("Chyba při parsování konfiguračního souboru")
            raise ConfigManagerError("Neplatný formát konfiguračního souboru")
        except Exception as e:
            logger.error(f"Neočekávaná chyba při čtení konfigurace: {e}")
            raise ConfigManagerError(f"Chyba čtení konfigurace: {e}")

    @classmethod
    def reset_config(cls) -> None:
        """
        Obnoví konfiguraci na výchozí hodnoty z ConfigConstants.

        Raises:
            ConfigManagerError: Pro neočekávané chyby při resetu konfigurace
        """
        try:
            # Načtení cesty ke konfiguračnímu souboru
            config_dir = os.path.dirname(__file__)
            config_path = os.path.join(config_dir, 'config.json')

            # Obnovení konfigurace na defaultní hodnoty
            with open(config_path, 'w') as config_file:
                json.dump(ConfigConstants.DEFAULT_CONFIG, config_file, indent=2)

            # Logování resetu
            logger.info("Konfigurace byla obnovena na výchozí hodnoty")

            # Aktualizace třídy LogThisConfig
            from .config import LogThisConfig
            config_instance = LogThisConfig()
            config_instance._load_config(config_path)

        except (IOError, PermissionError) as e:
            logger.error(f"Chyba při resetu konfigurace: {e}")
            raise ConfigManagerError(f"Nelze resetovat konfiguraci: {e}")
        except Exception as e:
            logger.error(f"Neočekávaná chyba při resetu konfigurace: {e}")
            raise ConfigManagerError(f"Chyba resetu konfigurace: {e}")