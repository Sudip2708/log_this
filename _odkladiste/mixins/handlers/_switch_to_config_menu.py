from abc import ABC, abstractmethod

class SwitchToConfigMenuMixin(ABC):

    @abstractmethod
    def switch_menu(self, new_menu_type):
        pass

    def switch_to_config_menu(self):
        """Přepne do submenu pro nastavení konfigurace."""
        self.switch_menu("config_menu")

