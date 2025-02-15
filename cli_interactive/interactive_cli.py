from prompt_toolkit.key_binding import KeyBindings

from utils.singleton_meta import SingletonMeta

from zmehods import (
GetMenuAttributesMixin,
GetMenuDataMixin,
SetResponseMixin,
RunMenuMixin,
SetupKeyBindingsMixin,
GetMenuText,
GetInteractiveMenuMixin,
)

from zmenus import (
GetMainMenuMixin,
GetEndingMenuMixin,
GetConfigMenuMixin,
GetSelectKeyMenuMixin,
GetSelectValueMenuMixin,
)

from zatributes import (
ExitMenuMixin,
ClearResponseMixin,
ReloadMenuMixin,
)


class InteractiveCli(

    ### Metody pracující čistě s atributy: ###

    ExitMenuMixin,  # self.exit_menu()
    # Metoda uzavře aktuální interaktivní menu.
    # Používá atributy: 'interactive_menu'

    ClearResponseMixin,  # self.clear_response()
    # Metoda přepíše obsah atributu 'response' na None
    # Použité atributy: 'response'

    ReloadMenuMixin,  # self.reload_menu()
    # Metoda znovu načte data pro vykreselní menu
    # Použité atributy: 'interactive_menu'

    GetMenuText,  # self.get_menu_text()
    # Vrací naformátovaný text pro menu
    # Používá atributy: 'menu_title', 'menu_items', 'show_instruction', 'current_selection'

    GetInteractiveMenuMixin,  # self.get_interactive_menu()
    # Vytvoří interaktivní menu
    # Používá atributy: 'kb',
    # Používá metodu: get_menu_text()


    ### Metody se závislostí na atributních metodách: ###

    RunMenuMixin,  # self.run_menu()
    # Metoda načte a zobrazí aktuální nabídku interaktivního menu
    # Používá atributy: 'interactive_menu'
    # Používá metody: exit_menu()

    SetResponseMixin,  # self.set_response(request)
    # Nastaví atribut 'response' na požadovaný úkon a ukončí menu
    # Používá atributy: 'response'
    # Používá metody: exit_menu()

    SetupKeyBindingsMixin,  # Nastavení klávesových příkazů pro používání interaktivního menu
    # Používá atributy: 'kb', 'current_selection', 'menu_items'
    # Používá metodu: reload_menu(), exit_menu()


    ### Metody pro položky menu: ###

    GetMainMenuMixin,  # self.get_main_menu()
    # Vrací data (nadpis a položky) pro hlavní menu.
    # Používá metody: set_response(), switch_menu(), exit_menu()

    GetEndingMenuMixin,  # self.get_ending_menu()
    # Vrací data (položky) pro ukončovací menu
    # Používá metody: switch_menu(), exit_menu()

    GetConfigMenuMixin,  # self.get_config_menu()
    # Vrací data (nadpis a položky) pro konfigurační menu.
    # Používá metody: switch_menu()

    GetSelectKeyMenuMixin,  # self.get_select_key_menu()
    # Vrací data (nadpis a položky) pro menu pro výběr klíče.
    # Používá atributy: 'selected_key'
    # Používá metody: switch_menu()

    GetSelectValueMenuMixin,  # self.get_select_value_menu()
    # Vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč.
    # Používá atributy: 'selected_key', 'selected_value'
    # Používá metody: switch_menu(), set_response()


    ### Metody pro vykreslení menu: ###

    GetMenuDataMixin,  # self.get_menu_data(menu_name)
    # Na základě 'menu_name' načte data pro požadované menu.
    # Používá metody: get_main_menu(), get_config_menu(), get_ending_menu(), get_select_key_menu(), get_select_value_menu()

    GetMenuAttributesMixin,  # self.get_menu_attributes()
    # Na základě 'menu_name' vrátí obsah pro 'menu_title' a 'menu_items'.
    # Používá atributy: 'menu_name', 'menu_title', 'menu_items'
    # Používá metody: get_menu_data()

    metaclass=SingletonMeta  # Nastavení singleton instance
):

    # Atributy použité v mixinech:
    interactive_menu = None # Atribut obsahující data aktuálního menu
    show_instruction = False  # Boolean atribut pro zobrazení instrukcí ovládání interaktivního menu
    current_selection = 0  # Atribut pro zaznamenání vybrané položky
    response = None  # Atribut pro zaznamenání požadavku na odpověď z interaktivního menu
    menu_name = None  # Atribut pro zaznamenání jaké menu má být zobrazeno
    menu_title = None  # Atribut pro zaznamenání nadpisu zobrazeného menu
    menu_items = None  # Atribut pro zaznamenání položek zobrazeného menu
    selected_key = None  # Atribut pro zaznamenání vybraného klíče
    selected_value = None  # Atribut pro zaznamenání vybrané hodnoty pro daný klíče
    kb = KeyBindings()  # Atribut obsahující instanci KeyBindings


    def __init__(self, menu_name):

        if not hasattr(self, "_initialized"):

            # Navázání kláves pro ovládání
            self.setup_key_bindings()

            # Nastavení atributu pro jméno menu
            self.menu_name = menu_name

            # Získání položek pro nadpis a položky menu
            self.get_menu_attributes()

            # Vytvoření okna aplikace
            self.interactive_menu = self.get_interactive_menu()

            self._initialized = True

    def switch_menu(self, new_menu_name):
        """Přepne na nové menu"""
        # Důvod přítomnosti této metody zde je aby nedošlo k zacyklenému volání metod
        self.menu_name = new_menu_name
        self.current_selection = 0
        self.get_menu_attributes()
        self.reload_menu()



