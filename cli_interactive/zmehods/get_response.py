from abc import ABC


from abc_helper import abc_property, abc_method
from utils.print_configuration import print_configuration
from utils.set_value import set_value


class GetResponse(ABC):

    @property
    @abstractmethod
    def response(self):
        pass

    @property
    @response.setter
    def response(self, value):
        pass

    @property
    @abstractmethod
    def selected_key(self):
        pass

    @property
    @abstractmethod
    def selected_value(self):
        pass

    @property
    @selected_value.setter
    def selected_value(self, value):
        pass

    @abstractmethod
    def reset_key_value(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def switch_menu(self, new_menu_type):
        pass

    @abstractmethod
    def clear_response(self):
        pass


    def get_response(self):

        # Pokud je požadavek na vytištění konfigurace
        if self.response == "print_configuration":
            print_configuration()
            self.clear_response()
            print()  # Prázdná mezera

        # Pokud je požadavek na změnu konfigurace
        elif self.response == "set_value":
            set_value()
            print()  # Prázdná mezera

        # Pokud je požadavek na změnu konfigurace
        elif self.response == "print_new":
            print(f"Vybrán klíč: {self.selected_key}, hodnota: {self.selected_value}")
            self.reset_key_value()
            self.clear_response()
            print()  # Prázdná mezera

        # Pokud je požadavek na změnu konfigurace
        elif self.response == "input_custom_value":
            print(f"Ruční zadání hodnoty pro klíč '{self.selected_key}'")
            print("Povolené hodnoty: celé číslo v rozmezí 0 - 100")
            print("(Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter.)\n")
            while True:
                selected_value = input("Zadejte hodnotu: ")
                if not selected_value:
                    break
                try:
                    if 0 <= int(selected_value) <= 100:
                        break
                except ValueError:
                    print("Nesprávně zadaná hodnota. Zkuste to ještě jednou.")
                    print()  # Prázdná mezera

            if selected_value:
                print()  # Prázdná mezera
                self.selected_value = selected_value
                self.response = "print_new"

            else:
                print("(Nebyla zadaná žádná hodnota. Návrat do menu pro výběr hodnoty.)")
                print()  # Prázdná mezera
                self.switch_menu("select_value_menu")
                self.run()









