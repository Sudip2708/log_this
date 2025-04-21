from .._base_type_validator import BaseTypeValidator


class IterableValidator(BaseTypeValidator):
    """
    Validátor pro Iterable[T]

    Hint:
        Iterable = Objekt použitelný ve for cyklu (__iter__)
    """

    VALIDATOR_KEY = "Iterable"
    ANNOTATION = "Iterable"
    INFO = "Definuje, že objekt musí implementovat __iter__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__iter__"):
            raise TypeError(f"Hodnota '{value}' není iterovatelná.")
        return True