from typing import Union

from .validate_key import validate_key
from .validate_value import validate_value


def validate_key_and_value(
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

