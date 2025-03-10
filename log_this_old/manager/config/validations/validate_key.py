from ..errors import ValidateKeyError
from ..keys import KEYS_DATA


def validate_key(
        key: str
) -> None:
    """Validuje klíč."""

    # Check if the key exists in default dictionary
    if key not in KEYS_DATA.keys():
        raise ValidateKeyError(key)

