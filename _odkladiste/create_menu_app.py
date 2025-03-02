from abc import ABC
from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl

from abc_helper import abc_property, abc_method

class ControllersMethodsMixin(ABC):
    """Mixin pro spuštění, ukončení a obnovení interaktivního menu"""

    # Atribut pro instanci MenuRenderer
    application = abc_property("application")

    # Atribut pro metodu kb() instance KeyBindingsManager
    kb = abc_property("kb")

    # Metoda pro získání textu pro vykreslované menu
    get_menu_text = abc_method("get_menu_text")

    def create_display_app(self):
        """Vytvoří a vrátí interaktivní CLI aplikaci"""
        main_content = FormattedTextControl(
            text=self.get_menu_text,  # Načtení textu
            key_bindings=self.kb,  # Načtení klávesových ovladačů
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