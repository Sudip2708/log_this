from abc import ABC, abstractmethod
from typing import Any, Union


class ConfigKey(ABC):
    """Abstraktní základní třída pro konfigurační klíče"""

    # Třídní atributy které musí být definovány v potomcích
    INFO: str
    DEFAULT_VALUE: Any
    DETAIL: str
    HINT: str

    def __init__(self):
        """
        Inicializace konfiguračního klíče.
        Hodnoty jsou brány z třídních atributů.
        """
        self.default_value = self.DEFAULT_VALUE
        self.info = self.INFO
        self.detail = self.DETAIL
        self.hint = self.HINT

    @abstractmethod
    def validate(self, value: Any) -> bool:
        """Validace hodnoty pro daný konfigurační klíč"""
        pass

