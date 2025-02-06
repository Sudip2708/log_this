from typing import Dict, Union
from pathlib import Path

from ..utils.read_config_file import read_config_file
from ..validations import validate_dict_format, validate_key, validate_value


def load_and_validate_config_file(
        config_path: Path
) -> Dict[str, Union[int, str, bool]]:
    """
    Načte a zvaliduje konfigurační soubor.

    Returns:
        Dict: Zvalidovaná konfigurace

    Raises:
        ReadConfigFileError: Výjimky vyvolané při načítání konfiguračního souboru
        ValidateDictFormatError: Výjimky vyvolané při ověření, že se jedná o slovník s daty
        ValidateKeyError: Výjimka vyvolana při ověření klíčů
        ValidateValueError: Výjimka vyvolana při ověření hodnot
    """

    # Načtení konfiguračního souboru
    config_dict = read_config_file(config_path)

    # Validace že se jedná o slovník s daty
    validate_dict_format(config_dict)

    # Rozebrání slovníku a validace dat
    for key, value in config_dict.items():
        validate_key(key)
        validate_value(key, value)

    # Navrácení zvalidovaného slovníku, nebo předání výjimky
    return config_dict

# Přidat kontrolu existence cesty