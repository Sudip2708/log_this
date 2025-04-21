from .._base_type_validator import BaseTypeValidator


class FloatValidator(BaseTypeValidator):
    """
    Validátor pro zápis float

    Hint:
        float = Číslo s plovoucí desetinnou čárkou
        Neumožňuje zadat vnitřní hodnoty, validuje se pouze typ.
    """

    VALIDATOR_KEY = "float"
    ANNOTATION = float
    INFO = "Definuje, že hodnota může být pouze číslo s plovoucí desetinnou čárkou"
    GET_ORIGIN = float
