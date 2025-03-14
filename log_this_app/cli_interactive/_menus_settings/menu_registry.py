# print("_menus_settings/menus_manager.py")
from ._a_main_menus import (
    MainMenu,
    ExitMenu
)
from ._appearance_config import (
    AppearanceMenu,
    SelectColorsMenu,
    SelectSymbolsMenu
)
# from ._key_and_value_config import (
#     ConfigMenu,
#     SelectKeyMenu,
#     SelectValueMenu,
# )
from .modes_config import (
    ModesConfigMenu,
    SelectModeValueMenu
)
from .aspects_config import (
    AspectsConfigMenu,
    SelectAspectValueMenu
)
from ._setting_menus import (
    ConfigMenu,
    SelectKeyMenu,
    SelectValueMenu,
)

class MenuRegistry:
    """Spravuje dostupná menu a jejich data"""

    # Atribut shromežďující třídy pro jednotlivá menu
    menus = {

        # Hlavní menu
        "main_menu": MainMenu,
        "exit_menu": ExitMenu,

        # Menu pro nastavení konfihgurace vzhledu interaktivního režimu
        "appearance_menu": AppearanceMenu,
        "select_symbols_menu": SelectSymbolsMenu,
        "select_colors_menu": SelectColorsMenu,

        # Menu pro nastavení konfigurace knihovny
        "config_menu": ConfigMenu,
        "select_key_menu": SelectKeyMenu,
        "select_value_menu": SelectValueMenu,

        # # Menu pro nastavení konfigurace modu
        # "modes_config_menu": ModesConfigMenu,
        # "select_mode_value_menu": SelectModeValueMenu,
        #
        # # Menu pro nastavení konfigurace vzhledu
        # "aspects_config_menu": AspectsConfigMenu,
        # "select_aspect_value_menu": SelectAspectValueMenu,

    }

    def __init__(self, menus_manager):
        """Inicializace třídy"""

        # Napojení instance MenusManager
        self.mm = menus_manager

        # Atribut pro již vytvořené instace
        self._cache = {}


    def __call__(self, menu_name):
        """Vrací instanci menu podle názvu"""

        # Vrácení již vytvořené instance, pokud existuje
        if menu_name in self._cache:
            return self._cache[menu_name]

        # Načtení a kontrola menu
        menu_cls  = self.menus.get(menu_name)
        if menu_cls  is None:
            raise ValueError(f"Nepodařilo se najít menu s názvem {menu_name}")

        # Inicializace, uložení a navrácení instance třídy pro menu
        instance = menu_cls(self.mm)
        self._cache[menu_name] = instance
        return instance


    def refresh_select_colors_menu(self):
        """Metoda pro obnovu instance pro výběr barvy, tak aby se zobrazila aktuální"""
        self.menus["select_colors_menu"] = SelectColorsMenu(self.mm)


    def refresh_select_symbols_menu(self):
        """Metoda pro obnovu instance pro výběr symbolu, tak aby se zobrazila aktuální"""
        self.menus["select_symbols_menu"] = SelectSymbolsMenu(self.mm)


    def reset_menu(self, menu_name):
        """Odstraní menu z cache, aby se při dalším volání vytvořila nová instance."""
        self._cache.pop(menu_name, None)