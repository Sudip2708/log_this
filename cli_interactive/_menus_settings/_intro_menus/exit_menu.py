# print("_menus_settings/_menus_intro/exit_menu.py")

class ExitMenu:

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.title = None
        self.items = [
            ("Pokračovat v interaktivním režimu", lambda: self.mm.show_menu("main_menu")),
            ("Ukončit interaktivní režim", self.mm.exit_menu)
        ]


