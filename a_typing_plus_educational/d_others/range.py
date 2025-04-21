from .._base_type_validator import BaseTypeValidator


class RangeValidator(BaseTypeValidator):
    """
    Validátor pro range

    Hint:
        range = Sekvence čísel vytvořená pomocí funkce range()
    """

    VALIDATOR_KEY = "range"
    ANNOTATION = "range"
    INFO = "Definuje objekt typu range"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, range):
            raise TypeError(f"Hodnota '{value}' není validní range objekt.")
        return True