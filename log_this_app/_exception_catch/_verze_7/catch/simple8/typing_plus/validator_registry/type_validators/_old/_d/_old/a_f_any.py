from typing import get_args, Union, Any

from .._base_type_validator import TypeValidator


class AnyValidator(TypeValidator):
    """
    Validátor pro zápis Any

    Hint:
        Any = Libovolný typ
    """

    VALIDATOR_KEY = "any"
    ANNOTATION = Any
    INFO = "Definuje, že jakákoliv položka je platná"
    GET_ORIGIN = None


    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Any podporuje všechny hodnoty, takže je vždy True
        return True
