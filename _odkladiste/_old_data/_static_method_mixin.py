import os
import json
import logging
from typing import Dict, Union, Any


class StaticMethodMixin:

    @staticmethod
    def _save_config_to_file(path, config_dict):
        """
        Uloží konfiguraci do souboru ve formátu JSON.

        Metoda nejprve se pokusí otevřít a přepsat případný obsah souboru.
        Pokud se ji to povede vypíše potvrzovací zprávu a vrátí True.

        Args:
            path (str): Cesta k souboru.
            config_dict (dict): Slovník s konfigurací.

        Returns:
            bool: True, pokud byl soubor úspěšně uložen, jinak False.
        """
        try:

            # Otevření a zapsání dat do souboru
            # (dojde k jeho celému přepsání)
            with open(path, 'w') as file:
                json.dump(config_dict, file, indent=2)

            # Info log a potvrzení úspěšné operace
            logging.info(f"Konfigurace byla uložena do: {path}")
            return True

        except FileNotFoundError as e:
            logging.error(f"Chyba: Cesta k souboru neexistuje: {e}")

        except PermissionError as e:
            logging.error(
                f"Chyba: Nedostatečná oprávnění pro zápis do souboru: {e}")

        except TypeError as e:
            logging.error(
                f"Chyba: Konfigurační data nejsou serializovatelná do JSON: {e}")

        except json.JSONEncodeError as e:
            logging.error(f"Chyba při serializaci JSON: {e}")

        except OSError as e:
            logging.error(f"Chyba při práci se souborem: {e}")

        except Exception as e:
            logging.error(f"Neznámá chyba při ukládání souboru: {e}")

        return False


    @staticmethod
    def _reed_config_file(path):
        """
        Uloží konfiguraci do souboru ve formátu JSON.

        Metoda se nejprve pokusí načíst obsah souboru.
        Pokud se ji to povede vypíše potvrzovací zprávu a vrátí obsah.

        Args:
            path (str): Cesta k souboru.

        Returns:
            bool: True, pokud byl soubor úspěšně uložen, jinak False.
        """
        try:

            # Otevření a načtení dat ze souboru
            with open(path, 'r') as file:
                config = json.load(file)

            # Info log úspěšné operace a navrácení hodnot
            logging.info(f"Konfigurace byla uložena do: {path}")
            return config

        except FileNotFoundError as e:
            logging.error(f"Chyba: Cesta k souboru neexistuje: {e}")

        except PermissionError as e:
            logging.error(
                f"Chyba: Nedostatečná oprávnění pro zápis do souboru: {e}")

        except TypeError as e:
            logging.error(
                f"Chyba: Konfigurační data nejsou serializovatelná do JSON: {e}")

        except json.JSONEncodeError as e:
            logging.error(f"Chyba při serializaci JSON: {e}")

        except OSError as e:
            logging.error(f"Chyba při práci se souborem: {e}")

        except Exception as e:
            logging.error(f"Neznámá chyba při ukládání souboru: {e}")

        return False