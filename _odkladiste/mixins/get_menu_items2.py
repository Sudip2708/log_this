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

    selected_key = None
    selected_value = None

    # Funkce pro navrácení menu dle požadovaného typu menu
    def get_menu_items(self, menu_type):

        # Definice menu položek podle typu menu
        if menu_type == "main":
            return "▼ VYBERTE ÚKON:", [
                ("Nápověda", self.show_help_handler),
                ("Zobrazit konfiguraci", self.show_config_handler),
                ("Nastavit konfiguraci", self.switch_to_config_menu),
                ("Ukončit", self.exit_handler)
            ]

        elif menu_type == "config_menu":
            return "▼ VYBERTE ÚKON:", [
                ("Nastavit hodnotu 1", self.switch_to_select_key),
                ("Nastavit hodnotu 2", self.set_value_handler),
                ("Nastavit hodnotu 3", self.set_value_handler),
                ("Zpět do hlavního menu", self.switch_to_main)
            ]

        elif menu_type == "ending_menu":
            return None, [
                ("Pokračovat v interaktivním režimu", self.switch_to_main),
                ("Ukončit interaktivní režim", self.exit_handler)
            ]

        elif menu_type == "select_key_menu":
            return "▼ VYBERTE KLÍČ:", [
                ("key_1", lambda: self.switch_to_set_key("key_1")),
                ("key_2", lambda: self.switch_to_set_key("key_2")),
                ("key_3", lambda: self.switch_to_set_key("key_3")),
                ("Zpět", self.switch_to_config_menu)
            ]

        elif menu_type == "select_value_menu":
            return f"▼ VYBERTE HODNOTU PRO {self.selected_key.upper()}:", [
                ("value_1", lambda: self.set_value_and_print("value_1")),
                ("value_2", lambda: self.set_value_and_print("value_2")),
                ("value_3", lambda: self.set_value_and_print("value_3")),
                ("Zadat vlastní hodnotu", self.input_custom_value),
                ("Zpět", self.switch_to_select_key)
            ]

    def switch_to_main(self):
        """Přepne zpět na hlavní menu."""
        self.switch_menu("main")

    def switch_to_config_menu(self):
        """Přepne do submenu pro nastavení konfigurace."""
        self.switch_menu("config_menu")

    def switch_to_select_key(self):
        """Přepne do submenu pro výběr klíče."""
        self.reset_key_value()
        self.switch_menu("select_key_menu")

    def switch_to_set_key(self, key=None):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        if key:
            self.selected_key = key
        if self.selected_key:
            self.switch_menu("select_value_menu")
        else:
            print("Není vybrán žádný klíč, zadejte klíč prosím znovu.")
            self.switch_menu("select_key_menu")

    def set_value_and_print(self, value):
        """Uloží vybranou hodnotu, vypíše výsledek a vrátí se do hlavního menu."""
        self.selected_value = value
        self.response = "print_new"
        self.exit()

    def reset_key_value(self):
        """Resetuje hodnoty těchto dvou atributů na None"""
        self.selected_key = None
        self.selected_value = None

    def input_custom_value(self):
        """Zobrazí vstupní dialog pro zadání vlastní hodnoty."""
        self.response = "input_custom_value"
        self.exit()

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
        self.response = "exit"
        self.exit()


