from typing import Any

class ValidateAndSaveMixin:

    def _validate_and_save(self, key: str, value: Any) -> bool:
        """
        Validuje a uloží novou hodnotu.

        Args:
            key: Konfigurační klíč
            value: Nová hodnota

        Returns:
            bool: True pokud byla hodnota úspěšně uložena
        """
        if self.keys_data[key].validate(value):
            self.config_inst.config[key] = value
            return True

        print(f"\nChyba: Neplatná hodnota pro klíč '{key}'")
        print(f"Detail: {self.keys_data[key].DETAIL}")
        return False