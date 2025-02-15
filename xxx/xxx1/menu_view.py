from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout


class MenuView:
    """Třída pro zobrazení menu"""

    def __init__(self, controller, key_bindings):
        self.controller = controller
        self.main_content = FormattedTextControl(
            self.get_menu_text,
            key_bindings=key_bindings.get_bindings(),
            focusable=True
        )

        self.layout = Layout(HSplit([Window(self.main_content)]))
        self.app = Application(
            layout=self.layout,
            full_screen=False,
            erase_when_done=False
        )

    def get_menu_text(self):
        lines = []

        if self.controller.show_help:
            lines.extend(self.get_help_text())

        for i, (text, _) in enumerate(self.controller.menu_items):
            if i == self.controller.current_selection:
                lines.append(('class:reverse', f'> {text}\n'))
            else:
                lines.append(('', f'  {text}\n'))

        return lines

    def get_help_text(self):
        return [
            ('', '\n'),
            ('class:bold', 'Nápověda:'),
            ('', '\n'),
            ('', '- Použijte šipky ↑↓ pro výběr položky'),
            ('', '\n'),
            ('', '- Stiskněte Enter pro potvrzení výběru'),
            ('', '\n'),
            ('', '- Ctrl+C pro ukončení'),
            ('', '\n'),
            ('', '\n')
        ]

    def refresh(self):
        if self.app.is_running:
            self.app.invalidate()

    def exit(self):
        if self.app.is_running:
            self.app.exit()

    def run(self):
        try:
            self.app.run()
        except Exception as e:
            print(f"Došlo k chybě: {e}")
            self.exit()
