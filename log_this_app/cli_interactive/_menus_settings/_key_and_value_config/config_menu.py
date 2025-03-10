# print("_menus_settings/_key_and_value_config/config_menu.py")

class ConfigMenu:

    def __init__(self, menus_manager):

        # Navázání instance menus managera
        self.mm = menus_manager

        # Reset používaných atributů
        self.mm.selected_key = None
        self.mm.selected_value = None

        # Definice nadpisu
        self.title = "VYBERTE ÚKON:"


        # Definice položek
        self.items = [
            ("Nastavit novou hodnotu", self.set_new_value),
            ("Nastavit hodnotu 2", self.proxy_method),
            ("Nastavit hodnotu 3", self.proxy_method),
        ]

        # Přidání doplňujících položek
        self.items += [
            ("Zpět do hlavního menu", self.mm.show_main_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]


    # Metoda pro nastavení novoé hodnoty
    def set_new_value(self):
        self.mm.show_menu("select_key_menu")


    def proxy_method(self):
        pass
