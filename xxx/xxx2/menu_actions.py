from response_handler import PrintResponse

class MenuActions:
    def show_help(self):
        pass  # Implementace zobrazování nápovědy

    def show_config(self):
        PrintResponse.response = "print_configuration"

    def set_value(self):
        PrintResponse.response = "set_value"

    def exit_program(self):
        PrintResponse.response = None