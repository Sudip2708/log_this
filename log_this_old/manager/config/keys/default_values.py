from typing import Dict, Union
from .keys_data_dict import KEYS_DATA

def default_values() -> Dict[str, Union[int, str, bool]]:
    """Vrátí slovník s výchozími hodnotami konfigurace."""
    return {
        key: config_key.default_value
        for key, config_key in KEYS_DATA.items()
    }