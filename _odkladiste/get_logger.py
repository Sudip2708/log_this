from ._logger_settings import logger_settings


def get_logger():
    """
    Hlavní funkce pro získání vlákna.
    """
    return logger_settings()
