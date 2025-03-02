# print("_manager.py")
from abc_helper import AbcSingletonMeta

from _methods_mixins import (
    NavigationMethodsMixin,
    RunMethodsMixin,
    LoopMethodsMixin
)

from _response_manager import ResponseManager
from _menu_render import MenuRenderer
from _menus_settings import MenuRegistry
from cli_styler import CliStyler


class InteractiveCliManager(

    NavigationMethodsMixin,
    # Mixin přidávající atribut a metody navigaci v interaktivním menu
    # Přidává atributy: 'current_selection'
    # Přidává metody: go_up(), go_down(), run_current_selection()
    # Používá atributy: 'menu_renderer', 'menu'

    RunMethodsMixin,
    # Mixin přidávající běhové metody a atribut pro definici odpovědi
    # Přidává atributy: 'response'
    # Přidává metody: run_menu(), exit_menu(), refresh_menu()
    # Používá atributy: 'menu_renderer'

    LoopMethodsMixin,
    # Mixin přidávající logiku pro vytvoření smyčky
    # Přidává metody: run_loop(), _response_loop(), _exit_response()
    # Používá atributy: 'response', 'response_manager'
    # Používá metody: 'run_menu', 'show_menu'

    metaclass=AbcSingletonMeta  # Nastavení singleton instance
):
    """
    Hlavní třída propojující jednotlivé komponenty CLI menu

    Atributy třídy:
        input_manager: Instace třídy 'InputManager' starající se správu vstupu od uživatele
        response_manager: Instance třídy 'ResponseManager' starajícíce o odpovědní reakci
        menu_renderer: Instance třídy 'MenuRenderer' starající se o vytvoření interaktivního menu
        menus_manager: Instance třídy 'MenusManager' starající se o správu jednotlivých menu
        menu_name: Zaznamenává název pro aktuálně zobrazené menu
        menu: Přístup k aktuálně vytvořenému menu třídou 'MenusManager'
        current_selection: Zaznameníví id zaměřené položky
        response: Zaznamenává požadavek na vytvoření odpovědi

    Metody třídy:
        go_up(): Definice akce pro klávesu 'šipka nahoru'
        go_down(): Definice akce pro klávesu 'šipka dolu'
        run_current_selection(): Definice akce pro klávesu 'enter'
        run_menu(): Spouští aktuálně vytvořené menu
        exit_menu(): Ukončuje aktuálně vytvořené menu
        refresh_menu(): Obnovuje aktuálně vytvořené menu
        show_menu(new_menu_name): Přepíná a zobrazuje nově vybrané menu
    """

    # Atributy použité v mixinech
    menu_name = None
    menus = None
    menu = None
    menu_renderer = None
    response_manager = None
    current_selection = 0  # Výchozí vybraná položka v menu
    response = None  # Odezva na akci
    show_instruction = False
    selected_value = None
    selected_key = None

    def __init__(self, menu_name):
        """Inicializační metoda singleton instance"""

        # Kontrola zda již proběhla inicializace
        if not hasattr(self, "_initialized"):

            # Napojení styleru pro zpracování výstupu
            self.styler = CliStyler()

            # Napojení manažera pro správu odpovědí
            self.response_manager = ResponseManager(self)

            # Napojení renderu pro zobrazení menu
            self.menu_renderer = MenuRenderer(self)

            # Napojení managera spravující jednotlivá menu
            self.menus = MenuRegistry(self)

            # Načtení menu k zobrazení
            self.menu = self.menus(menu_name)

            # Potvrzení o proběhlé inicializaci
            self._initialized = True

    def show_menu(self, new_menu_name):
        """Přepne na nové menu"""

        # Načtení menu k zobrazení
        self.menu = self.menus(new_menu_name)

        # Nastavení pozice výběru na první položku
        self.current_selection = 0

        # Obnovení zobrazení
        self.refresh_menu()

    # def colors_mode_settings(self, color_mode):
    #     set_colors_mode(color_mode)
    #     self.mm.show_menu("colors_select_menu")

    def toggle_show_instruction(self):
        self.show_instruction = not self.show_instruction

    def set_value_and_print(self, value):
        """Uloží vybranou hodnotu, vypíše výsledek a vrátí se do hlavního menu."""
        self.selected_value = value
        self.response = "print_new"
        self.exit_menu()

    def switch_to_set_key(self, key=None):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        if key:
            self.selected_key = key
            self.show_menu("select_value_menu")
        else:
            print("Není vybrán žádný klíč, zadejte klíč prosím znovu.")
            self.show_menu("select_key_menu")