from .._base_type_validator import BaseTypeValidator


class AsyncIteratorValidator(BaseTypeValidator):
    """
    Validátor pro AsyncIterator[T]

    Hint:
        AsyncIterator = Objekt, který implementuje metody __aiter__ a __anext__
    """

    VALIDATOR_KEY = "AsyncIterator"
    ANNOTATION = "AsyncIterator"
    INFO = "Definuje, že objekt musí implementovat __aiter__ a __anext__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not (hasattr(value, "__aiter__") and hasattr(value, "__anext__")):
            raise TypeError(f"Hodnota '{value}' není validní asynchronní iterátor.")
        return True