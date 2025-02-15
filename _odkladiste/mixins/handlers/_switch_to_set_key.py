from abc import ABC, abstractmethod

class SwitchToSetKeyMixin(ABC):

    @abstractmethod
    def switch_menu(self, new_menu_type):
        pass

    @property
    @abstractmethod
    def selected_key(self):
        pass

    @selected_key.setter
    @abstractmethod
    def selected_key(self, value):
        pass


    def switch_to_set_key(self, key=None):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        if key:
            self.selected_key = key
        if self.selected_key:
            self.switch_menu("select_value_menu")
        else:
            print("Není vybrán žádný klíč, zadejte klíč prosím znovu.")
            self.switch_menu("select_key_menu")

