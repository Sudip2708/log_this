from typing import NewType

from .._base_type_validator import TypeValidator


class NewTypeValidator(TypeValidator):
    """
    Validátor pro zápis UserId = NewType("UserId", int)

    Jedná se o nástroj k vytváření vlastních složených anotací.

    Hint:
        UserId = NewType("UserId", int) = Alias na jiný typ
    """

    # Definice klíče pro registr
    # Neodpovídá get_origin, protože ta vrací None!
    VALIDATOR_TYPE = NewType

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Najde původní typ
        original_type = annotation.__supertype__

        # Validace na originální typ
        return self.validate_typing(value, original_type, depth_check, custom_types, bool_only)
