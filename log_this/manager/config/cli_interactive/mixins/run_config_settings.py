from abc import ABC, abstractmethod
from typing import Optional, Any

class RunConfigSettingsMixin(ABC):

    @abstractmethod
    def config_key_picker(self) -> Optional[str]:
        """Zobrazí menu pro výběr konfiguračního klíče."""
        pass

    @staticmethod
    @abstractmethod
    def _exit_interactive_mode(message: Optional[str] = None) -> None:
        """Ukončí interaktivní režim s volitelnou zprávou."""
        pass

    @abstractmethod
    def config_value_input(self, key: str) -> Optional[Any]:
        """Zobrazí dialog pro zadání nové hodnoty."""
        pass

    @property
    @abstractmethod
    def config_inst(self) -> Optional[Any]:
        """Atribut s instanci konfigurační třídy."""
        pass

    def run_config_settings(self) -> None:
        """Zpracuje proces změny konfigurace."""

        # Zobrazení menu pro výběr klíče
        key = self.config_key_picker()

        # Kontrola zda nebyla zmáčknutá klávesnice pro přerušení zadávání
        if not key:
            return

        # Kontrola zda nebylo vybrané ukončení interaktivního modu
        if key == 'exit':
            self._exit_interactive_mode("Opouštím proces změny konfigurace.")
            return

        # Zobrazení dialogu pro zadání hodnoty
        value = self.config_value_input(key)

        # Kontrola zda nebyla zmáčknutá klávesnice pro přerušení zadávání
        if value is None:
            return

        # Uložení do konfigurace (klíč a hodnota jsou již zvalidované)
        self.config_inst.set_new_value(key, value, vlaue_check=True)
