# print("_menus_settings/_key_and_value_config/config_value_select.py")
from .._base_menu import BaseMenu
from functools import partial
from cli_styler import styler

class SelectValueMenu(BaseMenu):

    # Pojmenování menu (klíč pod kterým je volatelné)
    menu_name = "select_value_menu"

    menu_help = (
        "Zobrazit konfiguraci - Přístup k menu pro zobrazení aktuální konfigurace",
        "Nastavit konfiguraci - Přístup k menu pro změnu konfigurace",
        "Import/Export konfigurace - Přístup k menu pro import a export konfigurace",
        "Nastavení vzhledu interaktivního režimu - Přístup k menu pro nastavení vzhledu dialogových oken"
    )

    _input = None
    _key = None
    _mode_class = None

    # Definice nadpisu
    @property
    def title(self):

        # Načtení klíče
        self._key = self.mm.selected_key
        self._mode_class = self.get_mode_class()

        if not self._key:
            raise ValueError("Není zadán klíč, pro který se má zadat hodnota")


        title = self._mode_class.VALUES_TITLE
        return (
            title if title else
            f"VYBERTE HODNOTU PRO {self._key.upper()}:"
        )

    # Definice položek
    @property
    def items(self):


        # Nápověda k této sekci
        items = [
            ("Nápověda", self.show_help),
        ]

        # Vytvoření položek dle slovníku
        items += [
            (
                # Vytvoření labelu s přidáním označení aktuálně vybrané možnosti
                label
                + (
                    " (default)"
                    if value == self._mode_class.DEFAULT_VALUE
                    else ""
                )
                + (
                    " (selected)"
                    if value == self.mm.config_manager.config.get(self._key)
                    else ""
                )
                ,

                # Partial příkaz volající metodu pro změnu barevného režimu
                partial(self.request_processing,value)
            )

            # Cyklus procházející slovník a předávající jednotlivé položky
            for value, label in self._mode_class.VALUES_DICT.items()
        ]

        # Přidání statických položek
        items += [
            ("Zpět na předchozí menu", self.go_to_previous_menu),
            ("Ukončit", self.mm.close_interactive_mode)
        ]

        return items

    # Metoda pro získání třídy
    def get_mode_class(self):
        """Vrátí třídu s daty klíče"""
        return self.mm.config_manager.items_manager.KEYS_DATA[self._key]

    # Metoda pro zadání celočíselné hodnoty (rozmezí 1 - 1000)
    def show_help(self):
        pass

    # Metoda pro zpracování požadavku
    def request_processing(self, value):

        # Zpracování nastavení styleru
        if self._key in ("colors", "symbols"):
            self.set_styler(value)

        # Zpracování požadavku na zadání vlastní hodnoty
        elif value == "input":
            self.input_custom_int_value()

        # Zpracování ostatních požadavků
        else:
            self.set_value_and_print(value)

    # Metoda pro uložení a vytisknutí vybraného klíče a hodnoty
    def set_value_and_print(self, value):
        self.mm.selected_value = value
        self.mm.config_manager.change_value(
            self.mm.selected_key,
            self.mm.selected_value
        )
        self.mm.exit_menu()

    # Metoda pro zadání celočíselné hodnoty (rozmezí 1 - 1000)
    def input_custom_int_value(self):
        self.mm.response = "input_int_value"
        self.mm.exit_menu()

    # Metoda pro přepnutí na konfigurační menu
    def go_to_previous_menu(self):
        self.mm.show_menu("select_key_menu")

    # Metoda pro nastavení styleru
    def set_styler(self, value):

        # Změna setu na styleru
        styler.change_mode(self._key,value)

        # Uložení změny do souboru (je-li) používán
        file_manager = self.mm.config_manager.file_manager
        if file_manager:
            self.mm.config_manager.change_value(self._key, value, silent=True)

        # Načtení indexu pro aktuálně zvolenou položku
        option_id = self.mm.config_manager.current_id(self._key)
        self.mm.current_selection = option_id + 1  # plus 1 je zde kuli položce nápovědy

        # Obnovíme menu, což znovu zavolá __init__ a aktualizuje položky
        self.mm.show_menu("select_value_menu", target_reset=False)


