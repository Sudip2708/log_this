from typing import Union

from ..errors import ValidateValueError, ValidateKeyError
from ..keys import KEYS_DATA


def validate_key(
        key: str
) -> None:
    """Validuje klíč."""

    # Check if the key exists in default dictionary
    if key not in KEYS_DATA.keys():
        raise ValidateKeyError(key, KEYS_DATA.keys())


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


def _validate_key_and_value(
        key: str,
        value: Union[int, str, bool]
) -> None:
    """
    Validates the configuration value for a given key.

    The method first checks if the key exists in the default dictionary.
    Then it verifies if the value has custom validation rules.
    If not, it checks if the value is present in the configuration dictionary
    and whether the value is in the range 0-4.

    Args:
        key (str): Configuration key
        value (Union[int, str, bool]): Value to validate

    Raises:
        ValidateKeyError: If key doesn't exist in defaults
        ValidateValueError: If value is invalid for given key
    """

    # Check if the key exists in default dictionary
    validate_key(key)

    # Validace hodnoty pro daný klíč
    validate_value(key, value)

