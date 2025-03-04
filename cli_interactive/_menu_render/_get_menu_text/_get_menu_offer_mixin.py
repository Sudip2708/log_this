# print("_menu_render/_get_menu_text/_get_menu_offer_mixin.py")
from abc import ABC

from abc_helper import abc_property


class GetMenuOfferMixin(ABC):
    """Mixin přidávající metodu pro přidání naformátované nabídky menu"""

    # Atribut pro instanci MenuRenderer
    mm = abc_property("mm")
    get_style = abc_property("get_style")
    lines = abc_property("lines")


    def _get_menu_offer(self):
        """Metoda pro přidání položek menu"""

        # Načtení id aktuálně vybrané nabýdky
        selected_line_id = self.mm.current_selection

        # Načtení metody get_style
        get_style = self.mm.styler.get_style

        # Cyklus procházející položky
        for i, (text, _) in enumerate(self.mm.menu.items):

            # Přidání položky do hlavního seznamu 'lines'
            self.lines.append(

                # Styl pro aktuálně vybranou položku
                get_style.menu.selected(text)
                if i == selected_line_id

                # Styl pro ostatní položky
                else get_style.menu.offer(text)
            )