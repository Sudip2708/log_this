from abc import ABC

from abc_helper import abc_property, abc_method


class MenusSymbolsSettingsMixin(ABC):

    # Boolean atribut pro zobrazení instrukcí ovládání interaktivního menu
    show_instruction = abc_property("show_instruction")

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Metoda která přepne menu na nové menu
    show_menu = abc_method("show_menu")

    # Metoda která ukončí aktuální menu
    exit_menu = abc_method("exit_menu")


    def menus_symbols_config(self):
        """Vrací data (nadpis a položky) pro hlavní menu"""
        title = "VYBERTE BAREVNÝ MOD:"
        items = [
            ("Základní set symbolů", self.set_color_mode),
            ("Obrázkové symboly", self.set_color_mode),
            ("Bez zobrazovaných symbolů", self.set_color_mode),
            ("Zpět do konfiguračního menu", lambda: self.show_menu("interactive_menu_config")),
            ("Ukončit", self.exit_menu)
        ]
        selected = 0
        return title, items, selected


    def set_color_mode(self):
        """Metoda vracející konfigurační menu"""
        pass
        #self.show_menu("config_menu")


    # def get_back_to_interactive_config_menu(self):
    #     """Metoda pro návrat do hlavního menu"""
    #     self.show_menu("interactive_menu_config")