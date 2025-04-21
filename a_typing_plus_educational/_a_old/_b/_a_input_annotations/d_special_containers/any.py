from typing import Any

from .._base_type_validator import BaseTypeValidator


class AnyValidator(BaseTypeValidator):
    """
    Validátor pro zápis Any

    Hint:
        Any = Libovolný typ
    """

    VALIDATOR_KEY = "any"
    ANNOTATION = Any
    INFO = "Definuje, že jakákoliv položka je platná"
    GET_ORIGIN = Any


    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Any podporuje všechny hodnoty, takže je vždy True
        return True
