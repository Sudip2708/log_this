import json
import logging
from pathlib import Path
from typing import Dict


class SaveConfigToFileMixin:

    def _save_config_to_file(self,
            path: Path = self._config_path,
            config_dict: Dict[str, str] = self.DEFAULTS
    ) -> bool:
        """
        Saves the configuration to a file in JSON format.

        The method first attempts to open and overwrite any existing content in the file.
        If successful, it logs a confirmation message and returns True.

        Args:
            path (str): Path to the file.
            config_dict (dict): A dictionary containing the configuration.

        Returns:
            bool: True if the file was successfully saved, otherwise False.
        """
        try:

            # Open and write data to the file
            # (this will overwrite the entire file)
            with open(path, 'w') as file:
                json.dump(config_dict, file, indent=2)

            # Info log and confirmation of successful operation
            logging.info(
                f"Success with save config to file: "
                f"Configuration has been saved to: {path}"
            )
            return True


        except FileNotFoundError as e:
            logging.error(
                f"Error while save config to file: "
                f"The configuration dictionary was not saved! "
                f"The file path does not exist: {type(e).__name__}({str(e)})"
            )

        except PermissionError as e:
            logging.error(
                f"Error while save config to file: "
                f"The configuration dictionary was not saved! "
                f"Insufficient permissions to access the file: "
                f"{type(e).__name__}({str(e)})"
            )

        except TypeError as e:
            logging.error(
                f"Error while save config to file: "
                f"The configuration dictionary was not saved! "
                f"Configuration data is not JSON serializable: "
                f"{type(e).__name__}({str(e)})"
            )

        except json.JSONDecodeError as e:
            logging.error(
                f"Error while save config to file: "
                f"The configuration dictionary was not saved! "
                f"Something happened during JSON deserialization: "
                f"{e.msg}: line {e.lineno} column {e.colno} (char {e.pos})"
            )

        except OSError as e:
            logging.error(
                f"Error while save config to file: "
                f"The configuration dictionary was not saved! "
                f"Something happened while working with the file: "
                f"{type(e).__name__}({str(e)})"
            )

        except Exception as e:
            logging.error(
                f"Error while save config to file: "
                f"The configuration dictionary was not saved! "
                f"Something happened while reading the file: "
                f"{type(e).__name__}({str(e)})"
            )

        return False



