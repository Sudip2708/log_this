# print("_menus_settings/_menus_intro/main_menu.py")

class MainMenu:

    def __init__(self, menus_manager):
        self.mm = menus_manager
        self.title = "VYBERTE ÚKON:"
        self.items = [
            ("Nápověda", self.toggle_show_instruction),
            ("Zobrazit konfiguraci", self.show_actual_configuration),
            ("Nastavit konfiguraci", self.show_config_menu),
            ("Nastavení vzhledu", self.show_appearance_menu),
            ("Ukončit", self.close_interactive_mode),
        ]

    # Metoda pro zobrazení a skrytí nápovědy
    def toggle_show_instruction(self):
        self.mm.show_instruction = not self.mm.show_instruction

    # Metoda pro výpis aktuální konfigurace
    def show_actual_configuration(self):
        self.mm.response = "print_configuration"
        self.mm.exit_menu()

    # Metoda pro přepnutí na konfigurační menu
    def show_config_menu(self):
        self.mm.show_menu("config_menu")

    # Metoda přepne na menu pro konfiguraci vzhledu
    def show_appearance_menu(self):
        self.mm.show_menu("appearance_menu")

    # Metoda uzavře interaktivní režim
    def close_interactive_mode(self):
        self.mm.response = "exit"
        self.mm.exit_menu()