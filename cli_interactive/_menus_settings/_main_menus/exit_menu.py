# print("_menus_settings/_menus_intro/exit_menu.py")

class ExitMenu:

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.title = None
        self.items = [
            ("Pokračovat v interaktivním režimu", self.show_main_menu),
            ("Ukončit interaktivní režim", self.close_interactive_mode)
        ]

    # Metoda pro přepnutí na hlavní menu
    def show_main_menu(self):
        self.mm.show_menu("main_menu")

    # Metoda uzavře interaktivní režim
    def close_interactive_mode(self):
        self.mm.response = "exit"
        self.mm.exit_menu()