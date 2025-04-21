from .._base_type_validator import BaseTypeValidator


class IntValidator(BaseTypeValidator):
    """
    Validátor pro zápis int

    Hint:
        int = Celé číslo
        Neumožňuje zadat vnitřní hodnoty, validuje se pouze typ.
    """

    VALIDATOR_KEY = "int"
    ANNOTATION = int
    INFO = "Definuje, že hodnota může být pouze celé číslo"
    GET_ORIGIN = int
