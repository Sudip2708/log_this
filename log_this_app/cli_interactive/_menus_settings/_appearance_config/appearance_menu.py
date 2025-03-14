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
        self.mm.current_selection = styler.get_current_color_mode_id()
        self.mm.show_menu("select_colors_menu", target_reset=False)

    def show_select_symbols_menu(self):
        self.mm.current_selection = styler.get_current_symbol_mode_id()
        self.mm.show_menu("select_symbols_menu", target_reset=False)

