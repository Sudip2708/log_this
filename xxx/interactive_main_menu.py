from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout
from prompt_toolkit.key_binding import KeyBindings

from help_instructions import help_instructions
from print_response import PrintResponse
from setup_key_bindings import setup_key_bindings


class ImprovedInlineMenu:
    def __init__(self, menu_type="main"):
        self.current_selection = 0
        self.show_help = False
        self.menu_type = menu_type

        # Definice menu položek podle typu menu
        if menu_type == "main":
            self.menu_items = [
                ("Nápověda", self.show_help_handler),
                ("Zobrazit konfiguraci", self.show_config_handler),
                ("Nastavit hodnotu", self.set_value_handler),
                ("Ukončit", self.exit_handler)
            ]

        # Vytvoření klávesových zkratek
        self.kb = KeyBindings()
        self.setup_key_bindings()

        # Vytvoření hlavního obsahu
        self.main_content = FormattedTextControl(
            self.get_menu_text,
            key_bindings=self.kb,
            focusable=True
        )

        # Vytvoření layoutu
        self.layout = Layout(
            HSplit([
                Window(self.main_content)
            ])
        )

        # Vytvoření aplikace
        self.app = Application(
            layout=self.layout,
            full_screen=False,
            erase_when_done=False
        )

    def setup_key_bindings(self):
        setup_key_bindings(self)

    def get_menu_text(self):
        lines = []

        # Přidání nápovědy, pokud je aktivní
        if self.show_help:
            lines.extend(help_instructions())

        # Přidání položek menu
        for i, (text, _) in enumerate(self.menu_items):
            if i == self.current_selection:
                lines.append(('class:reverse', f'> {text}\n'))
            else:
                lines.append(('', f'  {text}\n'))

        return lines

    def show_help_handler(self):
        self.show_help = not self.show_help

    def show_config_handler(self):
        """Ukončí menu, vypíše konfiguraci a pak ho znovu spustí."""
        PrintResponse.response = "print_configuration"
        self.app.exit()

    def set_value_handler(self):
        PrintResponse.response = "set_value"
        self.app.exit()

    def exit_handler(self):
        PrintResponse.response = None
        if self.app.is_running:
            self.app.exit()

    def run(self):
        try:
            self.app.run()
        except Exception as e:
            print(f"Došlo k chybě: {e}")
            if self.app.is_running:
                self.app.exit()







