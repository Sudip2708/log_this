from ._read_config_file import ReadConfigFileMixin
from ._save_config_to_file import SaveConfigToFileMixin


__all__ = [
    "ReadConfigFileMixin",  # Uloží konfiguraci do souboru ve formátu JSON.
    "SaveConfigToFileMixin",  # Aktualizuje hodnotu konfigurace a uloží ji.
]