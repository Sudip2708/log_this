from ._reed_config_file import ReedConfigFileMixin
from ._save_config_to_file import SaveConfigToFileMixin


__all__ = [
    "ReedConfigFileMixin",  # Uloží konfiguraci do souboru ve formátu JSON.
    "SaveConfigToFileMixin",  # Aktualizuje hodnotu konfigurace a uloží ji.
]