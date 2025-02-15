from prompt_toolkit.shortcuts import radiolist_dialog
from typing import Optional, Any

from keys import KEYS_DATA
# from log_this.manager.config.styler import dialog_style
# from pickers import input_int_value
# from ..exceptions import ExitInteractiveMode, ValueIsNotValid



def config_value_picker(key: str) -> Optional[Any]:
    """
    Zobrazí dialog pro zadání nové hodnoty.

    Args:
        key (str): Konfigurační klíč.

    Returns:
        Optional[Any]: Zadaná hodnota nebo None při zrušení.
    """

    # Načtení dat pro daný klíč
    key_data = KEYS_DATA[key]

    # Načtení klíčů a info textu pro podrobnosti k výběru
    values = [
        (value_key, f"{value_key} - {description}")
        for value_key, description in key_data.values_dict
    ]

    # # Přidání položky pro opuštění konfigurace
    # values.append(
    #     ('exit', 'Ukončit interaktivní režim')
    # )

    # Vytvoření pickeru
    result = radiolist_dialog(
        title=f"Výběr hodnoty pro konfigurační klíč '{key}':",
        text='(Pohybujte se šipkami a volbu potvrďte entrem.)',
        values=values,
        # style=dialog_style
    ).run()

    # # Kontrola zda nebyla vybraná položka pro zadání vstupu
    # if result == 'input':
    #     result = input_int_value()

    # # Kontrola zda nebylo vybrané ukončení interaktivního modu
    # if result == 'exit':
    #     raise ExitInteractiveMode("Opouštím proces změny konfigurace.")

    # Kontrola zda nebyla zmáčknutá klávesnice pro přerušení zadávání
    if result is None:
        raise KeyboardInterrupt

    # # Validace hodnoty
    # if not key_data.validate(result):
    #     raise ValueIsNotValid(key, result)

    return result




































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
