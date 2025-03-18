# print("_menus_settings/_menus_config/menus_config_menu.py")

from cli_styler import styler
from .._base_menu import BaseMenu

class AppearanceMenu(BaseMenu):

    # Definice nadpisu
    title = "VYBERTE ÚKON:"

    # Definice položek
    @property
    def items(self):

        # Definice položek
        items = [
            ("Nastavit barevný mod", self.show_select_colors_menu),
            ("Nastavit zobrazení značek", self.show_select_symbols_menu),
        ]

        # Přidání doplňujících položek
        items += [
            ("Zpět do hlavního menu", self.mm.show_main_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items



    def show_select_colors_menu(self):
        self.mm.selected_key = "colors"
        self.mm.show_menu("select_value_menu")

    def show_select_symbols_menu(self):
        self.mm.selected_key = "symbols"
        self.mm.show_menu("select_value_menu")

