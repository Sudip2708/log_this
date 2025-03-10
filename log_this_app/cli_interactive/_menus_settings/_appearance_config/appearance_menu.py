# print("_menus_settings/_menus_config/menus_config_menu.py")

from cli_styler import styler

class AppearanceMenu:

    def __init__(self, menus_manager):

        # Navázání instance menus managera
        self.mm = menus_manager

        # Definice nadpisu
        self.title = "VYBERTE ÚKON:"

        # Definice položek
        self.items = [
            ("Nastavit barevný mod", self.show_select_colors_menu),
            ("Nastavit zobrazení značek", self.show_select_symbols_menu),
        ]

        # Přidání doplňujících položek
        self.items += [
            ("Zpět do hlavního menu", self.mm.show_main_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

    def show_select_colors_menu(self):
        self.mm.current_selection = styler.get_current_color_mode_id()
        self.mm.show_menu("select_colors_menu", target_reset=False)

    def show_select_symbols_menu(self):
        self.mm.current_selection = styler.get_current_symbol_mode_id()
        self.mm.show_menu("select_symbols_menu", target_reset=False)

