from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from typing import TYPE_CHECKING

# Importy pro typovou kontrolu:
if TYPE_CHECKING:
    from ..menus_manager import MenusManager

from ._key_bindings_manager import KeyBindingsManager
from ._get_menu_text import GetMenuText
from ._run_methods_mixins import RunMethodsMixin


class MenuRenderer(RunMethodsMixin):
    """
    Zpracování a vykreslování menu pomocí prompt_toolkit.

    Třída umožňuje vytvoření interaktivního menu pro CLI aplikaci.

    Mixiny:
        RunMethodsMixin - Mixin přidávající běhové metody
        # Přidává metody: run(), refresh(), exit(), is_running()
        # Používá atributy: 'menu_app'
    """

    # Instance CLI aplikace.
    menu_app: Application | None = None

    def __init__(self, menus_manager: "MenusManager") -> None:
        """
        Inicializuje renderer menu a nastaví klávesové zkratky i text menu.

        Args:
            menus_manager (object): Správce menu, který obsahuje informace o menu.

        Atributy:
            kb (KeyBindingsManager): Správce klávesových zkratek.
            get_menu_text (GetMenuText): Generátor textového obsahu menu.
            menu_app (Application | None): Instance CLI aplikace.
        """
        self.kb = KeyBindingsManager(menus_manager)
        self.get_menu_text = GetMenuText(menus_manager)
        self.menu_app = self.create_menu_app()

    def create_menu_app(self) -> Application:
        """
        Vytvoří a vrátí instanci CLI aplikace pro vykreslení menu.

        Returns:
            Application: Aplikace pro zobrazení menu.
        """
        main_content = FormattedTextControl(
            text=self.get_menu_text,  # Načtení textu
            key_bindings=self.kb(),  # Načtení klávesových ovladačů
            focusable=True,
            show_cursor=False
        )

        layout = Layout(
            HSplit([
                Window(content=main_content)
            ])
        )

        return Application(
            layout=layout,
            full_screen=False,
            erase_when_done=False
        )
