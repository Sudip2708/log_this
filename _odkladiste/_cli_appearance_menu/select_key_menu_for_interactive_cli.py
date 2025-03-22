# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial

from .._base_menu import BaseMenu

class SelectKeyMenuForInteractiveCLI(BaseMenu):

    menu_name = "Menu pro nastavení vzhledu interaktivního režimu"
    _menu_key = "select_key_menu_for_interactive_cli"
    _previous_menu_key = "main_menu"
    _category = "interactive_cli"

    # Dinamické vytvořeí nabídky pro nápovědu
    @property
    def _menu_items(self):
        category_dict = self.im.get_key_class_for_category(self._category)
        return {
            key: {
                "label": key_class.LABEL,
                "help": key_class.INFO
            }
            for key, key_class in category_dict.items()
        }


    # Definice nadpisu
    title = "VYBERTE ÚKON:"

    # Definice položek
    @property
    def items(self):
        return [
            self.get_help_offer(),
            self.get_items_offer(),
            self.get_previous_menu(self._previous_menu_key),
            self.get_close_offer(),
        ]

    # Metoda pro získání položek menu
    def get_items_offer(self):
        return (
            ((label, partial(self.set_new_value, key))
             for key, label in self._menu_items.items()),
        )


    # Metoda pro zobrazení menu pro nastavení hodnoty
    def set_new_value(self, key):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        self.mm.selected_key = key
        self.mm.show_menu("select_value_menu")









