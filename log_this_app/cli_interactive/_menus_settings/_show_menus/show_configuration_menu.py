# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial
from .._base_menu import BaseMenu

class ShowConfigurationMenu(BaseMenu):

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
            ("• Stručný výpis", self.show_config_simple),
            ("• Podrobný výpis s popisem", self.show_category_menu),
        ]

        # Přidání doplňujících položek
        items += [
            ("Zpět do hlavního menu", self.mm.show_main_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items


    # Metoda pro zobrazení nápovědy
    def show_help(self):
        pass

    # Metoda pro zobrazení menu pro nastavení položek modů
    def show_config_simple(self):
        self.mm.config_manager.print_actual_configuration2()
        self.mm.exit_menu()
        pass


    # Metoda pro zobrazení menu pro nastavení položek aspektů
    def show_category_menu(self):
        self.mm.show_menu("show_category_menu")
        pass

