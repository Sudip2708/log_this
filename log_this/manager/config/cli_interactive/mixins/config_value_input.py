from abc import ABC, abstractmethod
from webbrowser import Error

from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.styles import Style
from typing import Optional, Any

class ConfigValueInputMixin(ABC):

    @property
    @abstractmethod
    def keys_data(self) -> dict[str, Any]:
        """Atribut pro přístup k instancím klíčů ."""
        pass

    @property
    @abstractmethod
    def config_inst(self) -> Any:
        """Atribut s instancí konfigurace."""
        pass

    @property
    @abstractmethod
    def style(self) -> Style:
        """Atribut s nastavením stylu vzhledu."""
        pass

    @abstractmethod
    def config_value_input(self, key: str) -> Optional[Any]:
        """Zobrazí dialog pro zadání nové hodnoty."""
        pass

    def _convert_value(self, key: str) -> Optional[Any]:
        """
        Zobrazí dialog pro zadání nové hodnoty.

        Args:
            key (str): Konfigurační klíč.

        Returns:
            Optional[Any]: Zadaná hodnota nebo None při zrušení.
        """

        key_data = self.keys_data[key]
        current_value = self.config_inst.config[key]

        while True:
            # Vytvoření úvodní zprávy s nápovědou
            help_text = (
                f"Nápověda:\n{key_data.hint}\n\n"
                f"Možnosti:\n{key_data.options}\n\n"
                f"Aktuální hodnota: {current_value}\n"
                f"Výchozí hodnota: {key_data.default_value}\n\n"
                f"Zadejte novou hodnotu:"
            )

            # Vytvoření inputu
            result = input_dialog(
                title=f'Nastavení hodnoty pro {key}',
                text=help_text,
                style=self.style
            ).run()

            # Pokud uživatel zruší dialog
            if not result:
                return None

            # Pokus o převod hodnoty
            value = self._convert_value(result)

            # Kontrola, zda nebyla zadaná již existující hodnota
            if value == current_value:
                print(f"\nThe configuration key '{key}' is already set to '{value}'. \n"
                      f"Žádná změna nebyla učiněna. \n")
                return None

            # Validace hodnoty
            if key_data.validate(value):
                return value
            else:
                print(f"\nNeplatná hodnota: '{result}'. Zkuste to znovu.\n")
