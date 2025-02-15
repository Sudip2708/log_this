from abc import ABC, abstractmethod

class ExitHandlerMixin(ABC):

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

    # Funkce pro ukončení interaktivního režimu
    def exit_handler(self):
        self.response = "exit"
        self.exit()
