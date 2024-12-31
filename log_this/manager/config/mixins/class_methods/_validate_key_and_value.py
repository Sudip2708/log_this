import logging
from typing import Union


class ValidateKeyAndValueMixin:

    @classmethod
    def _validate_key_and_value(
            cls,
            key: str,
            value: Union[int, str, bool]
    ) -> bool:
        """
        Validuje konfigurační hodnotu pro daný klíč.

        Metoda nejprve zkontroluje přítomnos klíče v defaultním slovníku
        Následně ověří, zda hodnota nespadá pod hodnoty s vlastní validací.
        Pokud ne, pak ověří její přítomnost v konfiguračním slovníku,
        a zda je hodnota v rozmezí 0 - 4.

        Args:
            key (str): Klíč konfigurace
            value (Union): Hodnota ke kontrole

        Returns:
            bool: Indikuje platnost hodnoty
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

        # Pokud klíč odkazuje na nastavení zobrazení prázdných řádek mezi logy
        if key == 'blank_lines':
            if isinstance(value, bool):
                return True
            else:
                logging.error(
                    f"Neplatná hodnota pro klíč: {key}. "
                    f"Obdržená hodnota: {value}. "
                    f"Možnosti: True, False")
                return False

        # Pokud klíč odkazuje na nastavení zobrazení délky docstringu
        elif key == 'docstring_lines':
            if (value == 'all' or isinstance(value, int)
                    and not isinstance(value, bool) and value >= 0):
                return True
            else:
                logging.error(
                    f"Neplatná hodnota pro klíč: {key}. "
                    f"Obdržená hodnota: {value}. "
                    f"Možnosti: 0 - 1000, 'all'")
                return False

        # Pokud klíč odkazuje na nastavení maximálního povoleného zanoření
        # (ochrana proti nekonečné rekurzy)
        elif key == 'max_depth':
            if (isinstance(value, int) and not isinstance(value, bool)
                    and value >= 0):
                return True
            else:
                logging.error(
                    f"Neplatná hodnota pro klíč: {key}. "
                    f"Obdržená hodnota: {value}. "
                    f"Možnosti: 0 - 1000")
                return False

        # Ve všech ostatních případech zkontroluj přítomnost klíče v defaultním slovníku
        # a zda hodnota obsahuje číslice mezi 0 a 4
        else:
            if value in (0, 1, 2, 3, 4) and not isinstance(value, bool):
                return True
            else:
                logging.error(
                    f"Neplatná hodnota pro klíč: {key}. "
                    f"Obdržená hodnota: {value}. "
                    f"Možnosti: 0 - 4")
                return False




