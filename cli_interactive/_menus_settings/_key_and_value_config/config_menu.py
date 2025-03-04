# print("_menus_settings/_key_and_value_config/config_menu.py")

class ConfigMenu:

    def __init__(self, menus_manager):

        self.mm = menus_manager
        self.mm.selected_key = None
        self.mm.selected_value = None

        self.title = "VYBERTE ÚKON:"
        self.items = [
            ("Nastavit novou hodnotu", self.set_new_value),
            ("Nastavit hodnotu 2", self.proxy_method),
            ("Nastavit hodnotu 3", self.proxy_method),
            ("Zpět do hlavního menu", self.show_main_menu)
        ]

    # Nastavit novou hodnotu
    def set_new_value(self):
        self.mm.show_menu("select_key_menu")

    # Metoda pro přepnutí na hlavní menu
    def show_main_menu(self):
        self.mm.show_menu("main_menu")


    def proxy_method(self):
        pass
