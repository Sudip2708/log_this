from pathlib import Path
from typing import Union, Optional

from _system_access_error import SystemAccessError


def verify_path_instance(path) -> Optional:
    """Ověří validitu cesty."""
    if isinstance(path, Path):
        return True

    else:
        raise SystemAccessError(
            message="Cesta není zapsaná jako Path instance",
            detail=f"Cesta '{path}' nemá formát platné cesty v systému.",
            hint="Pro použití cesty v rámci sitému je potřeba ji pčřevést na instanci Path."
        )