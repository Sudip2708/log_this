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
        self.menu_items[self.current_selection][1]()

    @self.kb.add('c-c')
    def handle_ctrl_c(event):
        self.exit_handler()