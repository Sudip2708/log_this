# print("_response_manager/response_manager.py")
from .dialogs import (
    dialog_import_file_path,
    dialog_export_file_path,
    dialog_export_directory_path
)
from .inputs import (
    input_int_value,
    input_import_file_path,
    input_export_file_path,
    input_export_directory_path
)


from cli_styler import styler

class ResponseManager:
    """Spravuje reakce na vybrané položky menu"""

    def __init__(self, menus_manager):

        # Přiřazení instance hlavní třídy
        self.mm = menus_manager

        # Definice akcí odezvy
        self.response_actions = {

            # Vstup pro zadíní číslené hodnoty
            "input_int_value": self.input_int_value,

            # Vstup pro zadání cesty
            "input_import_file_path": self.input_import_file_path,
            "input_export_file_path": self.input_export_file_path,
            "input_export_directory_path": self.input_export_directory_path,

            # Dialog pro zadání cesty
            "dialog_import_file_path": self.dialog_import_file_path,
            "dialog_export_file_path": self.dialog_export_file_path,
            "dialog_export_directory_path": self.dialog_export_directory_path,
        }

    def __call__(self):
        """Vrací výstupní reakci na daný požadavek"""
        action = self.response_actions.get(self.mm.response)
        if action:
            action()
            self.mm.response = "exit_menu"  # Nastavení zobrazení exut menu

    # Vstup pro zadíní číslené hodnoty
    def input_int_value(self):
        # Výběr hodnoty
        self.mm.selected_value = input_int_value(self.mm)
        # Pokud nebyla zadána žádná hodnota, vrací se None
        if self.mm.selected_value:
            # Zapsání hodnoty
            self.mm.config_manager.change_value(
                self.mm.selected_key,
                self.mm.selected_value
            )

    # Vstup pro zadání cesty
    def input_import_file_path(self):
        # Výběr hodnoty
        self.mm.selected_path = input_import_file_path(self.mm)
        # Pokud nebyla zadána žádná hodnota, vrací se None
        if self.mm.selected_path:
            print("### self.mm.selected_path: ", self.mm.selected_path)

    def input_export_file_path(self):
        # Výběr hodnoty
        self.mm.selected_path = input_export_file_path(self.mm)
        # Pokud nebyla zadána žádná hodnota, vrací se None
        if self.mm.selected_path:
            print("### self.mm.selected_path: ", self.mm.selected_path)

    def input_export_directory_path(self):
        # Výběr hodnoty
        self.mm.selected_path = input_export_directory_path(self.mm)
        # Pokud nebyla zadána žádná hodnota, vrací se None
        if self.mm.selected_path:
            print("### self.mm.selected_path: ", self.mm.selected_path)

    # Dialog pro zadání cesty
    def dialog_import_file_path(self):
        # Výběr hodnoty
        self.mm.selected_path = dialog_import_file_path(self.mm)
        # Pokud nebyla zadána žádná hodnota, vrací se None
        if self.mm.selected_path:
            print("### self.mm.selected_path: ", self.mm.selected_path)

    def dialog_export_file_path(self):
        # Výběr hodnoty
        self.mm.selected_path = dialog_export_file_path(self.mm)
        # Pokud nebyla zadána žádná hodnota, vrací se None
        if self.mm.selected_path:
            print("### self.mm.selected_path: ", self.mm.selected_path)

    def dialog_export_directory_path(self):
        # Výběr hodnoty
        self.mm.selected_path = dialog_export_directory_path(self.mm)
        # Pokud nebyla zadána žádná hodnota, vrací se None
        if self.mm.selected_path:
            print("### self.mm.selected_path: ", self.mm.selected_path)
