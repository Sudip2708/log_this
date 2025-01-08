import logging
from typing import Dict, Union


class LoadConfigDictMixin:

    @classmethod
    def _load_config_dict(cls) -> Dict[str, Union[int, str, bool]]:
        """
        Načte konfiguraci ze souboru nebo vytvoří výchozí.

        Metoda nejprve načte cestu k souboru.
        Po té ověří její existenci a obsah.
        Když vše proběhne v pořádku, vrátí konfigurační slovník ze souboru.
        Když soubor neexistuje, vytvoří nový s výchozími hodnotami.

        Returns:
            Dict: Načtená nebo výchozí konfigurace
        """

        # Načtení konfiguračního slovníku ze souboru
        config_dict = cls._read_config_file()

        # Pokud načtení proběhlo v pořádku
        if config_dict:

            # Navrácení načtené konfigurace
            return config_dict

        # Pokud načtení neproběhlo v pořádku
        else:

            # Info o neúspěšném načtení
            logging.error(
                f"Error while 'load default config': "
                f"There is no data from config file."
            )

            # Pokus o smazání souboru
            if cls._config_path.exist():

                # Info o detekci poškozeného souboru
                logging.debug(
                    f"Info for 'load default config': "
                    f"A corrupted configuration file has been detected. "
                    f"It will be deleted and replaced with a new one."
                )

                # Pokus o smazání souboru
                if cls._delete_config_file():
                    logging.debug(
                        f"Info for 'load default config': "
                        f"A corrupted configuration file has been deleted."
                    )

                # Pokud se soubor nepovedlo smazat
                else:
                    logging.error(
                        f"Error while 'load default config': "
                        f"Failed to delete a corrupted configuration file. \n"
                        f"Running info for this Error: "
                        f"The library will try to rewrite this corrupted file "
                        f"with default values."
                    )

            # Pokus o vytvoření nového souboru
            if cls._create_config_file():
                logging.debug(
                    f"Info for 'load default config': "
                    f"A new configuration file with default values has been created."
                )

            # Pokud se nový soubor nepovedlo vytvořit
            else:
                logging.error(
                    f"Error while 'load default config': "
                    f"Failed to create a new configuration file. \n"
                    f"Running info for this Error: "
                    f"The library will run without a configuration file. \n"
                    f"Possible limitations: "
                    f"Default values will be loaded, which can be changed, "
                    f"but they will not be saved for next time."
                )

            # Nvrácení defaultních hodnot
            return cls.DEFAULTS.copy()








