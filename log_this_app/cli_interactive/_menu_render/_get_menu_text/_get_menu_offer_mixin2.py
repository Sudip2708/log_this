# print("_menu_render/_get_menu_text/_get_menu_offer_mixin.py")
from abc import ABC

from abc_helper import abc_property
from cli_styler import styler

class GetMenuOfferMixin(ABC):
    """Mixin přidávající metodu pro přidání naformátované nabídky menu"""

    # Atribut pro instanci MenuRenderer
    mm = abc_property("mm")
    get_style = abc_property("get_style")
    lines = abc_property("lines")


    def _get_menu_offer(self):
        """Metoda pro přidání položek menu"""

        lines = []

        menu_title = self.mm.current_menu.title
        if menu_title:
            lines.append(
                styler.get_style.menu.title(menu_title)
            )

        selected_line_id = self.mm.selected_item_id 
        for i, (text, _) in enumerate(self.mm.current_menu.menu_items):
            lines.append(
                styler.get_style.menu.selected(text)
                if i == selected_line_id
                else styler.get_style.menu.offer(text)
            )

        return lines