from typing import Union

from ..errors import ValidateValueError
from ..keys import KEYS_DATA



def validate_value(
        key: str,
        value: Union[int, str, bool]
) -> None:
    """Validuje hodnotu pro daný klíč."""

    # Načtení validační funkce ze slovníku
    key_data = KEYS_DATA.get(key)

    # Validace hodnoty pro daný klíč
    if not key_data or not key_data.validate(value):
        raise ValidateValueError(key, value, key_data)
