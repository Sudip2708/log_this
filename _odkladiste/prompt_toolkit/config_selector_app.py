from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, VSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import Button, Label, Box
from prompt_toolkit.styles import Style

from .all_mixins import AllMixins


class ConfigSelectorApp(AllMixins):

    def __init__(self, options):
        """
        Inicializuje aplikaci pro výběr klíče a hodnoty.

        Args:
            options (dict): Slovník s klíči a odpovídajícími možnostmi hodnot.
        """
        self.options = options
        self.selected_key = None
        self.selected_value = None
        self.message = Label("")  # Dynamický výstup pro potvrzení nebo chyby
        self.key_list = list(options.keys())
        self.current_key_index = 0

        # Styl aplikace
        self.style = Style.from_dict({
            "button": "bg:#007BFF #FFFFFF",
            "button.focused": "bg:#0056b3 #FFFFFF",
            "message": "fg:#00FF00 bold",
        })

        # Klávesové zkratky
        self.bindings = KeyBindings()
        self.bindings.add("q")(self.exit_application)
        self.bindings.add("up")(self.move_up)
        self.bindings.add("down")(self.move_down)
        self.bindings.add("enter")(self.confirm_selection)

        # Hlavní rozložení
        self.layout = Layout(self.create_main_container())

        # Aplikace
        self.app = Application(
            layout=self.layout,
            key_bindings=self.bindings,
            full_screen=True,
            style=self.style,
        )

    def exit_application(self, _):
        """
        Ukončí aplikaci.
        """
        self.app.exit()

    def run(self):
        """
        Spustí aplikaci.
        """
        self.app.run()


# Příklad použití
if __name__ == "__main__":
    config_options = {
        "color": ["red", "blue", "green"],
        "size": ["small", "medium", "large"],
        "shape": ["circle", "square", "triangle"],
    }
    app = ConfigSelectorApp(config_options)
    app.run()
