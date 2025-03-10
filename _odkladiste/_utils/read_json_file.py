import json
from pathlib import Path
from typing import Any, Optional, Dict

from ._load_file_content import _load_file_content


def read_json_file(
        file_path: Path
) -> Optional[Dict[str, Any]]:
    """
    Přečte a zparsuje JSON soubor.

    Args:
        file_path (Path): Cesta k JSON souboru

    Returns:
        Optional[Dict[str, Any]]: Načtená JSON data nebo None při chybě
    """
    try:
        content = _load_file_content(file_path)
        if content is None:
            return None

        return json.loads(content)

    except json.JSONDecodeError as json_error:
        print(f"Chyba při parsování JSON: {json_error}")
        return None

    except Exception as e:
        print(f"Neočekávaná chyba při čtení JSON souboru: {e}")
        return None