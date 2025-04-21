from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.named_commands import KeyPressEvent

class MenuKeyBindings:
    """Flexibilní správa klávesových vazeb pro menu."""

    def __init__(self, menus_manager: "MenusManager"):
        """
        Inicializace klávesových vazeb s vazbou na menu manager.

        Args:
            menus_manager: Instance správce menu pro ovládání navigace.
        """
        self._menus_manager = menus_manager
        self._key_bindings = self._create_key_bindings()

    def _create_key_bindings(self) -> KeyBindings:
        """
        Vytvoří a nakonfiguruje klávesové vazby.

        Returns:
            Nakonfigurované klávesové vazby.
        """
        key_bindings = KeyBindings()

        @key_bindings.add("up")
        def handle_up(event: KeyPressEvent) -> None:
            """Přesune výběr v menu nahoru."""
            self._menus_manager.go_up()

        @key_bindings.add("down")
        def handle_down(event: KeyPressEvent) -> None:
            """Přesune výběr v menu dolů."""
            self._menus_manager.go_down()

        @key_bindings.add("enter")
        def handle_enter(event: KeyPressEvent) -> None:
            """Potvrdí aktuálně vybranou možnost v menu."""
            self._menus_manager.run_selected_item_id ()

        @key_bindings.add("c-c")
        def handle_ctrl_c(event: KeyPressEvent) -> None:
            """Ukončí menu při stisknutí Ctrl+C."""
            self._menus_manager.exit_menu()

        return key_bindings

    def __call__(self) -> KeyBindings:
        """
        Umožňuje volat instanci jako callable pro získání klávesových vazeb.

        Returns:
            Nakonfigurované klávesové vazby.
        """
        return self._key_bindings