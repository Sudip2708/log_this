from pathlib import Path
import json
import logging


class ReadConfigFileMixin:

    @staticmethod
    def _read_config_file(
            path: Path,
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
            # Open and load data from the file
            with path.open('r') as file:
                config = json.load(file)

            # Info log for a successful operation and return the content
            logging.info(f"Configuration has been loaded from: {path}")
            return config

        except FileNotFoundError as e:
            logging.error(
                f"Error: The file path does not exist: "
                f"{type(e).__name__}({str(e)})"
            )

        except PermissionError as e:
            logging.error(
                f"Error: Insufficient permissions to access the file: "
                f"{type(e).__name__}({str(e)})"
            )

        except TypeError as e:
            logging.error(
                f"Error: Configuration data is not JSON serializable: "
                f"{type(e).__name__}({str(e)})"
            )

        except json.JSONDecodeError as e:
            logging.error(
                f"Error during JSON deserialization: "
                f"{e.msg}: line {e.lineno} column {e.colno} (char {e.pos})"
            )

        except OSError as e:
            logging.error(
                f"Error while working with the file: "
                f"{type(e).__name__}({str(e)})"
            )

        except Exception as e:
            logging.error(
                f"Unknown error occurred while reading the file: "
                f"{type(e).__name__}({str(e)})"
            )

        return False
