import logging
from pathlib import Path


class DeleteConfigFileMixin:

    @classmethod
    def _delete_config_file(
            cls,
            config_file_path: Path = None,
    ) -> bool:
        """
        Metoda pro smazání konfiguračního souboru.
        """

        try:
            # Pokud není zadána cesta, použije se výchozí
            config_file_path = config_file_path or cls._config_path

            # Pokus o smazání souboru
            config_file_path.unlink()
            logging.debug(
                f"Success with delete config file: "
                f"File was deleted from this location: {config_file_path} "
            )
            return True

        except AttributeError:
            # self._config_path neexistuje
            logging.error(
                f"Error while delete config file: "
                f"Default config file path (cls._config_path) is not defined."
            )

        except FileNotFoundError:
            logging.warning(
                f"Error while delete config file: "
                f"Config file not found at {config_file_path}. "
                f"Nothing to delete."
            )

        except PermissionError:
            logging.error(
                f"Error while delete config file: "
                f"Permission denied to delete config file at {config_file_path}."
            )

        except IsADirectoryError:
            logging.error(
                f"Error while delete config file: "
                f"Path {config_file_path} is a directory, not a file."
            )

        except OSError as e:
            logging.error(
                f"Error while delete config file: "
                f"OS error occurred while trying to delete config file "
                f"at {config_file_path}: {e}."
            )

        return False

