from .._base_type_validator import BaseTypeValidator


class AsyncIterableValidator(BaseTypeValidator):
    """
    Validátor pro AsyncIterable

    Hint:
        AsyncIterable = Objekt použitelný v async for (__aiter__)
    """

    VALIDATOR_KEY = "AsyncIterable"
    ANNOTATION = "AsyncIterable"
    INFO = "Definuje, že objekt musí implementovat __aiter__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__aiter__"):
            raise TypeError(f"Hodnota '{value}' není asynchronně iterovatelná.")
        return True
