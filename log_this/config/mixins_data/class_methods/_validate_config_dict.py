import logging
from typing import Dict, Any


class ValidateConfigDictMixin:

    @classmethod
    def _validate_config_dict(cls, config: Dict[str, Any]) -> bool:
        """
        Metoda pro ověření klíčů a hodnot konfiguračního slovníku.

        Metoda nejprve ověří přítomnost klíče v defaultním slovníku.
        Následně ověří i správný formát hodnoty.

        Args:
            config (Dict[str, Any]): Konfigurace ke kontrole

        Returns:
            bool: Indikuje validitu celé konfigurace
        """

        # Cyklus rozebírající slovník na klíč a hodnotu
        for key, value in config.items():

            # Ověření klíče a hodnoty
            try:
                cls._key_and_value_check(key, value)

            # Zachycení chybného klíče
            except KeyError:
                logging.warning(f"Neplatný klíč: {key}")
                return False

            # Zachycení chybné hodnoty
            except (KeyError, ValueError):
                logging.warning(f"Neplatná hodnota pro klíč: {key}: {value}")
                return False

        # Pokud ověření proběhne bez chyb
        return True

