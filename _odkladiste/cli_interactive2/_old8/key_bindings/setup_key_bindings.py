from abc import ABC

from abc_helper import abc_property, abc_method


class SetupKeyBindingsMixin(ABC):

    # Atribut obsahující instanci KeyBindings
    kb = abc_property("kb")

    # Atribut pro zaznamenání vybrané položky
    current_selection = abc_property("current_selection")

    # Atribut pro zaznamenání položek zobrazeného menu
    menu_items = abc_property("menu_items")

    # Metoda znovu načte data pro vykreselní menu
    reload_menu = abc_method("reload_menu")

    # Metoda uzavře aktuální interaktivní menu
    exit_menu = abc_method("exit")



    def setup_key_bindings(self):
        """Nastavení klávesových příkazů pro používání interaktivního menu"""

        # Mapování šipky nahoru
        @self.kb.add('up')
        def handle_up(event):
            self.go_up()

        # Mapování šipky dolu
        @self.kb.add('down')
        def handle_down(event):
            self.go_down()

        # Mapování klávesy enter
        @self.kb.add('enter')
        def handle_enter(event):
            self.run_current_selection()

        # Mapování Ctrl+C
        @self.kb.add('c-c')
        def handle_ctrl_c(event):
            self.exit_menu()


    def go_up(self):
        """Odpočet 1 od hodnoty 'current_selection' se spodním limitem 0"""
        self.current_selection = max(
            0,
            self.current_selection - 1
        )
        self.reload_menu()


    def go_down(self):
        """Odpočet 1 od hodnoty 'current_selection' se spodním limitem 0"""
        self.current_selection = min(
            len(self.menu_items) - 1,
            self.current_selection + 1
        )
        self.reload_menu()


    def run_current_selection(self):
        """Spustí metodu navázanou na vyraný úkon"""
        self.menu_items[self.current_selection][1]()
