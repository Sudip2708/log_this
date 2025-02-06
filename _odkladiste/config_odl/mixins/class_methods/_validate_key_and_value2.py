from typing import Union
from log_this.manager.config.cli.raise_with_extra import raise_with_extra
from .key_hint import key_hint

class CLIValueError(ValueError):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, key: str, value: Union[int, str, bool], key_data: dict):
        # Inicializace základní výjimky
        message = f"Pro klíč '{key}' byla zadaná neplatná hodnota: '{value}'."
        super().__init__(message)

        # Přidání extra informací o klíči pro CLI logging
        self.extra = {
            "detail": key_data.get("detail", ""),
            "hint": key_data.get("hint", "")
        }

        # Nastavení extra atributu pro výjimku
        self.key = key
        self.value = value


class CLIKeyError(KeyError):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, key: str, defaults: list[str]):
        # Inicializace základní výjimky
        message = f"Byl zadán neplatný klíč: '{key}'."
        super().__init__(message)

        # Přidání extra informací o klíči pro CLI logging
        self.extra = {
            "detail": f"Zde je seznam povolených klíčů: \n{defaults}",
            "hint": f"Pro zobrazení seznamu klíčů i s popisem a nápovědou zadej v terminálu: \n"
                    f"$ log-this-config --help -key"
        }

        # Nastavení extra atributu pro výjimku
        self.key = key
        self.value = value


class ValidateKeyAndValueMixin:


    @classmethod
    def _validate_key_and_value(
            cls,
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
            KeyError: If key doesn't exist in defaults
            ValueError: If value is invalid for given key
        """

        # Check if the key exists in default dictionary
        if key not in key_hint:
            raise CLIKeyError(key, list(key_hint.keys()))

        # Načtení dat ze slovníku
        key_data = key_hint[key]
        validate_func = key_data.get("validate", None)

        # validace hodnoty pro daný klíč
        if not validate_func(value):
            raise CLIValueError(key, value, key_data)

