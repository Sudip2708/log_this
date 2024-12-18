import json
from typing import Dict, Any

from ._config_constants import ConfigConstants


def read_config(config_path: str) -> Dict[str, Any]:
    """
    Přečte konfigurační soubor.

    Args:
        config_path: Cesta ke konfiguračnímu souboru

    Returns:
        Obsah konfiguračního souboru
    """
    try:
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    except json.JSONDecodeError:
        return ConfigConstants.DEFAULT_CONFIG


