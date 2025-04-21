from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from typing import TYPE_CHECKING

# Importy pro typovou kontrolu:
if TYPE_CHECKING:
    from ..menus_manager import MenusManager


class KeyBindingsManager:
    """ Třída pro správu klávesových příkazů."""

    def __init__(self, menus_manager: "MenusManager") -> None:
        """
        Inicializace instance pro mapování kláves.

        Args:
            menus_manager (object): Správce menu, který ovládá interakci uživatele.

        Atributy:
            menus_manager (object): Správce menu obsahující logiku přepínání položek.
            kb (KeyBindings): Objekt pro mapování klávesových zkratek.
        """
        self.menus_manager = menus_manager
        self.kb = KeyBindings()
        self.setup_key_bindings()

    def setup_key_bindings(self) -> None:
        """Nastavení klávesových příkazů pro navigaci a ovládání menu."""

        @self.kb.add("up")
        def handle_up(event: KeyPressEvent) -> None:
            """Přesune výběr v menu nahoru."""
            self.menus_manager.go_up()

        @self.kb.add("down")
        def handle_down(event: KeyPressEvent) -> None:
            """Přesune výběr v menu dolů."""
            self.menus_manager.go_down()

        @self.kb.add("enter")
        def handle_enter(event: KeyPressEvent) -> None:
            """Potvrdí aktuálně vybranou možnost v menu."""
            self.menus_manager.run_selected_item_id ()

        @self.kb.add("c-c")
        def handle_ctrl_c(event: KeyPressEvent) -> None:
            """Ukončí menu při stisknutí Ctrl+C."""
            self.menus_manager.exit_menu()

    def __call__(self) -> KeyBindings:
        """
        Vrátí objekt s namapovanými klávesovými příkazy.

        Returns:
            KeyBindings: Objekt spravující klávesové zkratky.
        """
        return self.kb
