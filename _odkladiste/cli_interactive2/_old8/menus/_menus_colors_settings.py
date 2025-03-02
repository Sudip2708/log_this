from abc import ABC

from abc_helper import abc_property, abc_method
from cli_styler import set_colors_mode, get_current_colors_mode, get_colors_modes_dict


def get_current_color_mode_id():
    current_color_key = get_current_colors_mode()
    colors_dict = get_colors_modes_dict()
    current_color_id = colors_dict[current_color_key]
    return current_color_id


class MenusColorsSettingsMixin(ABC):

    # Boolean atribut pro zobrazení instrukcí ovládání interaktivního menu
    show_instruction = abc_property("show_instruction")

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Metoda která přepne menu na nové menu
    show_menu = abc_method("show_menu")

    # Metoda která ukončí aktuální menu
    exit_menu = abc_method("exit_menu")


    def menus_colors_config(self):
        """Vrací data (nadpis a položky) pro hlavní menu"""

        title = "VYBERTE BAREVNÝ MOD:"
        items = [
            ("Zobrazení bez barev", lambda: set_colors_mode("native")),
            ("Mod pro tmavý režim", lambda: set_colors_mode("dark")),
            ("Mod pro světlý režimk", lambda: set_colors_mode("light")),
            ("Zpět do konfiguračního menu", lambda: self.show_menu("menus_config")),
            ("Ukončit", self.exit_menu)
        ]
        selected = 0
        return title, items, selected




