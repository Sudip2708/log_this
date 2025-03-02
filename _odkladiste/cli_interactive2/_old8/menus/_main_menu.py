from abc import ABC

from abc_helper import abc_property, abc_method


class MainMenuMixin(ABC):

    # Boolean atribut pro zobrazení instrukcí ovládání interaktivního menu
    show_instruction = abc_property("show_instruction")

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Metoda která přepne menu na nové menu
    show_menu = abc_method("show_menu")

    # Metoda která ukončí aktuální menu
    exit_menu = abc_method("exit_menu")


    def main_menu(self):
        """Vrací data (nadpis a položky) pro hlavní menu"""
        title = "VYBERTE ÚKON:"
        items = [
            ("Nastavení vzhledu", self.show_menu("menus_config")),
            ("Nápověda", self.toggle_show_instruction),
            ("Zobrazit konfiguraci", self.show_current_configuration),
            ("Nastavit konfiguraci", lambda: self.show_menu("config_menu")),

            ("Ukončit", self.exit_menu)
        ]
        selected = 0
        return title, items, selected


    def toggle_show_instruction(self):
        """Metoda měnící boolean hodnotu atributu 'show_instruction'"""
        self.show_instruction = not self.show_instruction

    def show_current_configuration(self):
        """Metoda zobrazující aktuální konfiguraci"""
        self.response = "print_configuration"
        self.exit_menu()
