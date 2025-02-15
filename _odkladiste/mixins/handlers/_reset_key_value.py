from abc import ABC, abstractmethod

class ResetKeyValueMixin(ABC):

    @property
    @abstractmethod
    def selected_key(self):
        pass

    @selected_key.setter
    @abstractmethod
    def selected_key(self, value):
        pass

    @property
    @abstractmethod
    def selected_value(self):
        pass

    @selected_value.setter
    @abstractmethod
    def selected_value(self, value):
        pass

    def reset_key_value(self):
        """Resetuje hodnoty těchto dvou atributů na None"""
        self.selected_key = None
        self.selected_value = None
