from .._base_type_validator import BaseTypeValidator


class ReversibleValidator(BaseTypeValidator):
    """
    Validátor pro Reversible[T]

    Hint:
        Reversible = Objekt, který implementuje metodu __reversed__
    """

    VALIDATOR_KEY = "Reversible"
    ANNOTATION = "Reversible"
    INFO = "Definuje, že objekt musí implementovat metodu __reversed__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__reversed__"):
            raise TypeError(f"Hodnota '{value}' neimplementuje __reversed__().")
        return True