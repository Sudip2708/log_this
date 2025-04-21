from typing import Callable, Protocol
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.named_commands import KeyPressEvent

class MenuNavigator(Protocol):
    """Protokol definující rozhraní pro navigaci v menu."""
    def go_up(self) -> None: ...
    def go_down(self) -> None: ...
    def run_selected_item_id (self) -> None: ...
    def exit_menu(self) -> None: ...

class MenuKeyBindings:
    """Flexibilní správa klávesových vazeb s dependency injection."""

    def __init__(
        self,
        navigator: MenuNavigator,
        key_config: dict[str, Callable[[KeyPressEvent], None]] = None
    ):
        """
        Inicializace klávesových vazeb s možností vlastní konfigurace.

        Args:
            navigator: Objekt implementující navigační metody menu
            key_config: Volitelný slovník pro přepsání výchozích klávesových vazeb
        """
        self._navigator = navigator
        self._key_bindings = self._create_key_bindings(key_config or {})

    def _create_key_bindings(
        self,
        custom_bindings: dict[str, Callable[[KeyPressEvent], None]]
    ) -> KeyBindings:
        """
        Vytvoří klávesové vazby s možností přepsání výchozích nastavení.

        Args:
            custom_bindings: Vlastní mapování klávesových zkratek

        Returns:
            Nakonfigurované klávesové vazby
        """
        key_bindings = KeyBindings()

        # Výchozí vazby
        default_bindings = {
            "up": lambda event: self._navigator.go_up(),
            "down": lambda event: self._navigator.go_down(),
            "enter": lambda event: self._navigator.run_selected_item_id (),
            "c-c": lambda event: self._navigator.exit_menu()
        }

        # Sloučení výchozích a vlastních vazeb
        bindings = {**default_bindings, **custom_bindings}

        # Registrace klávesových zkratek
        for key, handler in bindings.items():
            key_bindings.add(key)(handler)

        return key_bindings

    def __call__(self) -> KeyBindings:
        """
        Umožňuje volat instanci jako callable pro získání klávesových vazeb.

        Returns:
            Nakonfigurované klávesové vazby.
        """
        return self._key_bindings

# Příklad použití
class ExampleMenuNavigator:
    def go_up(self): print("Nahoru")
    def go_down(): print("Dolů")
    def run_selected_item_id (self): print("Vybráno")
    def exit_menu(self): print("Ukončeno")

# Použití s výchozím chováním
default_key_bindings = MenuKeyBindings(ExampleMenuNavigator())

# Použití s vlastní konfigurací klávesových zkratek
custom_key_bindings = MenuKeyBindings(
    ExampleMenuNavigator(),
    key_config={
        "a": lambda event: print("Stisknuto A"),
        "b": lambda event: print("Stisknuto B")
    }
)