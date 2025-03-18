# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial
from .._base_menu import BaseMenu

class ImportExportMenu(BaseMenu):

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
            ("• Možnosti pro import konfigurace", self.import_config_from_file),
            ("• Možnosti pro export konfigurace", self.export_confit_to_file),

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

    # Metoda pro přepnutí na konfigurační menu
    def show_previous_menu(self):
        self.mm.show_menu("main_menu")

    # Metoda pro zobrazení menu pro nastavení položek aspektů
    def import_config_from_file(self):
        self.mm.show_menu("import_menu")

    # Metoda pro zobrazení menu pro nastavení položek aspektů
    def export_confit_to_file(self):
        self.mm.show_menu("export_menu")
