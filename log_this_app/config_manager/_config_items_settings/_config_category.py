from enum import Enum

class ConfigCategory(Enum):
    """Třída definijící jednotlivé kategorie"""
    MODE_SETTINGS = "log_this mode refactoring"
    APPEARANCE = "log_this CLI appearance"
    INTERACTIVE_CLI = "Interactive CLI appearance"
    OTHERS = "Others"