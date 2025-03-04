# print("_menus_settings/_menus_config/menus_config_symbols_select.py")

class SelectSymbolsMenu:

    def proxy_method(self):
        pass

    def __init__(self, menus_manager):

        # Navázání instance managera
        self.mm = menus_manager

        # Nadpis menu
        self.title = "VYBERTE SET ZNAČEK:"

        # Dynamicky generované položky menu podle slovníku symbol_mode_settings
        self.items = self.get_symbol_mode_items()


    def get_symbol_mode_items(self):
        """Dynamicky vygeneruje položky menu s označením aktuálního výběru."""

        # Načtní klíče aktuálního modu
        current_mode = self.mm.styler.symbol_mode

        # Vytvoření položek dle slovníku
        items = [
            (
                # Vytvoření labelu s přidáním označení aktuálně vybrané možnosti
                label + (" (selected)" if symbol_mode == current_mode else ""),

                # Lambda příkaz volající metodu pro změnu barevného režimu
                lambda mode=symbol_mode: self.symbol_mode_settings(mode)
            )
            # Cyklus procházející slovník a předávající jednotlivé položky
            for symbol_mode, label in self.mm.styler.symbol_modes.items()
        ]

        # Přidání statických položek
        items += [
            ("Zpět do předchozí nabídky", lambda: self.mm.show_menu("appearance_menu")),
            ("Ukončit", self.mm.exit_menu)
        ]
        return items


    def symbol_mode_settings(self, symbol_mode):

        # Změna barevného modu na instanci styleru
        self.mm.styler.set_symbol_mode(symbol_mode)
        
        # Změna instance ColorsModeSelectMenu
        self.mm.menus.refresh_select_symbols_menu()

        # Načtení indexu pro aktuálně zvolenou položku
        self.mm.current_selection = self.mm.styler.get_current_symbol_mode_id()

        # Přepnutí na menu s ponechání current_selection
        self.mm.show_menu("select_symbols_menu", target_reset=False)
