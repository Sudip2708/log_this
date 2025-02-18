from prompt_toolkit.key_binding import KeyBindings

from abc_helper import AbcSingletonMeta
from methods.key_bindings import SetupKeyBindingsMixin
from methods.menu_base import (
    ExitMenuMixin,
    ReloadMenuMixin,
    RunMenuMixin,
)
from methods.menu_get import (
    GetMenuTextMixin,
    GetInteractiveMenuMixin,
    GetMenuDataMixin,
    DisplayMenuMixin,
)
from methods.responses import (
    GetResponseMixin,
    InputCustomIntValueMixin,
)
from methods.menus import (
    MainMenuMixin,
    EndingMenuMixin,
    ConfigMenuMixin,
    SelectKeyMenuMixin,
    SelectValueMenuMixin,
)

class InteractiveCli(

    ### Základní metody:
    ExitMenuMixin,  # exit_menu()
    # Metoda uzavře aktuální interaktivní menu.
    # Používá atributy: 'current_menu'

    RunMenuMixin,  # run_menu()
    # Metoda načte a zobrazí aktuální nabídku interaktivního menu
    # Používá atributy: 'current_menu'
    # Používá metody: exit_menu()

    ReloadMenuMixin,  # reload_menu()
    # Metoda znovu načte data pro vykreselní menu
    # Použité atributy: 'current_menu'
    # Používá metody: run_menu()

    DisplayMenuMixin,  # display_menu(new_menu_name)
    # Přepne na nové menu
    # Používá atributy: 'menu_name', 'current_selection'
    # Používá metodu: get_menu_attributes(), reload_menu()

    SetupKeyBindingsMixin,  # setup_key_bindings()
    # Nastavení klávesových příkazů pro používání interaktivního menu
    # Používá atributy: 'kb', 'current_selection', 'menu_items'
    # Používá metodu: reload_menu(), exit_menu()


    ### Definice jednotlivých menu
    MainMenuMixin,  # get_main_menu()
    # Vrací data (nadpis a položky) pro hlavní menu.
    # Používá metody: display_menu(), exit_menu()

    EndingMenuMixin,  # get_ending_menu()
    # Vrací data (položky) pro ukončovací menu
    # Používá metody: display_menu(), exit_menu()

    ConfigMenuMixin,  # get_config_menu()
    # Vrací data (nadpis a položky) pro konfigurační menu.
    # Používá metody: display_menu()

    SelectKeyMenuMixin,  # get_select_key_menu()
    # Vrací data (nadpis a položky) pro menu pro výběr klíče.
    # Používá atributy: 'selected_key'
    # Používá metody: display_menu()

    SelectValueMenuMixin,  # get_select_value_menu()
    # Vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč.
    # Používá atributy: 'selected_key', 'selected_value'
    # Používá metody: display_menu()

    InputCustomIntValueMixin,  # input_custom_int_value()
    # Vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč.
    # Používá atributy: 'response', 'selected_key', 'selected_value'
    # Používá metody: display_menu(), run_menu()


    ### Get metody:
    GetMenuDataMixin,  # get_menu_data(menu_name)
    # Na základě 'menu_name' načte data pro požadované menu.
    # Používá metody: get_main_menu(), get_config_menu(), get_ending_menu(), get_select_key_menu(), get_select_value_menu()

    GetMenuTextMixin,  # get_menu_text()
    # Vrací naformátovaný text pro menu
    # Používá atributy: 'menu_title', 'menu_items', 'show_instruction', 'current_selection'

    GetInteractiveMenuMixin,  # get_interactive_menu()
    # Vytvoří interaktivní menu
    # Používá atributy: 'kb',
    # Používá metodu: get_menu_text()

    GetResponseMixin,  # get_response()
    # Vrací výstupní reakci na daný požadavek
    # Používá atributy: 'response', 'selected_key', 'selected_value'
    # Používá metody: display_menu(), run_menu(), input_custom_int_value()

    metaclass=AbcSingletonMeta  # Nastavení singleton instance
):

    ### Atributy použité v mixinech:
    show_instruction = False  # Boolean atribut pro zobrazení instrukcí ovládání interaktivního menu
    current_selection = 0  # Atribut pro zaznamenání vybrané položky
    current_menu = None # Atribut obsahující data aktuálního menu
    response = None  # Atribut pro zaznamenání požadavku na odpověď z interaktivního menu
    menu_name = None  # Atribut pro zaznamenání jaké menu má být zobrazeno
    menu_title = None  # Atribut pro zaznamenání nadpisu zobrazeného menu
    menu_items = None  # Atribut pro zaznamenání položek zobrazeného menu
    selected_key = None  # Atribut pro zaznamenání vybraného klíče
    selected_value = None  # Atribut pro zaznamenání vybrané hodnoty pro daný klíče
    kb = None  # Atribut pro instanci KeyBindings pro mapování kláves


    def __init__(self, menu_name):
        """Inicializační metoda pro interaktivní režim"""

        # Kontrola zda již proběhla inicializace
        if not hasattr(self, "_initialized"):

            # Inicializace třídy KeyBindings pro mapování kláves
            self.kb = KeyBindings()

            # Navázání kláves pro ovládání
            self.setup_key_bindings()

            # Nastavení atributu pro jméno menu
            self.menu_name = menu_name

            # Získání položek pro nadpis a položky menu
            self.get_menu_attributes()

            # Vytvoření interaktivního okna
            self.current_menu = self.get_interactive_menu()

            # Potvrzení o proběhlé inicializaci
            self._initialized = True


    def get_menu_attributes(self):
        """Na základě 'menu_name' vrátí obsah pro 'menu_title' a 'menu_items'"""
        self.menu_title, self.menu_items = self.get_menu_data()



