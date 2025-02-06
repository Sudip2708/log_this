from pathlib import Path
from typing import Union, Optional

from _system_access_error import SystemAccessError


def validate_path(path) -> Optional:
    """Ověří validitu cesty."""
    try:
        path = Path(path).resolve(strict=False)
        return True

    except RuntimeError:
        raise SystemAccessError(
            message="Neplatná cesta",
            detail=f"Cesta '{path}' nemá formát platné cesty v systému.",
            hint="Zkontrolujte, zda cesta neobsahuje nepovolené znaky."
        )