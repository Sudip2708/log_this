from prompt_toolkit.validation import Validator, ValidationError


class NumberValidator(Validator):
    """Validátor pro zadávání čísel od 0 do 1000"""
    def validate(self, document):
        if document.text:
            try:
                value = int(document.text)
                if not (0 <= value <= 1000):
                    raise ValidationError(
                        message="Zadané číslo musí být mezi 0 a 1000.")
            except ValueError:
                raise ValidationError(
                    message="Zadaná hodnota musí bý celé číslo.")