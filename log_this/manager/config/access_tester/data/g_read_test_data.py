import json
from typing import Union, Optional

from _system_access_error import SystemAccessError


def read_test_data(test_path) -> Optional:
    """Otestuje čtení dat."""

    try:
        with test_path.open('r', encoding='utf-8') as f:
            read_data = json.load(f)
        return read_data

    except PermissionError:
        raise SystemAccessError(
            message="Nelze číst data",
            detail=f"Problém při čtení souboru '{test_path}'.",
            hint="Zkontrolujte oprávnění ke čtení."
        )


