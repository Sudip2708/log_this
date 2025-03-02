from abc import ABC

from abc_helper import abc_property, abc_method


class MenusConfigMixin(ABC):

    # Boolean atribut pro zobrazení instrukcí ovládání interaktivního menu
    show_instruction = abc_property("show_instruction")

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Metoda která přepne menu na nové menu
    show_menu = abc_method("show_menu")

    # Metoda která ukončí aktuální menu
    exit_menu = abc_method("exit_menu")


    def menus_config(self):
        """Vrací data (nadpis a položky) pro hlavní menu"""
        title = "VYBERTE ÚKON:"
        items = [
            ("Nastavit barevný mod", lambda: self.show_menu("menus_colors_settings")),
            ("Nastavit zobrazení značek", lambda: self.show_menu("menu_symbols_ettings")),
            ("Zpět do hlavního menu", lambda: self.show_menu("main_menu")),
            ("Ukončit", self.exit_menu)
        ]
        selected = 0
        return title, items, selected

