import logging
import json
from pathlib import Path
from typing import Dict


class CreateConfigFileMixin:

    @classmethod
    def _create_config_file(
            cls,
            config_dict: Dict[str, str]  = None,
            config_file_path: Path = None
    ) -> bool:
        """
        Metoda pro vytvoření konfiguračního souboru.

        Parameters:
            config_dict (dict): Slovník s konfigurací, která bude zapsána do souboru.
                                Pokud není zadán, použije se výchozí nastavení (cls.DEFAULTS).
            config_file_path (Path): Cesta k vytvoření konfiguračního souboru.
                                     Pokud není zadána, použije se výchozí cesta (cls._config_path).

        Returns:
            bool: True, pokud byl soubor úspěšně vytvořen, False v případě chyby.

        Info:
            config_file_path.parent.mkdir(parents=True, exist_ok=True)
                - parents=True: Pokud složka (nebo složky) v cestě neexistují, vytvoří je včetně všech nadřazených složek.
                - exist_ok=True: Pokud složka již existuje, nezpůsobí výjimku (nevrátí chybu).
        """

        # Pokud je zadán vlastní slovník, ale neprojde validací
        if config_dict and not cls._validate_config_dict(config_dict):
            logging.error(
                f"Error while create config file: "
                f"File not created. "
                f"The received configuration dictionary is not valid. "
            )
            return False

        try:

            # Pokud není zadán slovník, použije se výchozí konfigurace
            config_dict = config_dict or cls.DEFAULTS

            # Pokud není zadána cesta, použije se výchozí
            config_file_path = config_file_path or cls._config_path

            # Zajištění existence složky
            config_file_path.parent.mkdir(parents=True, exist_ok=True)

            # Vytvoření souboru a zápis dat ve formátu JSON
            with config_file_path.open('w', encoding='utf-8') as file:
                json.dump(config_dict, file, indent=4, ensure_ascii=False)

            logging.debug(
                f"Success with create config file: "
                f"File was created at this location: {config_file_path} "
            )
            return True

        except AttributeError:
            # Ověření existence atributů a výpis pro první z nich
            if not hasattr(cls, '_config_path'):
                logging.error(
                    f"Error while creating config file: "
                    f"File not created. "
                    f"Default config file path (cls._config_path) is not defined. "
                )
            elif not hasattr(cls, 'DEFAULTS'):
                logging.error(
                    f"Error while creating config file: "
                    f"File not created. "
                    f"Defaults (cls.DEFAULTS) are not defined. "
                )

        except FileNotFoundError:
            logging.error(
                f"Error while creating config file: "
                f"File not created. "
                f"Path {config_file_path} is invalid or could not be created. "
            )

        except PermissionError:
            logging.error(
                f"Error while creating config file: "
                f"File not created. "
                f"Permission denied to create config file at {config_file_path}. "
            )

        except IsADirectoryError:
            logging.error(
                f"Error while creating config file: "
                f"File not created. "
                f"Path {config_file_path} is a directory, not a file. "
            )

        except json.JSONDecodeError as e:
            logging.error(
                f"Error while creating config file: "
                f"File not created. "
                f"Failed to serialize config_dict to JSON. Error: {e} "
            )

        except OSError as e:
            logging.error(
                f"Error while creating config file: "
                f"File not created. "
                f"OS error occurred while trying to create config file "
                f"at {config_file_path}: {e}. "
            )

        return False

