# print("_response_manager/_input_int_value/input_int_value.py")
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.validation import Validator, ValidationError


# class NumberValidator(Validator):
#     """Validátor pro zadávání čísel od 0 do 1000"""
#     def validate(self, document):
#         try:
#             value = int(document.text)
#             if not (0 <= value <= 1000):
#                 raise ValidationError(message="Zadejte číslo mezi 0 a 1000.")
#         except ValueError:
#             raise ValidationError(message="Zadejte platné celé číslo.")

class NumberValidator(Validator):
    """Validátor pro zadávání čísel od 0 do 1000"""
    def validate(self, document):
        if document.text:
            value = int(document.text)
            if not (0 <= value <= 1000):
                raise ValidationError(message="Zadejte číslo mezi 0 a 1000.")



def input_int_value(menus_manager):
    """Metoda umožňující ruční zadání int hodnoty (0 - 1000)"""

    # Načtení metody pro výpis do konzole pro jednodušší zápis
    cli_print = menus_manager.styler.cli_print

    try:

        # Intro text
        cli_print.info.title(f"Ruční zadání hodnoty pro klíč '{menus_manager.selected_key}'")
        cli_print.info.text("Povolené hodnoty: celé číslo v rozmezí 0 - 1000")
        cli_print.info.text("Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter.")

        # Výzva k zadání hodnoty
        style, formatted_text = menus_manager.styler.get_style.prompt.input(
            "Zadejte hodnotu: "
        )

        # Validace a zapsání hodnoty
        selected_value = prompt(
            formatted_text,
            validator=NumberValidator(),
            validate_while_typing=True,
            style=Style.from_dict({"": style})
        )

        # Prázdný řádek pro oddělení výstupu
        print()

        # Pokud nebyla zadána žádná hodnota, vrací se None
        if selected_value == "":
            cli_print.warning.title("Nebyla zadaná žádná hodnota.")
            cli_print.warning.direction("Návrat do menu pro výběr hodnoty.")
            menus_manager.continue_with_menu = "select_value_menu"
            return None

        return selected_value  # Vrací zadanou hodnotu

    except KeyboardInterrupt:
        cli_print.error.title("Zadávání přerušeno uživatelem...")
        return None
