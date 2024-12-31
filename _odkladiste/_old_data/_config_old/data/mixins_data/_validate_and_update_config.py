from typing import Dict, Any
from ._validate_value import validate_value


def validate_and_update_config(
        config_data: Dict[str, Any],
        default_config: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Validuje a aktualizuje konfiguraci.

    Args:
        config_data: Načtená konfigurace
        default_config: Defaultní konfigurace

    Returns:
        Validovaná konfigurace
    """
    updated_config = {}
    for key, default_value in default_config.items():
        value = config_data.get(key, default_value)
        updated_config[key] = validate_value(value, default_value, key)

    return updated_config

