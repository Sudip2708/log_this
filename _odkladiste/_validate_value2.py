from typing import Any


class ValidateValueMixin:

    @classmethod
    def _validate_value(
            cls,
            key: str,
            value: Any
    ) -> bool:
        """
        Validuje konfigurační hodnotu pro daný klíč.

        Nejprve zkontroluje, zda hodnota nespadá pod hodnoty s vlastní validací.
        Pokud ne, pak ověří její přítomnost v konfiguračním slovníku,
        a zda je hodnota v rozmezí 0 - 4.

        Args:
            key (str): Klíč konfigurace
            value (Any): Hodnota ke kontrole

        Returns:
            bool: Indikuje platnost hodnoty
        """

        # Pokud klíč odkazuje na nastavení zobrazení prázdných řádek mezi logy
        if key == 'blank_lines' and isinstance(value, bool):
            print("###### key == 'blank_lines'")
            return True

        # Pokud klíč odkazuje na nastavení zobrazení délky docstringu
        elif key == 'docstring_lines' and isinstance(value, int) or value == 'all':

            print("###### key == 'docstring_lines'")
            return True

        # Pokud klíč odkazuje na nastavení maximálního povoleného zanoření
        # (ochrana proti nekonečné rekurzy)
        elif key == 'max_depth' and isinstance(value, int):
            print("###### key == 'max_depth'")
            return True

        # Ve všech ostatních případech zkontroluj přítomnost klíče v defaultním slovníku
        # a zda hodnota obsahuje číslice mezi 0 a 4
        elif key in (
            'skip_this', 'one_line', 'simple', 'detailed','report',
            'true', 'false', 'none', 'empty', 'indent',
        ) and value in (0, 1, 2, 3, 4):
            print("### key in cls.DEFAULTS and value in (0, 1, 2, 3, 4)")
            return True

        # Pokud klíč není rospoznán
        print("### return False")
        return False

