from abc import ABC, abstractmethod

class GetMenuItems(ABC):

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def switch_menu(self, new_menu_type):
        pass

    @property
    @abstractmethod
    def show_help(self):
        pass

    @show_help.setter
    @abstractmethod
    def show_help(self, value):
        pass

    @property
    @abstractmethod
    def response(self):
        pass

    @response.setter
    @abstractmethod
    def response(self, value):
        pass

    # Funkce pro navrácení menu dle požadovaného typu menu
    def get_menu_items(self, menu_type):

        # Definice menu položek podle typu menu
        if menu_type == "main":
            return "▼ VYBERTE ÚKON:", [
                ("Instrukce", self.show_help_handler),
                ("Ukázat aktuální konfiguraci", self.show_config_handler),
                ("Změnit konfiguraci", self.switch_to_config_menu),
                ("Import/Export konfigurace", self.switch_to_import_export_menu),
                ("Nápověda k těmto volbám", self.show_config_handler),
                ("Ukončit interaktivní režim", self.exit_handler)
            ]

        elif menu_type == "post_action":
            return None, [
                ("Pokračovat v interaktivním režimu", self.switch_to_main_menu),
                ("Ukončit interaktivní režim", self.exit_handler)
            ]

        elif menu_type == "config_menu":
            return "▼ VYBERTE ÚKON:", [
                ("Změnit konfiguraci pomocí klíče a hodnoty", self.set_value_handler),
                ("Změnit konfiguraci na předešlou", self.show_config_handler),
                ("Změnit konfiguraci na defaultní hodnoty", self.show_config_handler),
                ("Nápověda k těmto volbám", self.show_config_handler),
                ("Zpět do hlavního menu", self.switch_to_main_menu),
            ]

        elif menu_type == "import_export":
            return "▼ VYBERTE ÚKON:", [
                ("Uložit aktuální konfiguraci do souboru", self.show_config_handler),
                ("Načíst konfiguraci ze souboru", self.show_config_handler),
                ("Nápověda k těmto volbám", self.show_config_handler),
                ("Zpět do hlavního menu", self.switch_to_main_menu),
            ]

    def switch_to_main_menu(self):
        """Přepne zpět na hlavní menu."""
        self.switch_menu("main")

    def switch_to_config_menu(self):
        """Přepne do submenu pro nastavení konfigurace."""
        self.switch_menu("config_menu")

    def switch_to_import_export_menu(self):
        """Přepne do submenu pro nastavení konfigurace."""
        self.switch_menu("import_export")

    # Funkce pro zobrazení a skyrytí menu
    def show_help_handler(self):
        self.show_help = not self.show_help

    # Funkce pro výpis aktuální konfigurace
    def show_config_handler(self):
        self.response = "print_configuration"
        self.exit()

    # Funkce pro nasavení nové konfigurace
    def set_value_handler(self):
        self.response = "set_value"
        self.exit()

    # Funkce pro ukončení interaktivního režimu
    def exit_handler(self):
        self.response = None
        self.exit()