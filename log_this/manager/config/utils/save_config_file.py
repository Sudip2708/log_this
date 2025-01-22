import json
from pathlib import Path

from ..errors import SaveConfigFileError


def save_config_file(config_file_path: Path, config_dict: dict) -> None:
    """
    Uloží konfiguraci do souboru.

    Args:
        config_file_path (Path): Cesta ke konfiguračnímu souboru.
        config_dict (dict): Konfigurační data.

    Raises:
        SaveConfigError: Pokud nastane chyba při ukládání souboru.
    """

    try:

        # Uložení poskytnuté konfigurace
        with config_file_path.open('w') as config_file:
            json.dump(config_dict, config_file, indent=4)

    except PermissionError as e:
        raise SaveConfigFileError(
            exception_type=PermissionError,
            config_file_path=config_file_path,
            error_info={
                "detail": f"Permission denied: {type(e).__name__}({str(e)})",
                "hint": "Ensure you have write permissions for the file."
            }
        )

    except OSError as e:
        raise SaveConfigFileError(
            exception_type=OSError,
            config_file_path=config_file_path,
            error_info={
                "detail": f"I/O error: {type(e).__name__}({str(e)})",
                "hint": "Check for file locks or disk issues."
            }
        )
    except TypeError as e:
        raise SaveConfigFileError(
            exception_type=TypeError,
            config_file_path=config_file_path,
            error_info={
                "detail": f"Data serialization error: {type(e).__name__}({str(e)})",
                "hint": "Ensure the configuration data is serializable to JSON."
            }
        )

    except Exception as e:
        raise SaveConfigFileError(
            exception_type=type(e),
            config_file_path=config_file_path,
            error_info={
                "detail": f"Unexpected error: {type(e).__name__}({str(e)})",
                "hint": "Contact system administrator."
            }
        )
