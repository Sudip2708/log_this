# print("_menu_render/_get_menu_text/_get_menu_offer_mixin.py")
from abc import ABC

from abc_helper import abc_property
from cli_styler import styler, cli_print

class GetMenuOfferMixin(ABC):
    """Mixin přidávající metodu pro přidání naformátované nabídky menu"""

    # Atribut pro instanci MenuRenderer
    mm = abc_property("mm")

    def _get_menu_offer(self):
        """
        Generuje nabídku menu včetně nadpisu a zvýraznění vybrané položky.

        Raises:
            ValueError: Pokud nejsou načteny položky menu.

        Returns:
            List[Tuple[str, str]]: Formátované položky menu
        """
        # Kontrola prázdného menu
        if not self.mm.current_menu.menu_items:
            raise ValueError(
                f"Chyba menu - nepodařilo se načíst položky pro {self.mm.current_menu.title}")

        # Nadpis
        title = (
            styler.get_style.menu.title(self.mm.current_menu.title)
            if self.mm.current_menu.title
            else None
        )

        # Položky
        selected_line_id = self.mm.selected_item_id 
        items = [
            styler.get_style.menu.selected(text)
            if i == selected_line_id else styler.get_style.menu.offer(text)
            for i, (text, _) in enumerate(self.mm.current_menu.menu_items)
        ]

        # Filtrování None hodnot pro případ prázdného nadpisu
        return [item for item in [title, *items] if item is not None]