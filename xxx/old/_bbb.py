from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.widgets import RadioList, Frame, Box
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style


def custom_radiolist_dialog(title, values):
    """Vlastní radiolist dialog bez tlačítka OK a Cancel, výběr se provede Enterem."""

    # Vytvoření radiolist widgetu
    radio_list = RadioList(values)

    # Key bindings (Enter ukončí aplikaci s vybranou hodnotou)
    kb = KeyBindings()

    @kb.add("enter")
    def _(event):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
        event.app.exit(result=radio_list.current_value)

    # Vytvoření layoutu s Boxem (Frame pro titulek)
    frame = Frame(
        Box(radio_list, padding=1),
        title=title
    )

    # Vytvoření aplikace s full_screen=False
    app = Application(
        layout=Layout(frame),
        key_bindings=kb,
        full_screen=False  # Zabrání fullscreen režimu
    )

    return app.run()


def run_interactive_teaser() -> None:
    """Spustí interaktivní režim a zobrazí hlavní menu."""

    result = custom_radiolist_dialog(
        title="Chcete pokračovat skrze interaktivní režim?",
        values=[
            ("interactive", "Zpustit interaktivní režim"),
            ("help", "Zobrazit nápovědu"),
            ("exit", "Opustit tento dialog")
        ]
    )

    print(f"Vybraná možnost: {result}")


run_interactive_teaser()
