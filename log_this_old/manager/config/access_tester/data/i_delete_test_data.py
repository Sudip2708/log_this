import json
from typing import Union, Optional

from _system_access_error import SystemAccessError


def delete_test_data(test_path) -> Optional:
    """Otestuje smazání souboru."""

    try:
        test_path.unlink()
        return True

    except PermissionError:
        raise SystemAccessError(
            message="Nelze smazat soubor",
            detail=f"Nemáte oprávnění smazat soubor '{test_path}'.",
            hint="Zkontrolujte oprávnění k mazání."
        )


