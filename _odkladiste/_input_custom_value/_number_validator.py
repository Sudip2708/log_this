# print("_response_manager/_input_int_value/_number_validator.py")
from prompt_toolkit.validation import Validator, ValidationError


class NumberValidator(Validator):
    """Validátor pro zadávání čísel od 0 do 1000"""
    def validate(self, document):
        try:
            value = int(document.text)
            if not (0 <= value <= 1000):
                raise ValidationError(message="Zadejte číslo mezi 0 a 1000.")
        except ValueError:
            raise ValidationError(message="Zadejte platné celé číslo.")