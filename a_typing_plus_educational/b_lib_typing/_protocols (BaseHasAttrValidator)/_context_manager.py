from .._base_type_validator import BaseTypeValidator


class ContextManagerValidator(BaseTypeValidator):
    """
    Validátor pro ContextManager

    Hint:
        ContextManager = Objekt použitelný s with blokem (__enter__ a __exit__)
    """

    VALIDATOR_KEY = "ContextManager"
    ANNOTATION = "ContextManager"
    INFO = "Definuje, že objekt musí implementovat __enter__ a __exit__"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not (hasattr(value, "__enter__") and hasattr(value, "__exit__")):
            raise TypeError(f"Hodnota '{value}' není validní kontextový manažer.")
        return True
