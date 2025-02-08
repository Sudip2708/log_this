from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window, HSplit, VSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.widgets import RadioList, Button, Box
from prompt_toolkit.formatted_text import HTML


# Příklad 2: Interaktivní fullscreen menu s výpisem
class FullscreenMenu:
    def __init__(self):
        self.output_text = ""
        self.current_screen = "main"

        # Vytvoření radio listu pro hlavní menu
        self.main_menu = RadioList([
            ("show", "Zobrazit konfiguraci"),
            ("set", "Nastavit hodnotu"),
            ("exit", "Ukončit")
        ])

        # Vytvoření klávesových zkratek
        self.kb = KeyBindings()

        @self.kb.add('c-c')
        def _(event):
            event.app.exit()

        # Vytvoření layoutu
        self.layout = Layout(
            HSplit([
                # Místo pro výpis
                Window(
                    FormattedTextControl(self.get_output_text),
                    height=10
                ),
                # Menu
                self.main_menu,
                # Tlačítka
                VSplit([
                    Button("OK", handler=self.handle_ok),
                    Button("Cancel", handler=self.handle_cancel)
                ])
            ])
        )

        # Vytvoření aplikace
        self.app = Application(
            layout=self.layout,
            key_bindings=self.kb,
            full_screen=True
        )

    def get_output_text(self):
        if self.current_screen == "show":
            return HTML(f"<b>Aktuální konfigurace:</b>\n{self.output_text}")
        return ""

    def handle_ok(self):
        selected = self.main_menu.current_value
        if selected == "show":
            self.current_screen = "show"
            self.output_text = "key1: value1\nkey2: value2\n"  # Zde by byl skutečný výpis konfigurace
        elif selected == "exit":
            self.app.exit()

    def handle_cancel(self):
        self.app.exit()

    def run(self):
        self.app.run()


# Příklad 3: Inline menu v terminálu
class InlineMenu:
    def __init__(self):
        self.kb = KeyBindings()

        @self.kb.add('enter')
        def _(event):
            self.handle_enter(event)

        self.choices = [
            ("show", "Zobrazit konfiguraci"),
            ("set", "Nastavit hodnotu"),
            ("exit", "Ukončit")
        ]

        self.menu = RadioList(self.choices)

        self.layout = Layout(
            HSplit([
                self.menu,
                Window(height=1),  # Mezera
                Button("OK", handler=self.handle_ok)
            ])
        )

        self.app = Application(
            layout=self.layout,
            key_bindings=self.kb,
            full_screen=False,
            erase_when_done=False
        )

    def handle_ok(self):
        selected = self.menu.current_value
        if selected == "show":
            self.app.exit()
            print("\nAktuální konfigurace:")
            print("key1: value1")
            print("key2: value2")
            print("\nPro pokračování stiskněte Enter...")
            input()
            self.run()
        elif selected == "exit":
            self.app.exit()

    def handle_enter(self, event):
        # Pokud je fokus na menu, přesuneme ho na OK tlačítko
        if self.layout.has_focus(self.menu):
            self.layout.focus_next()

    def run(self):
        self.app.run()


# Příklad použití
if __name__ == "__main__":
    # Vyzkoušejte jeden z následujících řádků:
    FullscreenMenu().run()
    # InlineMenu().run()