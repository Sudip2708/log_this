# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial

from .._base_menu import BaseMenu

class ModesConfigMenu(BaseMenu):

    # Definice nadpisu
    title = "VYBERTE ÚKON:"

    # Definice položek
    @property
    def items(self):

        # Reset používaných atributů
        self.mm.selected_key = None
        self.mm.selected_value = None

        # Získání jednotlivých sekcí
        modes = self.get_keys_and_labels("log_this_modes")

        # Dynamická definice položek menu
        items = [
            ("• "+label, partial(self.set_new_value, key))
            for key, label in modes.items()
        ]

        # Přidání doplňujících položek
        items += [
            ("Zpět do hlavního menu", self.mm.show_main_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items

    # Metoda pro nastavení novoé hodnoty
    def set_new_value(self, key):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        self.mm.selected_key = key
        self.mm.show_menu("select_value_menu")


    def get_keys_and_labels(self, category):
        """Metoda získá z hlavního slovníku klíč a label"""
        keys_data = self.mm.config_manager.items_manager.KEYS_DATA
        return {
            key: key_class.LABEL
            for key, key_class in keys_data.items()
            if key_class.CATEGORY == category
        }



