from pathlib import Path
from typing import Optional


def _load_file_content(
        file_path: Path,
        encoding: str = 'utf-8'
) -> Optional[str]:
    """
    Načte obsah souboru.

    Args:
        file_path (Path): Cesta k souboru
        encoding (str, optional): Encoding souboru. Defaults to 'utf-8'.

    Returns:
        Optional[str]: Obsah souboru nebo None při chybě
    """
    try:

        with file_path.open('r', encoding=encoding) as file:
            return file.read()

    except (IOError, PermissionError) as io_error:
        print(f"Chyba při čtení souboru: {io_error}")
        return None

    except Exception as e:
        print(f"Neočekávaná chyba při čtení souboru: {e}")
        return None


