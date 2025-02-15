from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from menu_actions import MenuActions
from utils import help_instructions

class InteractiveCli:
    def __init__(self):
        self.current_selection = 0
        self.show_help = False
        self.actions = MenuActions()
        self.menu_items = [
            ("Nápověda", self.actions.show_help),
            ("Zobrazit konfiguraci", self.actions.show_config),
            ("Nastavit hodnotu", self.actions.set_value),
            ("Ukončit", self.actions.exit_program)
        ]
        self.kb = KeyBindings()
        self.setup_key_bindings()
        self.main_content = FormattedTextControl(self.get_menu_text, key_bindings=self.kb, focusable=True)
        self.layout = Layout(HSplit([Window(self.main_content)]))
        self.app = Application(layout=self.layout, full_screen=False, erase_when_done=False)

    def setup_key_bindings(self):
        @self.kb.add('up')
        def handle_up(event):
            self.current_selection = max(0, self.current_selection - 1)

        @self.kb.add('down')
        def handle_down(event):
            self.current_selection = min(len(self.menu_items) - 1, self.current_selection + 1)

        @self.kb.add('enter')
        def handle_enter(event):
            self.menu_items[self.current_selection][1]()

        @self.kb.add('c-c')
        def handle_ctrl_c(event):
            self.actions.exit_program()

    def get_menu_text(self):
        lines = []
        if self.show_help:
            lines.extend(help_instructions())
        for i, (text, _) in enumerate(self.menu_items):
            lines.append(('class:reverse', f'> {text}\n') if i == self.current_selection else ('', f'  {text}\n'))
        return lines

    def run(self):
        try:
            self.app.run()
        except Exception as e:
            print(f"Došlo k chybě: {e}")
            if self.app.is_running:
                self.app.exit()