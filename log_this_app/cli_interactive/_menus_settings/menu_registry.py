from typing import Dict, Type

# Import pro typovou analýzu
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..menus_manager import MenusManager
    from ._base_menu import BaseMenu

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
    ResetConfigMenu
)
from ._select_key_menus import (
    SelectKeyMenuModes,
    SelectKeyMenuAspects,
    SelectKeyMenuInteractive
)
from ._select_value_menu import (
    SelectValueMenuModes,
    SelectValueMenuAspects,
    SelectValueMenuInteractive
)
from ._import_export_menus import (
    ImportExportMenu,
    ImportMenu,
    ExportMenu
)


class MenuRegister:
    """
    Spravuje dostupná menu a jejich instance.

    Umožňuje dynamické získávání instancí menu podle jejich klíče a správu jejich cache.
    """

    # Mapa názvů menu k odpovídajícím třídám
    menus: Dict[str, Type["BaseMenu"]] = {
        "main_menu": MainMenu,
        "exit_menu": ExitMenu,
        "show_configuration_menu": ShowConfigurationMenu,
        "show_category_menu": ShowCategoryMenu,
        "config_menu": ConfigMenu,
        "reset_config_menu": ResetConfigMenu,
        "select_key_menu_modes": SelectKeyMenuModes,
        "select_value_menu_modes": SelectValueMenuModes,
        "select_key_menu_aspects": SelectKeyMenuAspects,
        "select_value_menu_aspects": SelectValueMenuAspects,
        "select_key_menu_interactive": SelectKeyMenuInteractive,
        "select_value_menu_interactive": SelectValueMenuInteractive,
        "import_export_menu": ImportExportMenu,
        "import_menu": ImportMenu,
        "export_menu": ExportMenu,
    }

    def __init__(self, menus_manager: "MenusManager") -> None:
        """
        Inicializuje registr menu a propojí ho s manažerem menu.

        :param menus_manager: Instance MenusManager spravující menu.
        """
        self.mm = menus_manager
        self._initialized_menus: Dict[str, "BaseMenu"] = {}

    def __call__(self, menu_name: str) -> "BaseMenu":
        """
        Vrací instanci menu podle zadaného názvu.

        :param menu_name: Název požadovaného menu.
        :return: Instance třídy odpovídající danému menu.
        :raises ValueError: Pokud menu s daným názvem neexistuje.
        """
        if menu_name in self._initialized_menus:
            return self._initialized_menus[menu_name]

        menu_cls = self.menus.get(menu_name)
        if menu_cls is None:
            raise ValueError(f"Nepodařilo se najít menu s názvem {menu_name}")

        instance = menu_cls(self.mm)
        self._initialized_menus[menu_name] = instance
        return instance

    def reset_menu(self, menu_name: str) -> None:
        """
        Odstraní menu z cache, aby se při dalším volání vytvořila nová instance.

        :param menu_name: Název menu, které má být resetováno.
        :note: Tato metoda není momentálně využívána, ale může být užitečná pro dynamické změny menu.
        """
        self._initialized_menus.pop(menu_name, None)
