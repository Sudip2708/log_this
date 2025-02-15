from abc import ABC, abstractmethod

class ShowConfigHandlerMixin(ABC):

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

    # Funkce pro výpis aktuální konfigurace
    def show_config_handler(self):
        self.response = "print_configuration"
        self.exit()
