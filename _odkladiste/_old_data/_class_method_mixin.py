import os
import json
import logging
from typing import Dict, Union, Any


class ClassMethodMixin:

    @classmethod
    def _get_config_file_path(cls, file_name='config.json') -> str:
        """
        Určí cestu ke konfiguračnímu souboru.

        Cestu určuje dle umístění souboru s definicí třídy.
        Konfigurační soubor tedy bude vždy na stejném umístění ,
        jako je soubor s definicí třídy LogThisConfig.

        Returns:
            str: Absolutní cesta ke konfiguračnímu JSON souboru
        """

        # Načtení cesty k souboru s kodem třídy
        config_dir = os.path.dirname(__file__)

        # Vrácení cesty s odkazen na config.json
        return os.path.join(config_dir, file_name)


    @classmethod
    def _validate_value(cls, key: str, value: Any) -> bool:
        """
        Validuje konfigurační hodnotu pro daný klíč.

        Nejprve zkontroluje, zda hodnota nespadá pod hodnoty s vlastní validací.
        Pokud ne, pak ověří její přítomnost v konfiguračním slovníku,
        a zda je hodnota v rozmezí 0 - 4.

        Args:
            key (str): Klíč konfigurace
            value (Any): Hodnota ke kontrole

        Returns:
            bool: Indikuje platnost hodnoty
        """

        # Pokud klíč odkazuje na nastavení zobrazení prázdných řádek mezi logy
        if key == 'blank_lines' and isinstance(value, bool):
            return True

        # Pokud klíč odkazuje na nastavení zobrazení délky docstringu
        elif key == 'docstring_lines' and (
                isinstance(value, int) or value == 'all'):
            return True

        # Pokud klíč odkazuje na nastavení maximálního povoleného zanoření
        # (ochrana proti nekonečné rekurzy)
        elif key == 'max_depth' and isinstance(value, int):
            return True

        # Ve všech ostatních případech zkontroluj přítomnost klíče v defaultním slovníku
        # a zda hodnota obsahuje číslice mezi 0 a 4
        elif key in cls.DEFAULTS and value in (0, 1, 2, 3, 4):
            return True

        # Pokud klíč není rospoznán
        return False


    @classmethod
    def _key_and_value_check(cls, key: str,
                             value: Union[int, str, bool]) -> None:
        """
        Ověří platnost klíče a hodnoty konfigurace.

        Metoda nejprve zkontroluje přítomnos klíče v defaultním slovníku
        Následně ověří platnost hodnoty.

        Args:
            key: Klíč konfigurace
            value: Hodnota konfigurace

        Raises:
            KeyError: Pokud klíč není v DEFAULTS
            ValueError: Pokud hodnota není validní
        """
        if key not in cls.DEFAULTS:
            raise KeyError(f"Neznámý klíč konfigurace: {key}")

        if not cls._validate_value(key, value):
            raise ValueError(f"Neplatná hodnota pro {key}: {value}")


    @classmethod
    def _validate_config_dict(cls, config: Dict[str, Any]) -> bool:
        """
        Metoda pro ověření klíčů a hodnot konfiguračního slovníku.

        Metoda nejprve ověří přítomnost klíče v defaultním slovníku.
        Následně ověří i správný formát hodnoty.

        Args:
            config (Dict[str, Any]): Konfigurace ke kontrole

        Returns:
            bool: Indikuje validitu celé konfigurace
        """

        # Cyklus rozebírající slovník na klíč a hodnotu
        for key, value in config.items():

            # Ověření klíče a hodnoty
            try:
                cls._key_and_value_check(key, value)

            # Zachycení chybného klíče
            except KeyError:
                logging.warning(f"Neplatný klíč: {key}")
                return False

            # Zachycení chybné hodnoty
            except (KeyError, ValueError):
                logging.warning(f"Neplatná hodnota pro klíč: {key}: {value}")
                return False

        # Pokud ověření proběhne bez chyb
        return True

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
