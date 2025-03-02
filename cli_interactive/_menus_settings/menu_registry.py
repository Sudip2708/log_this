# print("_menus_settings/menus_manager.py")
from ._intro_menus import (
    MainMenu,
    ExitMenu
)
from ._appearance_config import (
    AppearanceConfigMenu,
    ColorsModeSelectMenu,
    SymbolsModeSelectMenu
)
from ._key_and_value_config import (
    ConfigValueSelect,
    ConfigKeySelect,
    ConfigMenu
)

class MenuRegistry:
    """Spravuje dostupná menu a jejich data"""

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.menus = {

            # Hlavní menu
            "main_menu": MainMenu(self.mm),
            "exit_menu": ExitMenu(self.mm),

            # Menu pro nastavení konfigurace knihovny
            "config_menu": ConfigMenu(self.mm),
            "key_select_menu": ConfigKeySelect(self.mm),
            "value_select_menu": ConfigValueSelect(self.mm),

            # Menu pro nastavení konfihgurace vzhledu interaktivního režimu
            "appearance_menu": AppearanceConfigMenu(self.mm),
            "symbols_select_menu": SymbolsModeSelectMenu(self.mm),
            "colors_select_menu": ColorsModeSelectMenu(self.mm),
        }

    def __call__(self, name):
        """Vrací instanci menu podle názvu"""
        return self.menus.get(name, None)

