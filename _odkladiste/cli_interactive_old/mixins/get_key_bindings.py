from abc import ABC, abstractmethod

class GetKeyBindings(ABC):

    @property
    @abstractmethod
    def menu_items(self):
        pass

    @property
    @abstractmethod
    def current_selection(self):
        pass

    @current_selection.setter
    @abstractmethod
    def current_selection(self, value):
        pass

    @property
    @abstractmethod
    def kb(self):
        pass


    @abstractmethod
    def exit(self):
        pass


    def setup_key_bindings(self):

        # Mapování šipky nahoru
        @self.kb.add('up')
        def handle_up(event):
            # Odpočet 1 od hodnoty current_selection se spodním limitem 0
            self.current_selection = max(0, self.current_selection - 1)
            event.app.invalidate()

        # Mapování šipky dolu
        @self.kb.add('down')
        def handle_down(event):
            # Připočte 1 k hodnotě current_selection se stropem dle počtu položek menu
            self.current_selection = min(len(self.menu_items) - 1, self.current_selection + 1)
            event.app.invalidate()

        # Mapování klávesy enter
        @self.kb.add('enter')
        def handle_enter(event):
            # Spustí metodu navázanou na dané menu
            self.menu_items[self.current_selection][1]()

        # Mapování Ctrl+C
        @self.kb.add('c-c')
        def handle_ctrl_c(event):
            self.exit()
