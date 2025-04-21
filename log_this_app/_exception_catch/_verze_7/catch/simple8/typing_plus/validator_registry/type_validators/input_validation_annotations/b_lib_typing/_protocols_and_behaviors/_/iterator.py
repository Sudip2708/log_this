from .._base_type_validator import BaseTypeValidator


class IteratorValidator(BaseTypeValidator):
    """
    Validátor pro Iterator[T]

    Hint:
        Iterator = Objekt, který implementuje metody __iter__ a __next__
    """

    VALIDATOR_KEY = "Iterator"
    ANNOTATION = "Iterator"
    INFO = "Definuje, že objekt musí implementovat __iter__ a __next__"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not (hasattr(value, "__iter__") and hasattr(value, "__next__")):
            raise TypeError(f"Hodnota '{value}' není validní iterátor.")
        return True