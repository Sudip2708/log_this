from .._base_type_validator import BaseTypeValidator


class ContainerValidator(BaseTypeValidator):
    """
    Validátor pro Container[T]

    Hint:
        Container = Objekt, který implementuje metodu __contains__
    """

    VALIDATOR_KEY = "Container"
    ANNOTATION = "Container"
    INFO = "Definuje, že objekt musí implementovat metodu __contains__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__contains__"):
            raise TypeError(f"Hodnota '{value}' neimplementuje __contains__().")
        return True