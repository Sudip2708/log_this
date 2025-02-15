from abc import ABC
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout

from abc_helper import abc_method, abc_property
from cli_styler import cli_style

class GetInteractiveMenuMixin(ABC):

    # Atribut obsahující instanci KeyBindings
    kb = abc_property("kb")

    # Vrací naformátovaný text pro menu
    get_menu_text = abc_method("get_menu_text")


    def get_interactive_menu(self):
        """Vytvoří interaktivní menu"""

        # Načtení formátovaného textu a obladačů pro výběr
        main_content = FormattedTextControl(
            text=self.get_menu_text,
            key_bindings=self.kb,
            focusable=True
        )

        # Vytvoření layoutu
        layout = Layout(
            HSplit([
                Window(
                    content=main_content,
                )
            ])
        )

        # Vytvoření aplikace
        return Application(
            layout=layout,
            full_screen=False,
            erase_when_done=False,
            style=cli_style
        )