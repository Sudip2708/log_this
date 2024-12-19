from .data import LogThisConfig


def get_config():
    """
    Hlavní funkce pro získání singleton instance konfigurace.

    Returns:
        LTConfig: Instance konfigurace
    """
    return LogThisConfig()
