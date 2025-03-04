# print("_menus_settings/menus_manager.py")
from ._main_menus import (
    MainMenu,
    ExitMenu
)
from ._appearance_config import (
    AppearanceMenu,
    SelectColorsMenu,
    SelectSymbolsMenu
)
from ._key_and_value_config import (
    ConfigMenu,
    SelectKeyMenu,
    SelectValueMenu,
)

class MenuRegistry:
    """Spravuje dostupná menu a jejich data"""

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.menus = {

            # Hlavní menu
            "main_menu": MainMenu(self.mm),
            "exit_menu": ExitMenu(self.mm),

            # Menu pro nastavení konfihgurace vzhledu interaktivního režimu
            "appearance_menu": AppearanceMenu(self.mm),
            "select_symbols_menu": SelectSymbolsMenu(self.mm),
            "select_colors_menu": SelectColorsMenu(self.mm),

            # Menu pro nastavení konfigurace knihovny
            "config_menu": ConfigMenu(self.mm),
            "select_key_menu": SelectKeyMenu(self.mm),
            "select_value_menu": SelectValueMenu,  # Odkaz na třídu a instance se bude tvořit až př inicializaci

        }

    def __call__(self, menu_name):
        """Vrací instanci menu podle názvu"""
        menu = self.menus.get(menu_name)

        if menu is None:
            raise ValueError(f"Nepodařilo se najít menu s názvem {menu_name}")

        # Pokud je `menu` třída, vytvoříme instanci
        if isinstance(menu, type):
            return menu(self.mm)  # Vytvoření nové instance

        return menu  # Vrácení existující instance

    def refresh_select_colors_menu(self):
        """Metoda pro obnovu instance pro výběr barvy, tak aby se zobrazila aktuální"""
        self.menus["select_colors_menu"] = SelectColorsMenu(self.mm)

    def refresh_select_symbols_menu(self):
        """Metoda pro obnovu instance pro výběr symbolu, tak aby se zobrazila aktuální"""
        self.menus["select_symbols_menu"] = SelectSymbolsMenu(self.mm)



