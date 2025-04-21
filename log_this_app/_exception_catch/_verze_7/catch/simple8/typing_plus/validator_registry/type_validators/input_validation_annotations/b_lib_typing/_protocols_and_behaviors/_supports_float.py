from .._base_type_validator import BaseTypeValidator


class SupportsFloatValidator(BaseTypeValidator):
    """
    Validátor pro SupportsFloat

    Hint:
        SupportsFloat = Objekt, který implementuje metodu __float__()
    """

    VALIDATOR_KEY = "SupportsFloat"
    ANNOTATION = "SupportsFloat"
    INFO = "Definuje, že objekt musí podporovat metodu __float__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__float__"):
            raise TypeError(f"Hodnota '{value}' neimplementuje __float__().")
        return True
