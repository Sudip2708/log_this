from abc import ABC

from abc_helper import abc_property, abc_method


class GetMainMenuMixin(ABC):

    # Boolean atribut pro zobrazení instrukcí ovládání interaktivního menu
    show_instruction = abc_property("show_instruction")

    # Metoda která nastaví atribut 'response' na 'print_configuration' a ukončí menu
    set_response = abc_method("set_response")

    # Metoda která přepne menu na nové menu
    switch_menu = abc_method("switch_menu")

    # Metoda která ukončí aktuální menu
    exit_menu = abc_method("exit_menu")


    def get_main_menu(self):
        """Vrací data (nadpis a položky) pro hlavní menu"""
        title = "▼ VYBERTE ÚKON: "
        items = [
            ("Instrukce", self.toggle_show_instruction),
            ("Zobrazit konfiguraci", lambda: self.set_response("print_configuration")),
            ("Nastavit konfiguraci", lambda: self.switch_menu("config_menu")),
            ("Ukončit", self.exit_menu)
        ]
        return title, items


    def toggle_show_instruction(self):
        """Metoda měnící boolean hodnotu atributu 'show_instruction'"""
        self.show_instruction = not self.show_instruction