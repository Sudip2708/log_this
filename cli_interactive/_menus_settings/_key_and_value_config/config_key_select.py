# print("_menus_settings/_key_and_value_config/config_key_select.py")

class ConfigKeySelect:

    def __init__(self, menus_manager):

        menus_manager.selected_key = None
        self.mm = menus_manager
        self.title = "VYBERTE KLÍČ:"
        self.items = [
            ("key_1", lambda: self.mm.switch_to_set_key("key_1")),
            ("key_2", lambda: self.mm.switch_to_set_key("key_2")),
            ("key_3", lambda: self.mm.switch_to_set_key("key_3")),
            ("Zpět do konfiguračního menu", lambda: self.mm.show_menu("config_menu"))
        ]


