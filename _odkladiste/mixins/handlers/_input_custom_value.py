from abc import ABC, abstractmethod

class InputCustomValueMixin(ABC):

    @abstractmethod
    def exit(self):
        pass

    @property
    @abstractmethod
    def response(self):
        pass

    @response.setter
    @abstractmethod
    def response(self, value):
        pass

    def input_custom_value(self):
        """Zobrazí vstupní dialog pro zadání vlastní hodnoty."""
        self.response = "input_custom_value"
        self.exit()
