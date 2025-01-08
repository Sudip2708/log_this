from pathlib import Path
import json
import logging


class ReadConfigFileMixin:

    @classmethod
    def _read_config_file(
            cls,
            config_file_path: Path = None
    ) -> bool:
        """
        Reads a configuration file and returns a dictionary with configurations.

        The method first tries to load the content of the file.
        If successful, it logs a confirmation message and returns the content.

        Args:
            path (Path): Path to the file.

        Returns:
            dict: Dictionary with the configuration.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
        """

        try:
            # Pokud není zadána cesta, použije se výchozí
            config_file_path = config_file_path or cls._config_path

            # Open and load data from the file
            with config_file_path.open('r') as config_file:
                config_dict = json.load(config_file)

            # Oznam o úspěšném načtení konfiguračního slovníku a navrácení dat
            logging.debug(
                f"Success with read config file: "
                f"The configuration dictionary was loaded from the file: {path}"
            )

            # Pokud je zadán vlastní slovník, ale neprojde validací
            if (config_file_path != cls._config_path
                    and not cls._validate_config_dict(config_dict)):
                logging.error(
                    f"Error while read config file: "
                    f"The configuration dictionary was not loaded! "
                    f"The received configuration dictionary is not valid. "
                )
                return False

            return config_dict

        except AttributeError:
            logging.error(
                f"Error while read config file: "
                f"The configuration dictionary was not loaded! "
                f"Default config file path (cls._config_path) is not defined."
            )

        except FileNotFoundError as e:
            logging.error(
                f"Error while read config file: "
                f"The configuration dictionary was not loaded! "
                f"The file path does not exist: {type(e).__name__}({str(e)})"
            )

        except PermissionError as e:
            logging.error(
                f"Error while read config file: "
                f"The configuration dictionary was not loaded! "
                f"Insufficient permissions to access the file: "
                f"{type(e).__name__}({str(e)})"
            )

        except TypeError as e:
            logging.error(
                f"Error while read config file: "
                f"The configuration dictionary was not loaded! "
                f"Configuration data is not JSON serializable: "
                f"{type(e).__name__}({str(e)})"
            )

        except json.JSONDecodeError as e:
            logging.error(
                f"Error while read config file: "
                f"The configuration dictionary was not loaded! "
                f"Something happened during JSON deserialization: "
                f"{e.msg}: line {e.lineno} column {e.colno} (char {e.pos})"
            )

        except OSError as e:
            logging.error(
                f"Error while read config file: "
                f"The configuration dictionary was not loaded! "
                f"Something happened while working with the file: "
                f"{type(e).__name__}({str(e)})"
            )

        except Exception as e:
            logging.error(
                f"Error while read config file: "
                f"The configuration dictionary was not loaded! "
                f"Something happened while reading the file: "
                f"{type(e).__name__}({str(e)})"
            )

        return False
