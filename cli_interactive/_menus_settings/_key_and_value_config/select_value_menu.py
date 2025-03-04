# print("_menus_settings/_key_and_value_config/config_value_select.py")
# from ._input_int_value import input_int_value

class SelectValueMenu:

    def __init__(self, menus_manager):

        self.mm = menus_manager
        self.mm.selected_value = None

        self.title = self.get_title()
        self.items = [
            ("value_1", lambda: self.set_value_and_print("value_1")),
            ("value_2", lambda: self.set_value_and_print("value_2")),
            ("value_3", lambda: self.set_value_and_print("value_3")),
            ("Zadat vlastní hodnotu", self.input_custom_int_value),
            ("Zpět na výběr klíče", self.show_key_select_menu)
        ]

    def get_title(self):
        if not self.mm.selected_key:
            raise ValueError("Není zadán klíč, pro který se má zadat hodnota")
        return f"VYBERTE HODNOTU PRO {self.mm.selected_key.upper()}:"

    # Metoda pro uložení a vytisknutí vybraného klíče a hodnoty
    def set_value_and_print(self, value):
        self.mm.selected_value = value
        self.mm.response = "print_new_settings"
        self.mm.exit_menu()

    # # Metoda pro zadání celočíselné hodnoty (rozmezí 1 - 1000)
    # def input_custom_int_value(self):
    #     self.mm.selected_value = input_int_value(self.mm)
    #     self.mm.response = "print_new_settings"
    #     self.mm.exit_menu()

    # Metoda pro zadání celočíselné hodnoty (rozmezí 1 - 1000)
    def input_custom_int_value(self):
        self.mm.response = "input_int_value"
        self.mm.exit_menu()


    # Metoda pro přepnutí na konfigurační menu
    def show_key_select_menu(self):
        self.mm.show_menu("select_key_menu")
