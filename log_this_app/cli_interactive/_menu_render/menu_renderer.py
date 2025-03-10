# print("_menu_render/menu_renderer.py")
from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl

from ._key_bindings_manager import KeyBindingsManager
from ._get_menu_text import GetMenuText
from ._run_methods_mixins import RunMethodsMixin


class MenuRenderer(

    RunMethodsMixin,
    # Mixin přidávající běhové metody
    # Přidává metody: run(), refresh(), exit(), is_running()
    # Používá atributy: 'menu_app'

):
    """Zpracování a vykreslování menu pomocí prompt_toolkit"""

    # Atributy použité v mixinech
    menu_app = None

    def __init__(self, menus_manager):

        # Načtení ovladače kláves
        self.kb = KeyBindingsManager(menus_manager)

        # Načtení textu k zobrazení
        self.get_menu_text = GetMenuText(menus_manager)

        # Volání metody pro vytvoření a zobrazení menu
        self.menu_app = self.create_menu_app()


    def create_menu_app(self):
        """Vytvoří a vrátí interaktivní CLI aplikaci"""

        # Vytvoření hlavního obsahu
        main_content = FormattedTextControl(
            text=self.get_menu_text,  # Načtení textu
            key_bindings=self.kb(),  # Načtení klávesových ovladačů
            focusable=True,
            show_cursor=False
        )

        # Přidání hlavního obsahu do layoutu
        layout = Layout(
            HSplit([
                Window(content=main_content)
            ])
        )

        # Vytvoření a vrácení aplikace pro vykreslení menu
        return Application(
            layout=layout,
            full_screen=False,
            erase_when_done=False
        )



