# print("_menus_settings/_menus_intro/exit_menu.py")
from .._base_menu import BaseMenu

class ExitMenu(BaseMenu):

    # Definice nadpisu
    title = None

    # Definice položek
    @property
    def items(self):
        return [
        ("Pokračovat v interaktivním režimu", self.mm.show_main_menu),
        ("Ukončit interaktivní režim", self.mm.close_interactive_mode)
    ]


