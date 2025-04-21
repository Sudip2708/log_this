from .._base_type_validator import BaseTypeValidator


class ComplexValidator(BaseTypeValidator):
    """
    Validátor pro zápis complex

    Hint:
        complex = Komplexní číslo
        Neumožňuje zadat vnitřní hodnoty, validuje se pouze typ.
    """

    VALIDATOR_KEY = "complex"
    ANNOTATION = complex
    INFO = "Definuje, že hodnota může být pouze komplexní číslo"
    GET_ORIGIN = complex


