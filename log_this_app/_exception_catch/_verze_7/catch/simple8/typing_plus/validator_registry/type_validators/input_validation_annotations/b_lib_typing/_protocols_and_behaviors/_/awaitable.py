from .._base_type_validator import BaseTypeValidator


class AwaitableValidator(BaseTypeValidator):
    """
    Validátor pro Awaitable[T]

    Hint:
        Awaitable = Objekt, který implementuje metodu __await__()
    """

    VALIDATOR_KEY = "Awaitable"
    ANNOTATION = "Awaitable"
    INFO = "Definuje, že objekt musí implementovat metodu __await__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__await__"):
            raise TypeError(f"Hodnota '{value}' není awaitable.")
        return True