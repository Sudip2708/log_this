import json
import logging


class ImportConfigFromFileMixin:


    def import_config_from_file(
            self,
            import_path: str
    ) -> None:
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
            imported_config = self._read_config_file(import_path)

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


