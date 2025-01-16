import logging
from typing import Dict, Any


class ValidateConfigDictMixin:

    @classmethod
    def _validate_config_dict(
            cls,
            config: Dict[str, Any]
    ) -> bool:
        """
        Metoda pro ověření klíčů a hodnot konfiguračního slovníku.

        Metoda nejprve ověří přítomnost klíče v defaultním slovníku.
        Následně ověří i správný formát hodnoty.

        Args:
            config (Dict[str, Any]): Konfigurace ke kontrole

        Returns:
            bool: Indikuje validitu celé konfigurace
        """

        # Ověření, že se jedná o slovník:
        if not isinstance(config, dict):
            logging.error(
                f"Error while validate config dict: "
                f"The configuration dictionary is not 'dict' type. "
                f"Detected type: {type(config)}"
            )
            return False

        # Ověření že slovník není prázdný
        if not config:
            logging.error(
                f"Error while validate config dict: "
                f"The configuration dictionary is empty."
            )
            return False

        # Cyklus rozebírající slovník na klíč a hodnotu
        for key, value in config.items():

            # Kontrola klíče a hodnoty
            if not cls._validate_key_and_value(key, value):
                logging.error(
                    f"Error while validate config dict: "
                    f"The configuration dictionary does not contain valid data."
                )
                return False

        # Pokud ověření proběhne bez chyb
        logging.debug(
            f"Success with validate config dict: "
            f"The configuration dictionary has been checked "
            f"and contains valid data."
        )
        return True


