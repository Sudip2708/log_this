# print("_menus_settings/_menus_config/menus_config_colors_select.py")

from cli_styler import styler
from .._base_menu import BaseMenu


class SelectColorsMenu(BaseMenu):

    # Definice nadpisu
    title = "VYBERTE BAREVNÝ MOD:"

    # Definice položek
    @property
    def items(self):

        # Načtní klíče aktuálního modu
        current_mode = styler.color_mode

        # Vytvoření položek dle slovníku
        items = [
            (
                # Vytvoření labelu s přidáním označení aktuálně vybrané možnosti
                label + (" (selected)" if color_mode == current_mode else ""),

                # Lambda příkaz volající metodu pro změnu barevného režimu
                lambda mode=color_mode: self.color_mode_settings(mode)
            )
            # Cyklus procházející slovník a předávající jednotlivé položky
            for color_mode, label in styler.color_modes.items()
        ]

        # Přidání doplňujících položek
        items += [
            ("Zpět do předchozí nabídky", self.show_appearance_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items



    # Metoda pro nastavení barev
    def color_mode_settings(self, color_mode):
        """Nastaví barevný režim a obnoví menu."""

        # Změna barevného modu na instanci styleru
        styler.set_color_mode(color_mode)

        # Změna instance ColorsModeSelectMenu
        self.mm.menus.refresh_select_colors_menu()

        # Uložení změny do souboru (je-li) používán
        if self.mm.config_manager.file_manager:
            color_mode_id = styler.get_current_color_mode_id()
            self.mm.config_manager.file_manager.change_value("colors", color_mode_id)

        # Načtení indexu pro aktuálně zvolenou položku
        self.mm.current_selection = styler.get_current_color_mode_id()

        # Obnovíme menu, což znovu zavolá __init__ a aktualizuje položky
        self.mm.show_menu("select_colors_menu", target_reset=False)


    # Metoda pro přepnutí na menu pro nastavení vzhledu
    def show_appearance_menu(self):
        self.mm.show_menu("appearance_menu")
