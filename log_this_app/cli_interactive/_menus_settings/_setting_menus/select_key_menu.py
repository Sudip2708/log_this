# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial

from .._base_menu import BaseMenu

class SelectKeyMenu(BaseMenu):

    # Definice nadpisu
    title = "VYBERTE ÚKON:"

    # Definice položek
    @property
    def items(self):

        # Nápověda k této sekci
        items = [
            (f"Nápověda k této nabídce", self.show_help),
        ]

        # Dynamická definice položek menu
        items += [
            ("• "+label, partial(self.set_new_value, key))
            for key, label in self.get_options_dict().items()
        ]

        # Přidání doplňujících položek
        items += [
            ("Zpět na předchozí menu", self.show_previous_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items


    # Metoda pro zobrazení nápovědy
    def show_help(self):
        pass

    # Metoda pro získání slovníku s položkami pro toto menu
    def get_options_dict(self) -> dict:
        """Metoda získá z hlavního slovníku klíč a label"""
        keys_data = self.mm.config_manager.items_manager.KEYS_DATA
        return {
            key: key_class.LABEL
            for key, key_class in keys_data.items()
            if key_class.CATEGORY == self.mm.menus_category
        }

    # Metoda pro zobrazení menu pro nastavení hodnoty
    def set_new_value(self, key):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        self.mm.selected_key = key
        self.mm.show_menu("select_value_menu")

    # Metoda pro přepnutí na předchozí menu
    def show_previous_menu(self):
        self.mm.show_menu("config_menu")






