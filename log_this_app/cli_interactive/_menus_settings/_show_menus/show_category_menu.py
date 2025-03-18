# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial
from .._base_menu import BaseMenu

class ShowCategoryMenu(BaseMenu):

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
            ("• Výpis pro mody @log_this", self.show_log_this_modes_options),
            ("• Výpis pro další nastavení @log_this", self.show_log_this_aspects_options),
            ("• Výpis pro nastavení vzhledu CLI", self.show_interactive_cli_options),
        ]

        # Přidání doplňujících položek
        items += [
            ("Zpět do předchozí menu", self.go_to_previous_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items

    def go_to_previous_menu(self):
        self.mm.show_menu("show_configuration_menu")


    # Metoda pro zobrazení nápovědy
    def show_help(self):
        pass

    def show_log_this_modes_options(self):
        self.mm.config_manager.print_category_configuration("log_this_modes")
        self.mm.exit_menu()
        pass


    def show_log_this_aspects_options(self):
        self.mm.config_manager.print_category_configuration("log_this_aspects")
        self.mm.exit_menu()
        pass

    def show_interactive_cli_options(self):
        self.mm.config_manager.print_category_configuration("interactive_cli")
        self.mm.exit_menu()
        pass
