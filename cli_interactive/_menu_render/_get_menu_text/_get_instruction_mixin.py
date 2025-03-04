# print("_menu_render/_get_menu_text/_get_instruction_mixin.py")
from abc import ABC

from abc_helper import abc_property

class GetInstructionMixin(ABC):
    """Mixin přidávající metodu pro zobrazení/skrytí nápovědy"""

    # Atribut pro instanci MenuRenderer
    mm = abc_property("mm")
    get_style = abc_property("get_style")
    lines = abc_property("lines")


    def _get_instruction(self):
        """
        Metoda pro zobrazení/skrytí nápovědy k používání interaktivního režimu
        """

        # Načtení metody get_style
        get_style = self.mm.styler.get_style

        # Text pro nápovědu
        instruction = [
            get_style.hint.title("NÁPOVĚDA:"),
            get_style.hint.text("Použijte šipky ↑↓ pro výběr položky"),
            get_style.hint.text("Stiskněte Enter pro potvrzení výběru"),
            get_style.hint.text("Ctrl+C pro ukončení\n"),
        ]

        # Zobrazení nápovědy (je-li aktivní)
        if self.mm.show_instruction:
            self.lines.extend(instruction)

