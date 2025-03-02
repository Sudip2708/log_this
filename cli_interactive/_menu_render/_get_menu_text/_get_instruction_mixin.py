# print("_menu_render/_get_menu_text/_get_instruction_mixin.py")
from abc import ABC

from abc_helper import abc_property
from cli_styler import get_style


class GetInstructionMixin(ABC):
    """Mixin přidávající metodu pro zobrazení/skrytí nápovědy"""

    # Atribut pro instanci MenuRenderer
    menus_manager = abc_property("menus_manager")
    lines = abc_property("lines")


    def _get_instruction(self):
        """
        Metoda pro zobrazení/skrytí nápovědy k používání interaktivního režimu
        """

        # Text pro nápovědu
        instruction = [
            get_style.hint.title("NÁPOVĚDA:"),
            get_style.hint.text("Použijte šipky ↑↓ pro výběr položky"),
            get_style.hint.text("Stiskněte Enter pro potvrzení výběru"),
            get_style.hint.text("Ctrl+C pro ukončení\n"),
        ]

        # Zobrazení nápovědy (je-li aktivní)
        if self.menus_manager.show_instruction:
            self.lines.extend(instruction)

