# print("_menus_settings/_menus_config/menus_config_colors_select.py")
from cli_styler import set_colors_mode


class ColorsModeSelectMenu:

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.title = "VYBERTE BAREVNÝ MOD:"
        self.items = [
            ("Mod pro tmavý režim", lambda: self.colors_mode_settings("dark")),
            ("Mod pro světlý režimk", lambda: self.colors_mode_settings("light")),
            ("Bez barev (nativní vzhled)", lambda: self.colors_mode_settings("native")),
            ("Zpět do předchozí nabídky", lambda: self.mm.show_menu("appearance_menu")),
            ("Ukončit", self.mm.exit_menu)
        ]

    def colors_mode_settings(self, color_mode):
        set_colors_mode(color_mode)
        self.mm.show_menu("colors_select_menu")






