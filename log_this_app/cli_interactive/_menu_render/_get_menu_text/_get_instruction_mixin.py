# print("_menu_render/_get_menu_text/_get_instruction_mixin.py")
from abc import ABC

from abc_helper import abc_property
from cli_styler import styler

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

        instruction = self._get_base_instruction()
        menu_instruction = self._get_menu_instruction()
        instruction.extend(menu_instruction)

        # Zobrazení nápovědy (je-li aktivní)
        if self.mm.show_instruction:
            self.lines.extend(instruction)

    def _get_base_instruction(self):
        menu_name = self.mm.menu_name
        return [
            styler.get_style.hint.title(f"NÁPOVĚDA:"),
            styler.get_style.hint.text("Použijte šipky ↑↓ pro výběr položky"),
            styler.get_style.hint.text("Stiskněte Enter pro potvrzení výběru"),
            styler.get_style.hint.text("Ctrl+C pro ukončení\n"),
        ]

    def _get_menu_instruction(self):
        menu = self.mm.menu_register(self.mm.menu_name)
        menu_help = menu.menu_help
        return (

            # Přidání nadpisu
            [styler.get_style.hint.title(
                f"Popis položek pro {menu.menu_name.lower()}:")]

            # Přidání položek
            + [styler.get_style.hint.text(
                text if index != len(menu_help) - 1 else text + "\n")
                for index, text in enumerate(menu_help)]

            # Pokud není nápověda nepřidávat nic
            if menu_help else []
        )