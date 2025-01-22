"""
Závislosti:
- read_config_file: Funkce pro načtení konfiguračního souboru
- _config_path: Atribut definující cestu ke konfiguračnímu souboru
- validate_dict_format: Funkce pro validaci zda se jedná o slovník
- _validate_key_and_value: Metoda pro kontrolu klíčů a hodnot konfiguračního slovníku
"""

from abc import ABC, abstractmethod
from typing import Dict, Union
from pathlib import Path

from ..utils.read_config_file import read_config_file
from ..utils.validate_dict_format import validate_dict_format


class LoadAndValidateConfigMixin(ABC):
    """Mixin metody pro načtení a validaci konfiguračního souboru"""

    @property
    @abstractmethod
    def _config_path(self) -> Path:
        """Atribut s cestou ke konfiguračnímu souboru."""
        pass

    @abstractmethod
    def _validate_key_and_value(self, key: str, value: Union[int, str, bool]) -> None:
        """Metoda načte a zvaliduje konfigurační soubor."""
        pass

    def _load_and_validate_config(
            self
    ) -> Dict[str, Union[int, str, bool]]:
        """
        Načte a zvaliduje konfigurační soubor.

        Returns:
            Dict: Zvalidovaná konfigurace

        Raises:
            ReadConfigFileError: Výjimky vyvolané při načítání konfiguračního souboru
            ValidateDictFormatError: Výjimky vyvolané při ověření, že se jedná o slovník s daty
            ValidateKeyError: Výjimka vyvolana při ověření klíčů
            ValidateValueError: Výjimka vyvolana při ověření hodnot
        """

        # Načtení konfiguračního souboru
        config_dict = read_config_file(self._config_path)

        # Validace že se jedná o slovník s daty
        validate_dict_format(config_dict)

        # Rozebrání slovníku a validace dat
        for key, value in config_dict.items():
            self._validate_key_and_value(key, value)

        # Navrácení zvalidovaného slovníku, nebo předání výjimky
        return config_dict