class PrintResponse:
    response = None

    @classmethod
    def print_configuration(cls):
        print("Aktuální konfigurace:")
        print("key1: value1")
        print("key2: value2")

    @classmethod
    def set_value(cls):
        key = input("\nZadejte klíč: ")
        value = input("Zadejte hodnotu: ")
        print(f"\nNastaveno: {key} = {value}")

    @classmethod
    def print_response(cls):
        if cls.response == "print_configuration":
            cls.print_configuration()
        elif cls.response == "set_value":
            cls.set_value()
        print()
