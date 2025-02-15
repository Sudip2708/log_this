class MenuController:
    """Třída pro řízení logiky menu"""

    def __init__(self, view, config):
        self.view = view
        self.config = config
        self.current_selection = 0
        self.show_help = False
        self.menu_items = self.initialize_menu_items()

    def initialize_menu_items(self):
        return [
            ("Nápověda", self.toggle_help),
            ("Zobrazit konfiguraci", self.show_configuration),
            ("Nastavit hodnotu", self.set_value),
            ("Ukončit", self.exit)
        ]

    def move_selection(self, direction):
        new_selection = self.current_selection + direction
        if 0 <= new_selection < len(self.menu_items):
            self.current_selection = new_selection
            self.view.refresh()

    def select_current_item(self):
        self.menu_items[self.current_selection][1]()

    def toggle_help(self):
        self.show_help = not self.show_help
        self.view.refresh()

    def show_configuration(self):
        self.config.print_configuration()
        self.exit()

    def set_value(self):
        key = input("\nZadejte klíč: ")
        value = input("Zadejte hodnotu: ")
        self.config.set_value(key, value)
        print(f"\nNastaveno: {key} = {value}")
        self.exit()

    def exit(self):
        self.view.exit()