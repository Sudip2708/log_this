# print("_menus_settings/_menus_config/menus_config_menu.py")

class AppearanceMenu:

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.title = "VYBERTE ÚKON:"
        self.items = [
            ("Nastavit barevný mod", self.show_select_colors_menu),
            ("Nastavit zobrazení značek", self.show_select_symbols_menu),
            ("Zpět do hlavního menu", lambda: self.mm.show_menu("main_menu")),
            ("Ukončit", self.mm.exit_menu)
        ]

    def show_select_colors_menu(self):
        self.mm.current_selection = self.mm.styler.get_current_color_mode_id()
        self.mm.show_menu("select_colors_menu", target_reset=False)

    def show_select_symbols_menu(self):
        self.mm.current_selection = self.mm.styler.get_current_symbol_mode_id()
        self.mm.show_menu("select_symbols_menu", target_reset=False)