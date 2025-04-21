from typing import Callable, Protocol
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.named_commands import KeyPressEvent


class KeyBindingsManager:
    """Flexibilní správa klávesových vazeb s dependency injection."""

    def __init__(self, menus_manager):
        """
        Inicializace klávesových vazeb s možností vlastní konfigurace.

        Args:
            navigator: Objekt implementující navigační metody menu
            key_config: Volitelný slovník pro přepsání výchozích klávesových vazeb
        """
        self._menus_manager = menus_manager
        self._key_bindings = self._create_key_bindings()

    def _create_key_bindings(self) -> KeyBindings:
        """
        Vytvoří klávesové vazby s možností přepsání výchozích nastavení.

        Args:
            custom_bindings: Vlastní mapování klávesových zkratek

        Returns:
            Nakonfigurované klávesové vazby
        """

        # Načtení instance KeyBindings
        key_bindings = KeyBindings()

        # Výchozí vazby
        bindings_set = {
            "up": lambda event: self._menus_manager.go_up(),
            "down": lambda event: self._menus_manager.go_down(),
            "enter": lambda event: self._menus_manager.run_selected_item_id (),
            "c-c": lambda event: self._menus_manager.exit_menu()
        }

        # Registrace klávesových zkratek
        for key, handler in bindings_set.items():
            key_bindings.add(key)(handler)

        return key_bindings

    def __call__(self) -> KeyBindings:
        """
        Umožňuje volat instanci jako callable pro získání klávesových vazeb.

        Returns:
            Nakonfigurované klávesové vazby.
        """
        return self._key_bindings

