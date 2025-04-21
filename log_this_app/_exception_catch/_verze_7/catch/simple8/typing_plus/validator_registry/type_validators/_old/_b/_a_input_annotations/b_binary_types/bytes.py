from .._base_type_validator import BaseTypeValidator


class BytesValidator(BaseTypeValidator):
    """
    Validátor pro zápis bytes

    Hint:
        bytes = Sekvence bajtů
        Neumožňuje zadat vnitřní hodnoty, validuje se pouze typ.
    """

    VALIDATOR_KEY = "bytes"
    ANNOTATION = bytes
    INFO = "Definuje, že hodnota může být pouze sekvence bajtů"
    GET_ORIGIN = bytes
