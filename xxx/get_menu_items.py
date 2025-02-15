def get_menu_items(self, menu_type):
    """Metoda vrátí nabídku pro interaktivní menu"""

    menu_items = []

    # Definice menu položek podle typu menu
    if menu_type == "main":
        menu_items = [
            ("Nápověda", self.show_help_handler),
            ("Zobrazit konfiguraci", self.show_config_handler),
            ("Nastavit hodnotu", self.set_value_handler),
            ("Ukončit", self.exit_handler)
        ]

    return menu_items