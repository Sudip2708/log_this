# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial
from .._base_menu import BaseMenu

class ResetConfigMenu(BaseMenu):

    # Definice nadpisu
    title = "VYBERTE ÚKON:"

    # Definice položek
    @property
    def items(self):

        # Nápověda k této sekci
        items = [
            (f"Nápověda", self.show_help),
        ]

        # Definice položek
        items += [
            ("• Resetovat na předchozí nastavení", self.reset_to_previous),
            ("• Resetovat na defaultní nastavení", self.reset_to_default),
        ]

        # Přidání doplňujících položek
        items += [
            ("Zpět do předchozího menu", self.show_config_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items


    # Metoda pro zobrazení nápovědy
    def show_help(self):
        pass

    # Metoda pro přepnutí na konfigurační menu
    def show_config_menu(self):
        self.mm.show_menu("config_menu")

    # Metoda pro zobrazení menu pro nastavení položek modů
    def reset_to_previous(self):
        self.mm.config_manager.reset_to_previous_configuration()
        self.mm.exit_menu()

    # Metoda pro zobrazení menu pro nastavení položek aspektů
    def reset_to_default(self):
        self.mm.config_manager.reset_to_default_configuration()
        self.mm.exit_menu()
