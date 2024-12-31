from ._config_base import LogThisConfig


def get_config():
    """
    Hlavní funkce pro získání singleton instance konfigurace.

    Returns:
        LogThisConfig: Instance konfigurace
    """
    return LogThisConfig()


