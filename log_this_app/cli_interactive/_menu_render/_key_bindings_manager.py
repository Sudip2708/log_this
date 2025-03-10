# print("_menu_render/_key_bindings_manager.py")
from prompt_toolkit.key_binding import KeyBindings


class KeyBindingsManager:
    """Třída pro správu klávesových příkazů"""

    def __init__(self, menus_manager):
        """Inicializace instance pro mapování kláves"""
        self.menus_manager = menus_manager
        self.kb = KeyBindings()
        self.setup_key_bindings()

    def setup_key_bindings(self):
        """Nastavení klávesových příkazů"""

        @self.kb.add('up')
        def handle_up(event):
            self.menus_manager.go_up()

        @self.kb.add('down')
        def handle_down(event):
            self.menus_manager.go_down()

        @self.kb.add('enter')
        def handle_enter(event):
            self.menus_manager.run_current_selection()

        @self.kb.add('c-c')
        def handle_ctrl_c(event):
            self.menus_manager.exit_menu()

    def __call__(self):
        return self.kb