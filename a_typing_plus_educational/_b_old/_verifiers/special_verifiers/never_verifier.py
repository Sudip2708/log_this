from typing import Any

from ..._exceptions import NeverValueError


def never_verifier(value: Any, bool_only: bool = False) -> bool:
    """
    Ověřuje, že hodnota je typu Never – což není nikdy možné.

    Args:
        value (Any): Hodnota, která nemá nikdy existovat.
        bool_only (bool): Pokud je True, vrací jen False bez výjimky.

    Returns:
        bool: False – hodnota nemůže být typu Never.

    Raises:
        NeverValueError: Pokud bool_only=False, vyvolá informativní výjimku.
    """
    if bool_only:
        return False
    raise NeverValueError(value)
