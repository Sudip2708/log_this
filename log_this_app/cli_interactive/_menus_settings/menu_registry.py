# print("_menus_settings/menus_manager.py")
from ._a_main_menus import (
    MainMenu,
    ExitMenu,

)
from ._show_menus import (
    ShowConfigurationMenu,
    ShowCategoryMenu
)

from ._config_menus import (
    ConfigMenu,
    SelectKeyMenu,
    SelectValueMenu,
    ResetConfigMenu
)
from ._import_export_menus import (
    ImportExportMenu,
    ImportMenu,
    ExportMenu
)

class MenuRegistry:
    """Spravuje dostupná menu a jejich data"""

    # Atribut shromežďující třídy pro jednotlivá menu
    menus = {

        # Hlavní menu
        "main_menu": MainMenu,
        "exit_menu": ExitMenu,
        "show_configuration_menu": ShowConfigurationMenu,
        "show_category_menu": ShowCategoryMenu,

        # Menu pro nastavení konfigurace knihovny
        "config_menu": ConfigMenu,
        "select_key_menu": SelectKeyMenu,
        "select_value_menu": SelectValueMenu,
        "reset_config_menu": ResetConfigMenu,

        # Inport / Export menu
        "import_export_menu": ImportExportMenu,
        "import_menu": ImportMenu,
        "export_menu": ExportMenu,

    }

    def __init__(self, menus_manager):
        """Inicializace třídy"""

        # Napojení instance MenusManager
        self.mm = menus_manager

        # Atribut pro již vytvořené instace
        self._initialized_menus = {}


    def __call__(self, menu_name):
        """Vrací instanci menu podle názvu"""

        # Vrácení již vytvořené instance, pokud existuje
        if menu_name in self._initialized_menus:
            return self._initialized_menus[menu_name]

        # Načtení a kontrola menu
        menu_cls  = self.menus.get(menu_name)
        if menu_cls  is None:
            raise ValueError(f"Nepodařilo se najít menu s názvem {menu_name}")

        # Inicializace, uložení a navrácení instance třídy pro menu
        instance = menu_cls(self.mm)
        self._initialized_menus[menu_name] = instance
        return instance


    def reset_menu(self, menu_name):
        """Odstraní menu z cache, aby se při dalším volání vytvořila nová instance."""
        self._initialized_menus.pop(menu_name, None)