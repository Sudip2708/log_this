from pathlib import Path
from typing import Union, Optional

from _system_access_error import SystemAccessError


def validate_dir(path) -> Optional:
    """Ověří adresář cesty."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        return True

    except PermissionError:
        raise SystemAccessError(
            message="Nelze vytvořit adresář",
            detail=f"Nemáte oprávnění vytvořit adresář v '{path.parent}'.",
            hint="Zkontrolujte oprávnění nebo zvolte jinou cestu."
        )