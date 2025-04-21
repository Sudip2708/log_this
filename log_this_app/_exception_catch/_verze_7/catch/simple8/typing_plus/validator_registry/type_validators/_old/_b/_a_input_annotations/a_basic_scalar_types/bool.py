from .._base_type_validator import BaseTypeValidator


class BoolValidator(BaseTypeValidator):
    """
    Validátor pro zápis bool

    Hint:
        bool = Boolean hodnota True / False
        Neumožňuje zadat vnitřní hodnoty, validuje se pouze typ.
    """

    VALIDATOR_KEY = "bool"
    ANNOTATION = bool
    INFO = "Definuje, že hodnota může být pouze True / False"
    GET_ORIGIN = bool

