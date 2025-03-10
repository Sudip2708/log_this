from pathlib import Path
from typing import Any

def create_file(
        file_path: Path,
        content: Any,
        mode: str = 'w',
        encoding: str = 'utf-8'
) -> bool:
    """
    Vytvoří soubor s daným obsahem na zadané cestě.

    Args:
        file_path (Path): Cesta pro uložení souboru
        content (Any): Obsah, který bude uložen do souboru
        mode (str, optional): Mód otevření souboru. Defaults to 'w'.
        encoding (str, optional): Encoding souboru. Defaults to 'utf-8'.

    Returns:
        bool: Zda se podařilo soubor úspěšně vytvořit
    """
    try:
        with file_path.open(mode, encoding=encoding) as file:
            file.write(content)
        return True

    except (IOError, PermissionError) as io_error:
        print(f"Chyba při ukládání souboru: {io_error}")
        return False

    except Exception as e:
        print(f"Neočekávaná chyba při ukládání souboru: {e}")
        return False