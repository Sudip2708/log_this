from typing import Dict, Union
from .keys_data_dict import KEYS_DATA

def allowed_keys_with_descriptions() -> list:
    """Vrátí seznam povolených klíčů s popisem."""
    outcome = []
    for key, config_key in KEYS_DATA.items():
        outcome.append(f"'{key}' - {config_key.info}")
    return outcome
