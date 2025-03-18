# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial
from .._base_menu import BaseMenu

class ImportMenu(BaseMenu):

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
            ("• Výběr cesty skrze souborové okno", self.dialog_import_file_path),
            ("• Ruční zadání cesty ", self.input_import_file_path),

        ]

        # Přidání doplňujících položek
        items += [
            ("Zpět do předchozího menu", self.show_previous_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items


    # Metoda pro zobrazení nápovědy
    def show_help(self):
        pass

    # Metoda pro přepnutí na předchozí menu
    def show_previous_menu(self):
        self.mm.show_menu("import_export_menu")

    # Metoda pro zobrazení menu pro nastavení položek modů
    def input_import_file_path(self):
        self.mm.response = "input_import_file_path"
        self.mm.exit_menu()

    # Metoda pro zobrazení menu pro nastavení položek modů
    def dialog_import_file_path(self):
        self.mm.response = "dialog_import_file_path"
        self.mm.exit_menu()