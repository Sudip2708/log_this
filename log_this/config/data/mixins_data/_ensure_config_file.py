import os
import json
from typing import Dict, Any

from ._read_config import read_config

def ensure_config_file(config_path: str, default_config: Dict[str, Any]) -> \
Dict[str, Any]:
    """
    Zajistí existenci konfiguračního souboru.

    Args:
        config_path: Cesta ke konfiguračnímu souboru
        default_config: Defaultní konfigurace

    Returns:
        Obsah konfiguračního souboru
    """
    if not os.path.exists(config_path):
        with open(config_path, 'w') as config_file:
            json.dump(default_config, config_file, indent=2)

    return read_config(config_path)


