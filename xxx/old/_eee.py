from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML


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
        # Sestavení textu menu
        lines = []

        # Přidání nápovědy, pokud je aktivní
        if self.show_help:
            lines.extend([
                HTML('\n<b>Nápověda:</b>'),
                HTML('- Použijte šipky ↑↓ pro výběr položky'),
                HTML('- Stiskněte Enter pro potvrzení výběru'),
                HTML('- Ctrl+C pro ukončení\n')
            ])

        # Přidání položek menu
        for i, (text, _) in enumerate(self.menu_items):
            if i == self.current_selection:
                lines.append(HTML(f'<b>></b> <reverse>{text}</reverse>'))
            else:
                lines.append(HTML(f'  {text}'))

        return lines

    def show_help_handler(self):
        self.show_help = not self.show_help

    def show_config_handler(self):
        self.app.exit()
        print("\nAktuální konfigurace:")
        print("key1: value1")
        print("key2: value2")
        print("\nPro pokračování stiskněte Enter...")
        input()
        self.run()

    def set_value_handler(self):
        self.app.exit()
        key = input("\nZadejte klíč: ")
        value = input("Zadejte hodnotu: ")
        print(f"\nNastaveno: {key} = {value}")
        print("\nPro pokračování stiskněte Enter...")
        input()
        self.run()

    def exit_handler(self):
        self.app.exit()

    def run(self):
        try:
            self.app.run()
        except Exception as e:
            print(f"Došlo k chybě: {e}")
            self.exit_handler()


if __name__ == "__main__":
    print("Vítejte v interaktivním režimu!")
    print("--------------------------------")
    ImprovedInlineMenu().run()