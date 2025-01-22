from abc import ABC, abstractmethod
from typing import Any
from ..singleton_meta import SingletonMeta


class ConfigKey(ABC, metaclass=SingletonMeta):
    """Abstraktní základní třída pro konfigurační klíče"""

    # Třídní atributy, které musí být definovány v potomcích
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
        self._actual_value = self.DEFAULT_VALUE  # Privátní atribut pro aktuální hodnotu

    @property
    def actual_value(self) -> Any:
        """Vrací aktuální hodnotu klíče."""
        return self._actual_value

    @actual_value.setter
    def actual_value(self, value: Any):
        """
        Nastavuje aktuální hodnotu klíče.
        Před nastavením ověřuje hodnotu pomocí metody `validate()`.
        """
        if self.validate(value):
            self._actual_value = value
        else:
            raise ValueError(
                f"Invalid value: {value}. "
                f"Key {self.__class__.__name__} accepts only valid values."
            )

    @abstractmethod
    def validate(self, value: Any) -> bool:
        """Validace hodnoty pro daný konfigurační klíč."""
        pass
