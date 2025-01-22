import json
from pathlib import Path

from ..errors import DeleteConfigFileError


def delete_config_file(config_file_path: Path) -> None:
    """
    Smaže konfigurační soubor.

    Args:
        config_file_path (Path): Cesta ke konfiguračnímu souboru.

    Raises:
        DeleteConfigError: Pokud nastane chyba při mazání souboru.
    """

    try:

        # Smazání aktuálního souboru
        config_file_path.unlink()

    except FileNotFoundError as e:
        raise DeleteConfigFileError(
            exception_type=FileNotFoundError,
            config_file_path=config_file_path,
            error_info={
                "detail": f"File not found: {type(e).__name__}({str(e)})",
                "hint": "The config file may have already been deleted."
            }
        )

    except PermissionError as e:
        raise DeleteConfigFileError(
            exception_type=PermissionError,
            config_file_path=config_file_path,
            error_info={
                "detail": f"Permission denied: {type(e).__name__}({str(e)})",
                "hint": "Check the file's permissions."
            }
        )

    except Exception as e:
        raise DeleteConfigFileError(
            exception_type=type(e),
            config_file_path=config_file_path,
            error_info={
                "detail": f"Unexpected error: {type(e).__name__}({str(e)})",
                "hint": "Contact system administrator."
            }
        )


