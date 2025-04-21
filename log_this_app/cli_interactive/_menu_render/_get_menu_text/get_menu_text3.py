from typing import List, Optional, Tuple, Any

from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Importy pro typovou kontrolu
    from ...menus_manager import MenusManager

from cli_styler import styler

class GetMenuText:
    """
    Třída definující logiku generování ostylovaného textového menu.
    """

    def __call__(self, menus_manager) -> List[Tuple[str, str]]:
        """
        Generuje a vrací seznam s naformátovaným textem menu.

        Returns:
            List[Tuple[str, str]]: Seznam obsahující jednotlivé části menu.

        Logika:
        """
        mm = menus_manager
        return self._get_instruction(mm) + self._get_menu_offer(mm)

    @staticmethod
    def _get_menu_offer(mm):
        """
        Generuje nabídku menu včetně nadpisu a zvýraznění vybrané položky.

        Returns:
            List[Tuple[str, str]]: Formátované položky menu
        """

        style = styler.get_style.menu
        selected_line_id = mm.selected_item_id 

        return [

            # Nadpis
            style.title(mm.current_menu.title) if mm.current_menu.title else "",

            # Položky
            *[
                style.selected(text)
                if i == selected_line_id else style.offer(text)
                for i, (text, _) in enumerate(mm.current_menu.menu_items)
            ]
        ]

    @staticmethod
    def _get_instruction(mm):
        """
        Generuje nápovědu pro menu s možností zobrazení.

        Returns:
            List[Tuple[str, str]]: Formátované textové instrukce
        """
        if not mm.show_instruction:
            return []

        last_item_id = len(mm.current_menu.menu_help) - 1
        style = styler.get_style.hint

        return [

            # Instrukce k ovládání
            style.title("NÁPOVĚDA:"),
            style.text("Použijte šipky ↑↓ pro výběr položky"),
            style.text("Stiskněte Enter pro potvrzení výběru"),
            style.text("Ctrl+C pro ukončení\n"),

            # Nadpis nápovědy
            style.title(f"Popis položek pro {mm.current_menu.menu_name.lower()}:"),

            # Položky nápovědy
            *[
                style.text(text if index != last_item_id else text + "\n")
                for index, text in enumerate(mm.current_menu.menu_help)
            ]
        ]