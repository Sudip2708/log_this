from abc import ABC, abstractmethod

class ShowHelpHandlerMixin(ABC):

    @property
    @abstractmethod
    def show_help(self):
        pass

    @show_help.setter
    @abstractmethod
    def show_help(self, value):
        pass

    # Funkce pro zobrazení a skyrytí menu
    def show_help_handler(self):
        self.show_help = not self.show_help
