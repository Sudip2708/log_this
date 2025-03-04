# print("_response_manager/_input_int_value/input_int_value.py")
from ._input_int_value_methods_mixin import InputIntValueMethodMixin

class InputCustomValue(InputIntValueMethodMixin):

    def __init__(self, menus_manager):
        self.mm = menus_manager

    def input_int_value(self):
        """Metoda umožňující ruční zadání int hodnoty (0 - 1000)"""

        try:

            # Vymazání atibutu pro hodnotu
            self.mm.selected_value = None

            # Intro text
            self.intro_text()

            # Zadání hodnoty
            self.input_dialog()

            # Zpracování výsledku
            self.result_processing()

        except KeyboardInterrupt:
            self.mm.styler.cli_print.error.title("Zadávání přerušeno uživatelem...")
            self.mm.response = "exit"
            self.mm.exit_menu()


