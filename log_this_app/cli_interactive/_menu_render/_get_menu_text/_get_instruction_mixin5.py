# print("_menu_render/_get_menu_text/_get_instruction_mixin.py")
from abc import ABC
from typing import List, Optional, Tuple, Any
from abc_helper import abc_property
from cli_styler import styler

class GetInstruction:
    """Mixin přidávající metodu pro zobrazení/skrytí nápovědy"""

    BASE_INSTRUCTION = [
        styler.get_style.hint.title(f"NÁPOVĚDA:"),
        styler.get_style.hint.text("Použijte šipky ↑↓ pro výběr položky"),
        styler.get_style.hint.text("Stiskněte Enter pro potvrzení výběru"),
        styler.get_style.hint.text("Ctrl+C pro ukončení\n"),
    ]

    @staticmethod
    def title(menu):
        return styler.get_style.hint.title(
            f"Popis položek pro {menu.menu_name.lower()}:"
        )

    @staticmethod
    def text(menu):
        menu_help = menu.menu_help
        return [
            styler.get_style.hint.text(
                text if index != len(menu_help) - 1 else text + "\n"
            )
            for index, text in enumerate(menu_help)
        ]

    def __call__(self, menus_manager):
        menu = menus_manager.get_actual_menu_class()
        return (
            self.BASE_INSTRUCTION + self.title(menu) + self.text(menu)
            if menus_manager.show_instruction else []
        )








# from abc import ABC
# from abc_helper import abc_property
# from cli_styler import styler
# from typing import List, Any
#
#
# class GetInstructionMixin(ABC):
#     """
#     Mixin přidávající metodu pro zobrazení nebo skrytí nápovědy v menu.
#
#     Atributy:
#         mm (object): Instance správce menu.
#         get_style (callable): Metoda vracející styly.
#         lines (List[Any]): Seznam naformátovaného textu menu.
#     """
#
#     mm = abc_property("mm")
#     get_style = abc_property("get_style")
#     lines = abc_property("lines")
#
#     def _get_instruction(self) -> None:
#         """
#         Přidá nápovědu k interaktivnímu režimu, pokud je aktivní.
#         """
#         instruction = self._get_base_instruction()
#         menu_instruction = self._get_menu_instruction()
#         instruction.extend(menu_instruction)
#
#         if self.mm.show_instruction:
#             self.lines.extend(instruction)
#
#     def _get_base_instruction(self) -> List[Any]:
#         """
#         Vrátí základní instrukce pro používání menu.
#
#         Returns:
#             List[Any]: Seznam základních instrukcí.
#         """
#         return [
#             styler.get_style.hint.title("NÁPOVĚDA:"),
#             styler.get_style.hint.text("Použijte šipky ↑↓ pro výběr položky"),
#             styler.get_style.hint.text("Stiskněte Enter pro potvrzení výběru"),
#             styler.get_style.hint.text("Ctrl+C pro ukončení\n"),
#         ]
#
#     def _get_menu_instruction(self) -> List[Any]:
#         """
#         Vrátí seznam s nápovědou ke konkrétním položkám menu.
#
#         Returns:
#             List[Any]: Seznam nápověd pro jednotlivé položky menu.
#         """
#         menu = self.mm.menu_register(self.mm.menu_name)
#         menu_help = menu.menu_help
#
#         return (
#             [styler.get_style.hint.title(
#                 f"Popis položek pro {menu.menu_name.lower()}:")]
#             + [styler.get_style.hint.text(
#                 text if index != len(menu_help) - 1 else text + "\n")
#                for index, text in enumerate(menu_help)]
#             if menu_help else []
#         )
