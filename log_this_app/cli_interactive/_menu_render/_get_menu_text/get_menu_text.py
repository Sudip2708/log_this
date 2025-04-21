from typing import List, Optional, Tuple, Any

from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Importy pro typovou kontrolu
    from ...menus_manager import MenusManager

from cli_styler import styler
# from ._get_instruction_mixin import GetInstructionMixin
# from ._get_menu_offer_mixin import GetMenuOfferMixin

class GetMenuText:
    """
    Třída definující logiku generování ostylovaného textového menu.
    """

    def __init__(self, menus_manager: "MenusManager") -> None:
        """
        Inicializuje instanci třídy, pokud ještě nebyla inicializována.

        Args:
            menus_manager (object): Správce menu, který obsahuje konfiguraci menu.

        Logika:
            Metoda nejprve zkontroluje, zda již proběhla inicializace.
            Pokud ne, načte instanci MenusManager a přiřadí ji do atributu 'mm',
            a vytvoří atribut definující proběhlou inicializaci.
        """
        if not hasattr(self, "_initialized"):
            self.mm = menus_manager
            self._initialized = True


    def __call__(self) -> List[Tuple[str, str]]:
        """
        Generuje a vrací seznam s naformátovaným textem menu.

        Returns:
            List[Tuple[str, str]]: Seznam obsahující jednotlivé části menu.

        Logika:
        """
        menu = self.mm.current_menu
        return self._get_instruction(menu) + self._get_menu_offer(menu)


    def _get_menu_offer(self, menu):
        """
        Generuje nabídku menu včetně nadpisu a zvýraznění vybrané položky.

        Returns:
            List[Tuple[str, str]]: Formátované položky menu
        """

        style = styler.get_style.menu
        selected_line_id = self.mm.selected_item_id 

        return [

            # Nadpis
            style.title(menu.title) if menu.title else "",

            # Položky
            *[
                style.selected(text)
                if i == selected_line_id else style.offer(text)
                for i, (text, _) in enumerate(menu.items)
            ]
        ]

    def _get_instruction(self, menu):
        """
        Generuje nápovědu pro menu s možností zobrazení.

        Returns:
            List[Tuple[str, str]]: Formátované textové instrukce
        """
        if not self.mm.show_instruction:
            return []

        last_item_id = len(menu.menu_help) - 1
        style = styler.get_style.hint

        return [

            # Instrukce k ovládání
            style.title("NÁPOVĚDA:"),
            style.text("Použijte šipky ↑↓ pro výběr položky"),
            style.text("Stiskněte Enter pro potvrzení výběru"),
            style.text("Ctrl+C pro ukončení\n"),

            # Nadpis nápovědy
            style.title(f"Popis položek pro {menu.menu_name.lower()}:"),

            # Položky nápovědy
            *[
                style.text(text if index != last_item_id else text + "\n")
                for index, text in enumerate(menu.menu_help)
            ]
        ]