from pathlib import Path
from typing import Union, Optional

from _system_access_error import SystemAccessError


def create_test_file(test_path) -> Optional:
    """Otestuje vytvoření testovacího souboru."""

    try:
        test_path.touch()
        return test_path

    except PermissionError:
        raise SystemAccessError(
            message="Nelze vytvořit soubor",
            detail=f"Nemáte oprávnění vytvořit soubor '{test_path}'.",
            hint="Zkontrolujte oprávnění k zápisu."
        )