import json
from pathlib import Path
from typing import Any, Dict

from ._create_file import create_file


def create_json_file(
        file_path: Path,
        data: Dict[str, Any]
) -> bool:
    """
    Vytvoří JSON soubor s daným obsahem.

    Args:
        file_path (Path): Cesta pro uložení souboru
        data (Dict[str, Any]): Konfigurační data k uložení

    Returns:
        bool: Zda se podařilo soubor úspěšně vytvořit
    """
    try:
        # Serializace je součástí funkce
        json_content = json.dumps(data, indent=4, ensure_ascii=False)
        return create_file(file_path, json_content)

    except (TypeError, OverflowError) as serialize_error:
        print(f"Chyba při serializaci JSON dat: {serialize_error}")
        return False

    except Exception as e:
        print(f"Neočekávaná chyba při ukládání JSON souboru: {e}")
        return False