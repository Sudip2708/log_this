# print("_manager.py")
import traceback

from abc_helper import AbcSingletonMeta
from cli_styler import styler

from ._methods_mixins import (
    NavigationMethodsMixin,
    RunMethodsMixin,
    LoopMethodsMixin
)

from ._response_manager import ResponseManager
from ._menu_render import MenuRenderer
from ._menus_settings import MenuRegister


class MenusManager(

    NavigationMethodsMixin,
    # Mixin přidávající atribut a metody navigaci v interaktivním menu
    # Přidává atributy: 'selected_item_id '
    # Přidává metody: go_up(), go_down(), run_selected_item_id ()
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
        selected_item_id : Zaznameníví id zaměřené položky
        response: Zaznamenává požadavek na vytvoření odpovědi

    Metody třídy:
        go_up(): Definice akce pro klávesu 'šipka nahoru'
        go_down(): Definice akce pro klávesu 'šipka dolu'
        run_selected_item_id (): Definice akce pro klávesu 'enter'
        run_menu(): Spouští aktuálně vytvořené menu
        exit_menu(): Ukončuje aktuálně vytvořené menu
        refresh_menu(): Obnovuje aktuálně vytvořené menu
        show_menu(new_menu_name): Přepíná a zobrazuje nově vybrané menu
    """

    # Atributy použité v mixinech
    menu_name = None
    menus = None
    current_menu = None
    menu_renderer = None
    response_manager = None
    selected_item_id  = 0  # Výchozí vybraná položka v menu
    response = None  # Odezva na akci
    show_instruction = False
    selected_value = None
    selected_key = None
    styler = None
    continue_with_menu = False

    def __init__(self, config_manager):
        """Inicializační metoda singleton instance"""

        # Kontrola zda již proběhla inicializace
        if not hasattr(self, "_initialized"):

            # Napojení na hlavní třídu LogThisManager
            self.config_manager = config_manager

            # Napojení managera pro zprávu klávesových zkratek
            # self.key_bindings = KeyBindingsManager(self)

            # Napojení manažera pro správu odpovědí
            self.response_manager = ResponseManager(self)

            # Napojení renderu pro zobrazení menu
            self.menu_renderer = MenuRenderer(self)

            # Napojení managera spravující jednotlivá menu
            self.menu_register = MenuRegister(self)

            # Potvrzení o proběhlé inicializaci
            self._initialized = True


    def show_menu(self, menu_name, target_reset=True):
        """Přepne na nové menu"""

        # Přiřazení jména menu do atriutu
        self.menu_name = menu_name

        # Načtení menu k zobrazení
        self.current_menu = self.menu_register(menu_name)

        # Nastavení pozice výběru na první položku
        if target_reset:
            self.selected_item_id  = 0

        # Obnovení zobrazení
        self.refresh_menu()

    # Metoda uzavře interaktivní režim
    def close_interactive_mode(self):
        self.response = "exit"
        self.exit_menu()

    # Metoda pro přepnutí na hlavní menu
    def show_main_menu(self):
        self.show_menu("main_menu")


    # Metoda pro zpuštění interaktivního menu
    def run_interactive_menu(self, menu_name="main_menu", silent=False):
        """Spustí interaktivní CLI režim"""
        try:
            # Zobrazení nadpisu (je-li požadováno)
            if not silent:
                styler.cli_print.intro.title(
                    "VÍTEJTE V INTERAKTIVNÍM REŽIMU!"
                )
            # Přiřazení jména menu do atriutu
            self.menu_name = menu_name
            # Načtení menu k zobrazení
            self.current_menu = self.menu_register(menu_name)
            # Spuštění hlavní smyčky
            self.run_loop()


        # Zachycení nepodchycených chyb
        except Exception as e:
            print(f"Došlo k neočekávané chybě: {str(e)}")
            print(traceback.format_exc())


    # Metoda pro zobrazení a skrytí nápovědy
    def toggle_show_instruction(self):
        self.show_instruction = not self.show_instruction

    # Metoda vrátí třídu aktuálního menu
    def get_actual_menu_class(self):
        return self.menu_register(self.menu_name)



