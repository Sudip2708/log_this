from prompt_toolkit.key_binding import KeyBindings
import logging

# Nastavení logování s podrobnostmi
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class KeyBindingsManager:
    """Správa klávesových zkratek a navigace v menu."""

    def __init__(self, menus_manager):
        """
        Inicializace klávesových vazeb.

        Args:
            menus_manager: Hlavní instance správy menu.
        """
        self.mm = menus_manager
        self._key_bindings = self._create_key_bindings()

    def __call__(self) -> KeyBindings:
        """Umožňuje volat instanci jako callable pro získání klávesových vazeb."""
        return self._key_bindings

    def _create_key_bindings(self) -> KeyBindings:
        """Vytvoří klávesové vazby."""
        key_bindings = KeyBindings()

        bindings_set = {
            "up": lambda event: self._go_up(),
            "down": lambda event: self._go_down(),
            "enter": lambda event: self._run_selected(),
            "c-c": lambda event: self._exit_menu()
        }

        for key, handler in bindings_set.items():
            key_bindings.add(key)(handler)

        return key_bindings

    def _go_up(self):
        """Posune výběr nahoru."""
        try:
            self.mm.selected_item_id = max(0, self.mm.selected_item_id - 1)
            self.mm.menu_renderer.refresh()
        except Exception as e:
            logging.error(f"Chyba v _go_up: {e}", exc_info=True)

    @try_except_base_exeption_catch
    def _go_up(self):
        """Posune výběr nahoru."""
        self.mm.selected_item_id = max(0, self.mm.selected_item_id - 1)
        self.mm.menu_renderer.refresh()


    def _go_down(self):
        """Posune výběr dolů."""
        try:
            self.mm.selected_item_id = min(
                len(self.mm.current_menu.menu_items) - 1,
                self.mm.selected_item_id + 1
            )
            self.mm.menu_renderer.refresh()
        except Exception as e:
            logging.error(f"Chyba v _go_down: {e}", exc_info=True)

    def _run_selected(self):
        """Spustí metodu navázanou na vybraný úkon."""
        try:
            selected_action = \
            self.mm.current_menu.menu_items[self.mm.selected_item_id][1]
            selected_action()
        except Exception as e:
            logging.error(f"Chyba v _run_selected: {e}", exc_info=True)

    def _exit_menu(self):
        """Ukončí interaktivní režim"""
        try:
            self.mm.menu_renderer.exit()
        except Exception as e:
            logging.error(f"Chyba v _exit_menu: {e}", exc_info=True)


