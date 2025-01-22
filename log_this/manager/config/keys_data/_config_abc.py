from abc import ABC, abstractmethod
from typing import Any


class ConfigKey(ABC):
    """Abstraktní základní třída pro konfigurační klíče"""

    # Třídní atributy které musí být definovány v potomcích
    INFO: str
    DEFAULT_VALUE: Any
    OPTIONS: str
    HINT: str

    def __init__(self):
        """
        Inicializace konfiguračního klíče.
        Hodnoty jsou brány z třídních atributů.
        """
        self.default_value = self.DEFAULT_VALUE
        self.info = self.INFO
        self.options = self.OPTIONS
        self.hint = self.HINT

    @abstractmethod
    def validate(self, value: Any) -> bool:
        """Validace hodnoty pro daný konfigurační klíč"""
        pass

