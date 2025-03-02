# print("_menu_render/_get_menu_text/_get_menu_title_mixin.py")
from abc import ABC

from abc_helper import abc_property
from cli_styler import get_style

class GetMenuTitleMixin(ABC):
    """Mixin přidávající metodu pro přidání naformátovaného nadpisu"""

    # Atribut pro instanci MenuRenderer
    menus_manager = abc_property("menus_manager")
    lines = abc_property("lines")



    def _get_menu_title(self):
        """Metoda pro přidání nadpisu menu"""

        # Kontrola zde je nadpis uvedem
        if self.menus_manager.menu.title:

            # Přidání ostylovaného nadpisu
            self.lines.append(
                get_style.menu.title(self.menus_manager.menu.title)
            )

