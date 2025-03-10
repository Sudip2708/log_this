import logging
from typing import Dict
import atexit
from .mixins import (
    GetLoggerMixin,
    CreateFileHandlerMixin,
    AppLoggerMixin,
    CliLoggerMixin,
    CleanupMixin
)

class LogManager(
    CreateFileHandlerMixin,  # Třídní metoda pro vytvoření nového logeru a nebo navrácení existujícího
    GetLoggerMixin,  # Třídní metoda pro konfiguraci logování do souboru
    AppLoggerMixin,  # Třídní metoda pro konfiguraci loggeru LogThis
    CliLoggerMixin,  # Třídní metoda pro konfiguraci loggeru pro CLI konfigiraci
    CleanupMixin  # Třídní metoda pro smazání handlerů při ukončení aplikace
):
    """Třída pro správu loggerů s podporou Singleton patternu."""

    _instance = None
    _loggers: Dict[str, logging.Logger] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Registrace cleanup metody při první inicializaci
            atexit.register(cls.cleanup)
        return cls._instance

    def __init__(self):
        # Init se zavolá při každém vytvoření instance,
        # ale díky __new__ máme jistotu, že cleanup registrujeme jen jednou
        pass

# Definice logerrů
app_log = LogManager.app_logger()
cli_log = LogManager.cli_logger()



