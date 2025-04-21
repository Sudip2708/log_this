from .._base_type_validator import BaseTypeValidator


class ByteArrayValidator(BaseTypeValidator):
    """
    Validátor pro zápis bytearray

    Hint:
        bytearray = Měnitelná sekvence bajtů
        Neumožňuje zadat vnitřní hodnoty, validuje se pouze typ.
    """

    VALIDATOR_KEY = "bytearray"
    ANNOTATION = bytearray
    INFO = "Definuje, že hodnota může být pouze měnitelná sekvence bajtů"
    GET_ORIGIN = bytearray
