from prompt_toolkit.key_binding import KeyBindings


class MenuKeyBindings:
    """Třída pro správu klávesových zkratek"""

    def __init__(self, menu_controller):
        self.controller = menu_controller
        self.kb = KeyBindings()
        self.setup_key_bindings()

    def setup_key_bindings(self):
        @self.kb.add('up')
        def handle_up(event):
            self.controller.move_selection(-1)

        @self.kb.add('down')
        def handle_down(event):
            self.controller.move_selection(1)

        @self.kb.add('enter')
        def handle_enter(event):
            self.controller.select_current_item()

        @self.kb.add('c-c')
        def handle_ctrl_c(event):
            self.controller.exit()

    def get_bindings(self):
        return self.kb