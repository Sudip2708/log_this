# print("_menu_render/_get_menu_text/_get_menu_offer_mixin.py")
from abc import ABC

from abc_helper import abc_property
from cli_styler import get_style

class GetMenuOfferMixin(ABC):
    """Mixin přidávající metodu pro přidání naformátované nabídky menu"""

    # Atribut pro instanci MenuRenderer
    menus_manager = abc_property("menus_manager")
    lines = abc_property("lines")


    def _get_menu_offer(self):
        """Metoda pro přidání položek menu"""

        # Načtení id aktuálně vybrané nabýdky
        selected_line_id = self.menus_manager.current_selection

        # Cyklus procházející položky
        for i, (text, _) in enumerate(self.menus_manager.menu.items):

            # Přidání položky do hlavního seznamu 'lines'
            self.lines.append(

                # Styl pro aktuálně vybranou položku
                get_style.menu.selected(text)
                if i == selected_line_id

                # Styl pro ostatní položky
                else get_style.menu.offer(text)
            )