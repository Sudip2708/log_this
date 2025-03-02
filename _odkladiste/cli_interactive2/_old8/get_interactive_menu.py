from abc import ABC
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout

from abc_helper import abc_method, abc_property

class GetInteractiveMenuMixin(ABC):

    # Atribut obsahující instanci KeyBindings
    kb = abc_property("kb")

    # Vrací naformátovaný text pro menu
    get_menu_text = abc_method("get_menu_text")


    def get_interactive_menu(self):
        """Vytvoří interaktivní menu"""

        # Načtení formátovaného textu a obladačů pro výběr
        main_content = FormattedTextControl(
            text=self.get_menu_text,  # Načtení textu
            key_bindings=self.kb,  # Načtení klávesových ovladačů
            focusable=True,  # Povolení klávesového ovládání
            show_cursor = False  # Skrytí kurzoru
        )

        # Vytvoření layoutu
        layout = Layout(
            HSplit([
                Window(
                    content=main_content,  # Přidání obsahu
                )
            ])
        )

        # Vytvoření aplikace
        return Application(
            layout=layout,  # Přidání layoutu
            full_screen=False,  # Nastavení zobrazení v dialogu konzole
            erase_when_done=False,  # Nastavení zobrazení předchozích příkazů
        )