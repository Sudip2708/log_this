from abc import ABC, abstractmethod

class SetValueAndPrintMixin(ABC):

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

    @property
    @abstractmethod
    def selected_value(self):
        pass

    @selected_value.setter
    @abstractmethod
    def selected_value(self, value):
        pass


    def set_value_and_print(self, value):
        """Uloží vybranou hodnotu, vypíše výsledek a vrátí se do hlavního menu."""
        self.selected_value = value
        self.response = "print_new"
        self.exit()
