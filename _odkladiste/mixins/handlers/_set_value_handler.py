from abc import ABC, abstractmethod


class SetValueHandlerMixin(ABC):

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

    # Funkce pro nasavení nové konfigurace
    def set_value_handler(self):
        self.response = "set_value"
        self.exit()
