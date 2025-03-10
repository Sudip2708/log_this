from abc import ABC, abstractmethod

from utils.print_configuration import print_configuration
from utils.set_value import set_value
from utils.run_config_settings import run_config_settings


class GetResponse(ABC):

    @property
    @abstractmethod
    def response(self):
        pass


    def get_response(self):

        # Pokud je požadavek na vytištění konfigurace
        if self.response == "print_configuration":
            print_configuration()

        # Pokud je požadavek na změnu konfigurace
        elif self.response == "set_value":
            run_config_settings()

        # Prázdná mezera
        print()




