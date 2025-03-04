# print("_menu_render/_get_menu_text/_get_menu_title_mixin.py")
from abc import ABC

from abc_helper import abc_property

class GetMenuTitleMixin(ABC):
    """Mixin přidávající metodu pro přidání naformátovaného nadpisu"""

    # Atribut pro instanci MenuRenderer
    mm = abc_property("mm")
    get_style = abc_property("get_style")
    lines = abc_property("lines")



    def _get_menu_title(self):
        """Metoda pro přidání nadpisu menu"""

        # Kontrola zde je nadpis uvedem
        if self.mm.menu.title:

            # Přidání ostylovaného nadpisu
            self.lines.append(
                self.mm.styler.get_style.menu.title(self.mm.menu.title)
            )
