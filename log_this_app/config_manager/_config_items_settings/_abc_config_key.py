from abc import ABC, abstractmethod
from typing import Any, Dict, Union, Tuple

from ._config_category import ConfigCategory


class ConfigKey(ABC):
    """Abstraktní základní třída pro konfigurační klíče"""

    # Třídní atributy které musí být definovány v potomcích
    INFO: str
    DEFAULT_VALUE: Union[int, str, bool]
    OPTIONS: Tuple[str, ...]
    HINT: Tuple[str, ...]
    VALUES_DICT: Dict[Union[int, str, bool], str]
    CATEGORY: ConfigCategory

    def validate(self, value: Any) -> bool:
        """Výchozí validace: kontrola, zda je hodnota v `VALUES_DICT`."""
        return value in self.VALUES_DICT

