# print("_response_manager/response_manager.py")
from ._input_int_value import input_int_value

from cli_styler import styler

class ResponseManager:
    """Spravuje reakce na vybrané položky menu"""

    def __init__(self, menus_manager):

        # Přiřazení instance hlavní třídy
        self.mm = menus_manager

        # Definice akcí odezvy
        self.response_actions = {
            "print_configuration": self.print_configuration,
            "print_new_settings": self.print_new_settings,
            "input_int_value": self.input_int_value,
        }

    def __call__(self):
        """Vrací výstupní reakci na daný požadavek"""
        action = self.response_actions.get(self.mm.response)
        if action:
            action()
            self.mm.response = "exit_menu"  # Nastavení zobrazení exut menu


    def print_configuration(self):
        styler.cli_print.success.title("Aktuální konfigurace:")
        styler.cli_print.success.text("key1: value1")
        styler.cli_print.success.text("key2: value2")
        print()


    def print_new_settings(self):
        """Tiskne aktuálně změněnou hodnotu"""

        # Načtení klíče
        key = self.mm.selected_key
        value = self.mm.selected_value

        # Ověření že došlo ke změně:
        if self.mm.config_manager.config.get(key) == value:

            # Načtení třídy klíče
            key_class = self.mm.config_manager.items_manager.KEYS_DATA.get(key)
            # Získání textové reprezentace hodnoty
            value_str = key_class.VALUES_DICT.get(value)
            # Výpis o změně
            styler.cli_print.success.title(
                f"Klíč '{key}', "
                f"byl nastaven na '{value_str}'"
            )
            print()

        else:
            print("Změnu se nepovvedlo provést. Klíč obsahuje hodnotu. Zkuste to znovu.")

        # Reset hodnot
        self.mm.selected_key = None
        self.mm.selected_value = None


    def input_int_value(self):
        self.mm.selected_value = input_int_value(self.mm)
        # Pokud nebyla zadána žádná hodnota, vrací se None
        if self.mm.selected_value:
            self.print_new_settings()


