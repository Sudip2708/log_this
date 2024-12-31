import os
import json
import logging
from datetime import datetime
from typing import Dict, Union, Any


class ImportExportMixin:

    def import_config_from_file(self, import_path: str) -> None:
        """
        Importuje konfiguraci z externího souboru.

        Metoda nejprve se pokusí načíst obsah souboru.
        Následně jej zkontroluje a uloží do konfigurace v instanci třýdy,
        a do konfiguračního souboru.

        Args:
            import_path (str): Cesta k souboru s konfigurací pro import

        Raises:
            FileNotFoundError: Pokud soubor neexistuje
            json.JSONDecodeError: Při chybě dekódování JSON
            ValueError: Při importu neplatné konfigurace
        """


        try:

            # Načtení obsahu souboru
            imported_config = self._reed_config_file(import_path)

            # Validace importované konfigurace
            if self._validate_config(imported_config):

                # Přiřazení hodnot do instanční konfigurace
                self.config = imported_config

                # Zapsání hodnot do konfiguračního souboru třídy
                config_path = self._get_config_file_path()
                self._save_config_to_file(config_path, imported_config)

                # Potvrzeí operace
                logging.info(f"Konfigurace importována z: {import_path}")

            # Pokud validace neprojde
            else:

                # Vyvolání výjimky
                raise ValueError(
                    "Importovaná konfigurace obsahuje neplatné hodnoty")

        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"Chyba při importu konfigurace: {e}")
            raise



    def export_config_to_file(self, export_path: Optional[str] = None) -> str:
        """
        Exportuje aktuální konfiguraci do samostatného souboru.

        Args:
            export_path (Optional[str]): Cesta pro export konfigurace.
                                         Pokud není zadána, použije se výchozí umístění.

        Returns:
            str: Cesta k exportovanému konfiguračnímu souboru
        """


        # Pokud není definovaná cesta
        if not export_path:

            # Vytvoření jména souboru
            file_name = (f'config_export_'
                         f'{datetime.now().strftime("%Y%m%d_%H%M%S")}_'
                         f'{os.getpid()}.json')

            # Vytvoření cesty k souboru
            export_path = self._get_config_file_path(file_name)


        try:

            # Uložení souboru a vrácení cesty
            self._save_config_to_file(export_path, self.config)
            return export_path

        except Exception as e:
            logging.error(f"Chyba při exportu konfigurace: {e}")
            raise