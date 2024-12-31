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

        #Ověření, že se jedná o slovník a není prázdný:
        if isinstance(config, dict) and config:

            # Cyklus rozebírající slovník na klíč a hodnotu
            for key, value in config.items():

                # Pokud klíč nebo hodnota neprojdou validací
                if not cls._validate_key_and_value(key, value):
                    return False

            # Pokud ověření proběhne bez chyb
            return True

        # Pokud není slovník a nebo je prázdný
        return False

