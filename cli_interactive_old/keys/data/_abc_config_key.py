from abc import ABC, abstractmethod
from typing import Any, Dict, Union, Tuple

class ConfigKey(ABC):
    """Abstraktní základní třída pro konfigurační klíče"""

    # Třídní atributy které musí být definovány v potomcích
    INFO: str
    DEFAULT_VALUE: Union[int, str, bool]
    OPTIONS: Tuple[str, ...]
    HINT: Tuple[str, ...]
    VALUES_DICT: Dict[Union[int, str, bool], str]

    def __init__(self):
        """
        Inicializace konfiguračního klíče.
        Hodnoty jsou brány z třídních atributů.
        """
        self.default_value = self.DEFAULT_VALUE
        self.info = self.INFO
        self.options = self.OPTIONS
        self.hint = self.HINT
        self.values_dict = self.VALUES_DICT

    @abstractmethod
    def validate(self, value: Any) -> bool:
        """Validace hodnoty pro daný konfigurační klíč"""
        pass

