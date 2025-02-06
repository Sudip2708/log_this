"""
Závislosti:
- valid_keys: Property vracející všechny klíče slovníku keys_data
- keys_data: Atribut obsahující slovník klíčů a navázaných datových tříd
"""

from abc import ABC, abstractmethod
from typing import Union, Set, Dict

from ..keys_data_mixins import ConfigKey
from ..errors import ValidateValueError, ValidateKeyError


class ValidateKeyAndValueMixin(ABC):
    """Mixin metody pro validaci klíče a hodnoty"""

    @property
    @abstractmethod
    def valid_keys(self) -> Set[str]:
        """Property s množinou platných klíčů."""
        pass

    @property
    @abstractmethod
    def keys_data(self) -> Dict[str, ConfigKey]:
        """Atribut slovníku pro třídu s daty pro dané klíče konfigurace."""
        pass

    def validate_key(self, key: str) -> None:
        """Validuje klíč."""
        # Check if the key exists in default dictionary
        if key not in self.valid_keys:
            raise ValidateKeyError(key, self.valid_keys)

    def validate_value(self, key: str, value: Union[int, str, bool]) -> None:
        """Validuje hodnotu pro daný klíč."""
        # Načtení validační funkce ze slovníku
        key_data = self.keys_data[key]
        # Validace hodnoty pro daný klíč
        if not key_data.validate(value):
            raise ValidateValueError(key, value, key_data)

    def _validate_key_and_value(
            self,
            key: str,
            value: Union[int, str, bool]
    ) -> None:
        """
        Validates the configuration value for a given key.

        The method first checks if the key exists in the default dictionary.
        Then it verifies if the value has custom validation rules.
        If not, it checks if the value is present in the configuration dictionary
        and whether the value is in the range 0-4.

        Args:
            key (str): Configuration key
            value (Union[int, str, bool]): Value to validate

        Raises:
            ValidateKeyError: If key doesn't exist in defaults
            ValidateValueError: If value is invalid for given key
        """

        # Check if the key exists in default dictionary
        self.validate_key(key)

        # Validace hodnoty pro daný klíč
        self.validate_value(key, value)

