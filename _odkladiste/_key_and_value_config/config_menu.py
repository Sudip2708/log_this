# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial
from .._base_menu import BaseMenu

class ConfigMenu(BaseMenu):

    # Definice nadpisu
    title = "VYBERTE ÚKON:"

    # Definice položek
    @property
    def items(self):

        # Reset používaných atributů
        self.mm.selected_key = None
        self.mm.selected_value = None


        # Definice položek
        items = [
            ("• Nastavit chování módů", self.show_modes_settings_menu),
            ("• Nastavit výstup", self.show_aspects_settings_menu),
        ]

        # Přidání doplňujících položek
        items += [
            ("Zpět do hlavního menu", self.mm.show_main_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items


    # Metoda pro nastavení nové hodnoty
    def show_modes_settings_menu(self):
        self.mm.menus_category = "log_this_modes"
        self.mm.show_menu("select_key_menu")


    # Metoda pro nastavení nové hodnoty
    def show_aspects_settings_menu(self):
        self.mm.menus_category = "log_this_aspects"
        self.mm.show_menu("select_key_menu")
