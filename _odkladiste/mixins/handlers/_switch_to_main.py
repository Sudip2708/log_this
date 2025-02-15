from abc import ABC, abstractmethod

class SwitchToMainMixin(ABC):

    @abstractmethod
    def switch_menu(self, new_menu_type):
        pass

    def switch_to_main(self):
        """Přepne zpět na hlavní menu."""
        self.switch_menu("main_menu")

