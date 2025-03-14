# print("_menus_settings/_key_and_value_config/config_value_select.py")
# from ._input_int_value import input_int_value
from .._base_menu import BaseMenu
from functools import partial

class SelectModeValueMenu(BaseMenu):


    # Definice nadpisu
    @property
    def title(self):
        if not self.mm.selected_key:
            raise ValueError("Není zadán klíč, pro který se má zadat hodnota")
        return f"VYBERTE HODNOTU PRO {self.mm.selected_key.upper()}:"

    # Definice položek
    @property
    def items(self):

        # Nápověda k této sekci
        items = [
            (f"Zobrazit nápovědu pro {self.mm.selected_key}", self.show_help),
        ]

        # Načtení možností
        items += [
            ("• "+label, partial(self.set_value_and_print, value))
            for value, label in self.get_options_for_key(self.mm.selected_key)
        ]

        # Přidání statických položek
        items += [
            ("Zpět na výběr klíče", self.show_key_select_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items

    def get_options_for_key(self, key):
        """Získá předefinované možnosti pro zadání hodnoty"""
        mode_class = self.mm.config_manager.items_manager.KEYS_DATA[key]
        return mode_class.VALUES_DICT

    # Metoda pro uložení a vytisknutí vybraného klíče a hodnoty
    def set_value_and_print(self, value):
        print("### value: ", value)
        self.mm.selected_value = value
        self.mm.config_manager.change_value(
            self.mm.selected_key,
            self.mm.selected_value
        )
        self.mm.response = "print_new_settings"
        self.mm.exit_menu()

    # Metoda pro zadání celočíselné hodnoty (rozmezí 1 - 1000)
    def show_help(self):
        self.mm.response = "input_int_value"
        self.mm.exit_menu()

    # Metoda pro přepnutí na konfigurační menu
    def show_key_select_menu(self):
        self.mm.show_menu("select_key_menu")
