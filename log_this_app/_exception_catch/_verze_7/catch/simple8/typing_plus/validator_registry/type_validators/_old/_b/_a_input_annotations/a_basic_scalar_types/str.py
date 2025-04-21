from .._base_type_validator import BaseTypeValidator


class StrValidator(BaseTypeValidator):
    """
    Validátor pro zápis str

    Hint:
        str = Řetězec
        Neumožňuje zadat vnitřní hodnoty, validuje se pouze typ.
    """

    VALIDATOR_KEY = "str"
    ANNOTATION = str
    INFO = "Definuje, že hodnota může být pouze řetězec"
    GET_ORIGIN = str
