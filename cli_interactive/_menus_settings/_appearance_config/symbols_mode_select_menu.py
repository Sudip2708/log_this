# print("_menus_settings/_menus_config/menus_config_symbols_select.py")

class SymbolsModeSelectMenu:

    def proxy_method(self):
        pass

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.title = "VYBERTE BAREVNÝ MOD:"
        self.items = [
            ("Základní set symbolů", self.proxy_method()),
            ("Obrázkové symboly", self.proxy_method()),
            ("Bez zobrazovaných symbolů", self.proxy_method()),
            ("Zpět do předchozí nabídky", lambda: self.mm.show_menu("appearance_menu")),
            ("Ukončit", self.mm.exit_menu)
        ]

