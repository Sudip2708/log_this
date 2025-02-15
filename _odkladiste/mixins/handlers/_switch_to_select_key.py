from abc import ABC, abstractmethod

class SwitchToMSelectKeyMixin(ABC):

    @abstractmethod
    def reset_key_value(self):
        pass

    @abstractmethod
    def switch_menu(self, new_menu_type):
        pass

    def switch_to_select_key(self):
        """Přepne do submenu pro výběr klíče."""
        self.reset_key_value()
        self.switch_menu("select_key_menu")

