from abc import ABC, abstractmethod
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout


class GetApp(ABC):

    @property
    @abstractmethod
    def menu_items(self):
        pass

    @abstractmethod
    def get_menu_text(self):
        pass

    @property
    @abstractmethod
    def kb(self):
        pass

    def get_app(self):

        # Načtení formátovaného textu a obladačů pro výběr
        main_content = FormattedTextControl(
            text=self.get_menu_text,
            key_bindings=self.kb,
            focusable=True
        )

        # Vytvoření layoutu
        layout = Layout(
            HSplit([
                Window(main_content)
            ])
        )

        # Vytvoření aplikace
        return Application(
            layout=layout,
            full_screen=False,
            erase_when_done=False
        )