# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial

from .._base_menu import BaseMenu

class SelectKeyMenu(BaseMenu):

    menu_name = "Menu pro výběr klíče"
    _menu_key = "select_key_menu"
    _previous_menu_key = None
    _menu_items = {
        "show_configuration_menu": {
            "label": "• Zobrazit konfiguraci",
            "help": "Přístup k menu pro zobrazení aktuální konfigurace.",
        },
        "config_menu": {
            "label": "• Nastavit konfiguraci",
            "help": "Přístup k menu pro změnu konfigurace.",
        },
        "import_export_menu": {
            "label": "• Import/Export konfigurace",
            "help": "Přístup k menu pro import a export konfigurace.",
        },
        "show_appearance_menu": {
            "label": "• Nastavení vzhledu interaktivního režimu",
            "help": "Přístup k menu pro nastavení vzhledu dialogových oken.",
        }
    }


    # Definice nadpisu
    title = "VYBERTE ÚKON:"

    # Definice položek
    @property
    def items(self):
        return [
            self.get_help_offer(),
            ((label, partial(self.set_new_value, key))
            for key, label in self.get_options_dict().items()),
            self.get_menu_offer("reset_config_menu"),
            self.get_previous_menu(self._previous_menu_key),
            self.get_close_offer(),
        ]


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
        if self.mm.menus_category == "interactive_cli":
            self.mm.show_menu("main_menu")
        else:
            self.mm.show_menu("config_menu")






