# print("_menus_settings/_menus_config/menus_config_menu.py")

class AppearanceConfigMenu:

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.title = "VYBERTE ÚKON:"
        self.items = [
            ("Nastavit barevný mod", lambda: self.mm.show_menu("colors_select_menu")),
            ("Nastavit zobrazení značek", lambda: self.mm.show_menu("symbols_select_menu")),
            ("Zpět do hlavního menu", lambda: self.mm.show_menu("main_menu")),
            ("Ukončit", self.mm.exit_menu)
        ]


