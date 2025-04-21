from .._base_type_validator import BaseTypeValidator


class MemoryViewValidator(BaseTypeValidator):
    """
    Validátor pro zápis memoryview

    Hint:
        memoryview = Pohled na paměť objektu typu bytes nebo bytearray
        Neumožňuje zadat vnitřní hodnoty, validuje se pouze typ.
    """

    VALIDATOR_KEY = "memoryview"
    ANNOTATION = memoryview
    INFO = "Definuje, že hodnota může být pouze pohled na paměť objektu typu bytes nebo bytearray"
    GET_ORIGIN = memoryview
