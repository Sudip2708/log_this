# print("_menus_settings/_menus_intro/exit_menu.py")

class ExitMenu:

    def __init__(self, menus_manager):

        # Navázání instance menus managera
        self.mm = menus_manager

        # Definice nadpisu
        self.title = None

        # Definice položek
        self.items = [
            ("Pokračovat v interaktivním režimu", self.mm.show_main_menu),
            ("Ukončit interaktivní režim", self.mm.close_interactive_mode)
        ]


