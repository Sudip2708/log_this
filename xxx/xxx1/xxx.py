# config.py
class Config:
    """Třída pro správu konfigurace"""

    def __init__(self):
        self.settings = {
            "key1": "value1",
            "key2": "value2"
        }

    def get_value(self, key):
        return self.settings.get(key)

    def set_value(self, key, value):
        self.settings[key] = value

    def print_configuration(self):
        print("Aktuální konfigurace:")
        for key, value in self.settings.items():
            print(f"{key}: {value}")


# key_bindings.py
from prompt_toolkit.key_binding import KeyBindings


class MenuKeyBindings:
    """Třída pro správu klávesových zkratek"""

    def __init__(self, menu_controller):
        self.controller = menu_controller
        self.kb = KeyBindings()
        self.setup_key_bindings()

    def setup_key_bindings(self):
        @self.kb.add('up')
        def handle_up(event):
            self.controller.move_selection(-1)

        @self.kb.add('down')
        def handle_down(event):
            self.controller.move_selection(1)

        @self.kb.add('enter')
        def handle_enter(event):
            self.controller.select_current_item()

        @self.kb.add('c-c')
        def handle_ctrl_c(event):
            self.controller.exit()

    def get_bindings(self):
        return self.kb


# menu_controller.py
class MenuController:
    """Třída pro řízení logiky menu"""

    def __init__(self, view, config):
        self.view = view
        self.config = config
        self.current_selection = 0
        self.show_help = False
        self.menu_items = self.initialize_menu_items()

    def initialize_menu_items(self):
        return [
            ("Nápověda", self.toggle_help),
            ("Zobrazit konfiguraci", self.show_configuration),
            ("Nastavit hodnotu", self.set_value),
            ("Ukončit", self.exit)
        ]

    def move_selection(self, direction):
        new_selection = self.current_selection + direction
        if 0 <= new_selection < len(self.menu_items):
            self.current_selection = new_selection
            self.view.refresh()

    def select_current_item(self):
        self.menu_items[self.current_selection][1]()

    def toggle_help(self):
        self.show_help = not self.show_help
        self.view.refresh()

    def show_configuration(self):
        self.config.print_configuration()
        self.exit()

    def set_value(self):
        key = input("\nZadejte klíč: ")
        value = input("Zadejte hodnotu: ")
        self.config.set_value(key, value)
        print(f"\nNastaveno: {key} = {value}")
        self.exit()

    def exit(self):
        self.view.exit()


# menu_view.py
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


# main.py
def main():
    print("Vítejte v interaktivním režimu:")
    print("--------------------------------")

    config = Config()
    while True:
        view = MenuView(None, None)  # Dočasné None hodnoty
        controller = MenuController(view, config)
        key_bindings = MenuKeyBindings(controller)
        view.controller = controller  # Nastavení controller reference
        view.main_content.key_bindings = key_bindings.get_bindings()

        view.run()
        if not controller.menu_items[controller.current_selection][
                   0] == "Ukončit":
            continue
        else:
            print("Ukončuji interaktivní režim...")
            break


if __name__ == "__main__":
    main()