import json
from typing import Union, Optional

from _system_access_error import SystemAccessError


def write_test_data(test_path, test_data) -> Optional:
    """Otestuje zápis dat."""

    try:
        with test_path.open('w', encoding='utf-8') as f:
            json.dump(test_data, f)
        return test_path

    except PermissionError:
        raise SystemAccessError(
            message="Nelze zapisovat do souboru",
            detail=f"Nemáte oprávnění zapisovat do '{test_file}'.",
            hint="Zkontrolujte oprávnění k zápisu."
        )

