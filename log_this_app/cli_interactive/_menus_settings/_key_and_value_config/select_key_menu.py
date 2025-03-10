# print("_menus_settings/_key_and_value_config/config_key_select.py")

class SelectKeyMenu:

    def __init__(self, menus_manager):

        # Navázání instance menus managera
        self.mm = menus_manager

        # Reset používaných atributů
        self.mm.selected_key = None

        # Definice nadpisu
        self.title = "VYBERTE KLÍČ:"


        # Definice položek
        self.items = [
            ("key_1", self.switch_to_set_key2),
            ("key_2", lambda: self.switch_to_set_key("key_2")),
            ("key_3", lambda: self.switch_to_set_key("key_3")),
        ]

        # Přidání doplňujících položek
        self.items += [
            ("Zpět do konfiguračního menu", self.show_config_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]


    def switch_to_set_key2(self):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        self.mm.selected_key = "key_1"
        self.mm.show_menu("select_value_menu")


    def switch_to_set_key(self, key):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        self.mm.selected_key = key
        self.mm.show_menu("select_value_menu")


    # Metoda pro přepnutí na konfigurační menu
    def show_config_menu(self):
        self.mm.show_menu("config_menu")