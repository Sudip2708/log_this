# print("_menus_settings/_key_and_value_config/config_value_select.py")

class ConfigValueSelect:

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.mm.selected_value = None
        selected_key = self.mm.selected_key.upper() if self.mm.selected_key else ""

        self.title = f"VYBERTE HODNOTU PRO {selected_key}:"
        self.items = [
            ("value_1", lambda: self.mm.set_value_and_print("value_1")),
            ("value_2", lambda: self.mm.set_value_and_print("value_2")),
            ("value_3", lambda: self.mm.set_value_and_print("value_3")),
            ("Zadat vlastní hodnotu", self.proxy_method),  #self.mm.input_custom_value),
            ("Zpět na výběr klíče", lambda: self.mm.show_menu("key_select_menu"))
        ]


    def proxy_method(self):
        pass