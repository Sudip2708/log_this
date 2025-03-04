# print("_menus_settings/_menus_config/menus_config_colors_select.py")


class SelectColorsMenu:
    def __init__(self, menus_manager):

        # Navázání instance managera
        self.mm = menus_manager

        # Nadpis menu
        self.title = "VYBERTE BAREVNÝ MOD:"

        # Inicializace položek
        self.items = self.get_color_mode_items()


    def get_color_mode_items(self):
        """Dynamicky vygeneruje položky menu s označením aktuálního výběru."""

        # Načtní klíče aktuálního modu
        current_mode = self.mm.styler.color_mode

        # Vytvoření položek dle slovníku
        items = [
            (
                # Vytvoření labelu s přidáním označení aktuálně vybrané možnosti
                label + (" (selected)" if color_mode == current_mode else ""),

                # Lambda příkaz volající metodu pro změnu barevného režimu
                lambda mode=color_mode: self.color_mode_settings(mode)
            )
            # Cyklus procházející slovník a předávající jednotlivé položky
            for color_mode, label in self.mm.styler.color_modes.items()
        ]

        # Přidání statických položek
        items += [
            ("Zpět do předchozí nabídky", lambda: self.mm.show_menu("appearance_menu")),
            ("Ukončit", self.mm.exit_menu)
        ]
        return items


    def color_mode_settings(self, color_mode):
        """Nastaví barevný režim a obnoví menu."""

        # Změna barevného modu na instanci styleru
        self.mm.styler.set_color_mode(color_mode)

        # Změna instance ColorsModeSelectMenu
        self.mm.menus.refresh_select_colors_menu()

        # Načtení indexu pro aktuálně zvolenou položku
        self.mm.current_selection = self.mm.styler.get_current_color_mode_id()

        # Obnovíme menu, což znovu zavolá __init__ a aktualizuje položky
        self.mm.show_menu("select_colors_menu", target_reset=False)

