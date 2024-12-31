import logging
from typing import Union


class KeyAndValueCheckMixin:
    """
    Závislosti:
        cls.DEFAULTS: (dict): Slovník obsahující defaultní konfiguraci
        cls._validate_value(key, value): Třídní metoda pro validci hodnot.
    """


    @classmethod
    def _key_and_value_check(
            cls,
            key: str,
            value: Union[int, str, bool]
    ) -> Bool:
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

        # Pokud klíč není mezi klíči defaultního slovníku
        if key not in cls.DEFAULTS:
            options = list(cls.DEFAULTS.keys())
            logging.error(
                f"Neplatný klíč: {key}. "
                f"Klíč není součástí defaultní konfigurace. "
                f"Možnosti: {options}"
            )
            return False

        # Pokud hodnota pro daný klíč neprojde validací
        if not cls._validate_value(key, value):
            # log vypisuje metoda _validate_value()
            return False

        # Ve všech ostatních případech
        return True


