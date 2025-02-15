# xxx4/interactive_cli.py
from mixins.get_menu_items import GetMenuItems
from mixins.get_app import GetApp
from prompt_toolkit.key_binding import KeyBindings

from mixins.get_key_bindings import GetKeyBindings
from mixins.get_menu_text import GetMenuText
from mixins.get_response import GetResponse
from singleton_meta import SingletonMeta

class InteractiveCli(
    GetMenuItems,
    GetKeyBindings,
    GetMenuText,
    GetResponse,
    GetApp,
    metaclass=SingletonMeta
):

    menu_items = None
    menu_title = None
    kb = KeyBindings()
    response = None
    current_selection = 0
    show_help = False


    def __init__(self, menu_type):

        if not hasattr(self, "_initialized"):  # 🔥 Ochrana proti opakované inicializaci

            self.current_selection = 0
            self.show_help = False
            self.response = None
            self.menu_type = menu_type

            # # Získání položek pro menu
            # self.menu_items = self.get_menu_items(menu_type)
            self.load_menu_items()

            # Získání navázaných kláves
            self.setup_key_bindings()

            # Vytvoření okna aplikace
            self.app = self.get_app()

            self._initialized = True

    def clear_response(self):
        self.response = None

    def load_menu_items(self):
        """Dynamicky načte menu podle aktuálního `menu_type`."""
        self.menu_title, self.menu_items = self.get_menu_items(self.menu_type)

    def switch_menu(self, new_menu_type):
        """Přepne menu na nový typ a obnoví obsah."""
        self.menu_type = new_menu_type
        self.current_selection = 0
        self.load_menu_items()
        self.app.invalidate()

    # Funkce pro ukončení interaktivního menu aplikace
    def exit(self):
        if self.app.is_running:
            self.app.exit()

    # Funkce pro zpuštění interaktivní nabídky
    def run(self):
        try:
            self.app.run()
        except Exception as e:
            print(f"Došlo k chybě: {e}")
            if self.app.is_running:
                self.app.exit()


