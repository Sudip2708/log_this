from typing import Literal, get_args

from .._base_type_validator import BaseTypeValidator


class LiteralValidator(BaseTypeValidator):
    """
    Validátor pro zápis Literal["a", "b", "c"]

    Hint:
        Literal["a", "b", "c"] = Předdefinovaná množina hodnot
    """

    VALIDATOR_KEY = "literal"
    ANNOTATION = Literal["a", "b", "c"]
    INFO = "Definuje povolené hodnoty"
    GET_ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Získání tuple s vnitřními typy
        inner_args = get_args(annotation)

        # Validace hodnoty vůči vnitřnímu typu
        return self.validate_condition(value in inner_args)