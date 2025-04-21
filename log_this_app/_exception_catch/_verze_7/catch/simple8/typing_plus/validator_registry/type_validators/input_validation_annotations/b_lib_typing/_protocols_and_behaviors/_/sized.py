from .._base_type_validator import BaseTypeValidator


class SizedValidator(BaseTypeValidator):
    """
    Validátor pro Sized

    Hint:
        Sized = Objekt, který implementuje metodu __len__()
    """

    VALIDATOR_KEY = "Sized"
    ANNOTATION = "Sized"
    INFO = "Definuje, že objekt musí implementovat metodu __len__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__len__"):
            raise TypeError(f"Hodnota '{value}' neimplementuje __len__().")
        return True