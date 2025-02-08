from prompt_toolkit import prompt
from prompt_toolkit.styles import Style


class PrintResponse:
    response = None

    @classmethod
    def print_configuration(cls):
        print("Aktuální konfigurace:")
        print("key1: value1")
        print("key2: value2")

    @classmethod
    def set_value(cls):


        key = input('Zadejte klíč: ')
        value = input('Zadejte hodnotu: ')

        # value = prompt([
        #     ('class:prompt', 'Zadejte hodnotu: '),
        # ], style=Style.from_dict({
        #             'prompt': 'yellow',
        #         })

        print(f"\nNastaveno: {key} = {value}")

    @classmethod
    def print_response(cls):
        if cls.response == "print_configuration":
            cls.print_configuration()
        elif cls.response == "set_value":
            cls.set_value()
        print()