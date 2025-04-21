# print("_menu_render/_get_menu_text/_get_menu_offer_mixin.py")
from abc import ABC

from abc_helper import abc_property
from cli_styler import styler, cli_print

class GetMenuOfferMixin(ABC):
    """Mixin přidávající metodu pro přidání naformátované nabídky menu"""

    # Atribut pro instanci MenuRenderer
    mm = abc_property("mm")
    get_style = abc_property("get_style")
    lines = abc_property("lines")

    def _get_menu_offer(self):
        """
        Generuje nabídku menu včetně nadpisu a zvýraznění vybrané položky.

        Returns:
            List[Tuple[str, str]]: Formátované položky menu
        """
        # Kontrola prázdného menu
        if not self.mm.current_menu.menu_items:
            raise ValueError("Chyba menu - nepovedlo se načítst položky.")

        lines = []

        # Přidání nadpisu menu, pokud existuje
        if self.mm.current_menu.title:
            lines.append(
                styler.get_style.menu.title(self.mm.current_menu.title)
            )

        # Generování položek menu s rozlišením vybrané položky
        selected_line_id = self.mm.selected_item_id 
        for index, (text, _) in enumerate(self.mm.current_menu.menu_items):
            style_func = (
                styler.get_style.menu.selected
                if index == selected_line_id
                else styler.get_style.menu.offer
            )
            lines.append(style_func(text))

        return lines