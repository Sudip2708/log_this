from typing import Union


class KeyAndValueCheckMixin:


    @classmethod
    def _key_and_value_check(cls, key: str,
                             value: Union[int, str, bool]) -> None:
        """
        Ověří platnost klíče a hodnoty konfigurace.

        Metoda nejprve zkontroluje přítomnos klíče v defaultním slovníku
        Následně ověří platnost hodnoty.

        Args:
            key: Klíč konfigurace
            value: Hodnota konfigurace

        Raises:
            KeyError: Pokud klíč není v DEFAULTS
            ValueError: Pokud hodnota není validní
        """
        if key not in cls.DEFAULTS:
            raise KeyError(f"Neznámý klíč konfigurace: {key}")

        if not cls._validate_value(key, value):
            raise ValueError(f"Neplatná hodnota pro {key}: {value}")

