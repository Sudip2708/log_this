# print("_menus_settings/_key_and_value_config/config_menu.py")

class ConfigMenu:

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.title = "VYBERTE ÚKON:"
        self.items = [
            ("Nastavit hodnotu 1", lambda: self.mm.show_menu("key_select_menu")),
            ("Nastavit hodnotu 2", self.proxy_method),
            ("Nastavit hodnotu 3", self.proxy_method),
            ("Zpět do hlavního menu", lambda: self.mm.show_menu("main_menu"))
        ]


    def proxy_method(self):
        pass
