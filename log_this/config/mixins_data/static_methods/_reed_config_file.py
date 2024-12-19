import json
import logging


class ReedConfigFileMixin:


    @staticmethod
    def _reed_config_file(path):
        """
        Načte soubor s konfiguracemi a vrátí slovník s konfiguracemi.

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