from prompt_toolkit import Application, PromptSession
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout
from prompt_toolkit.key_binding import KeyBindings


class ImprovedInlineMenu:
    def __init__(self):
        self.current_selection = 0
        self.show_help = False

        # Definice menu položek (text, handler funkce)
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

        # Vytvoření session pro bezpečný prompt
        self.session = PromptSession()

    def setup_key_bindings(self):
        @self.kb.add('up')
        def handle_up(event):
            self.current_selection = max(0, self.current_selection - 1)

        @self.kb.add('down')
        def handle_down(event):
            self.current_selection = min(len(self.menu_items) - 1,
                                         self.current_selection + 1)

        @self.kb.add('enter')
        def handle_enter(event):
            # Zavolá handler funkci pro vybranou položku
            self.menu_items[self.current_selection][1]()

        @self.kb.add('c-c')
        def handle_ctrl_c(event):
            self.exit_handler()

    def get_menu_text(self):
        lines = []

        # Přidání nápovědy, pokud je aktivní
        if self.show_help:
            lines.extend([
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
            ])

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
        self.app.exit()
        print("\nAktuální konfigurace:")
        print("key1: value1")
        print("key2: value2")

        # Vytvoření nového menu pro pokračování
        continue_menu = ImprovedInlineMenu()
        continue_menu.menu_items = [
            ("Pokračovat v interaktivním režimu", self.continue_handler),
            ("Ukončit interaktivní režim", self.exit_handler)
        ]
        # Čekání na Enter před zobrazením menu
        self.session.prompt('\nPro pokračování stiskněte Enter...')
        self.run()

    def set_value_handler(self):
        self.app.exit()
        # Použijeme session.prompt místo input()
        key = self.session.prompt("\nZadejte klíč: ")
        value = self.session.prompt("Zadejte hodnotu: ")
        print(f"\nNastaveno: {key} = {value}")

        # Vytvoření nového menu pro pokračování
        continue_menu = ImprovedInlineMenu()
        continue_menu.menu_items = [
            ("Pokračovat v interaktivním režimu", self.continue_handler),
            ("Ukončit interaktivní režim", self.exit_handler)
        ]
        self.session.prompt('\nPro pokračování stiskněte Enter...')
        continue_menu.run()

    def continue_handler(self):
        self.app.exit()
        self.__class__().run()

    def exit_handler(self):
        if self.app.is_running:
            self.app.exit()

    def run(self):
        try:
            self.app.run()
        except Exception as e:
            print(f"Došlo k chybě: {e}")
            if self.app.is_running:
                self.app.exit()


if __name__ == "__main__":
    print("Vítejte v interaktivním režimu!")
    print("--------------------------------")
    ImprovedInlineMenu().run()