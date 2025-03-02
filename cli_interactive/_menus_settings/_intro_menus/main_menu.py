# print("_menus_settings/_menus_intro/main_menu.py")

class MainMenu:

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.title = "VYBERTE ÚKON:"
        self.items = [
            ("Nastavení vzhledu", lambda: self.mm.show_menu("appearance_menu")),
            ("Nápověda", self.mm.toggle_show_instruction),
            ("Zobrazit konfiguraci", self.proxy_method),  #self.mm.show_current_configuration),
            ("Nastavit konfiguraci", lambda: self.mm.show_menu("config_menu")),
            ("Ukončit", self.mm.exit_menu),
        ]


    def proxy_method(self):
        pass
