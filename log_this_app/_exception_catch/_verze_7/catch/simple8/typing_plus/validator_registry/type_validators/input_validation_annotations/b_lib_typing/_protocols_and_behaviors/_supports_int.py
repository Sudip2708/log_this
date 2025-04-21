from .._base_type_validator import BaseTypeValidator


class SupportsIntValidator(BaseTypeValidator):
    """
    Validátor pro SupportsInt

    Hint:
        SupportsInt = Objekt, který implementuje metodu __int__()
    """

    VALIDATOR_KEY = "SupportsInt"
    ANNOTATION = "SupportsInt"
    INFO = "Definuje, že objekt musí podporovat metodu __int__"
    ORIGIN = None  # Kontroluje se pomocí hasattr

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__int__"):
            raise TypeError(f"Hodnota '{value}' neimplementuje __int__().")
        return True
