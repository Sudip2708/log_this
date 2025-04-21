from .._base_type_validator import BaseTypeValidator


class HashableValidator(BaseTypeValidator):
    """
    Validátor pro Hashable

    Hint:
        Hashable = Objekt, který implementuje metodu __hash__()
    """

    VALIDATOR_KEY = "Hashable"
    ANNOTATION = "Hashable"
    INFO = "Definuje, že objekt musí implementovat metodu __hash__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__hash__") or value.__hash__ is None:
            raise TypeError(f"Hodnota '{value}' není hashable.")
        return True