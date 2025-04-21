from .._base_type_validator import BaseTypeValidator
import uuid


class UUIDValidator(BaseTypeValidator):
    """
    Validátor pro uuid.UUID

    Hint:
        uuid.UUID = Univerzální unikátní identifikátor
    """

    VALIDATOR_KEY = "UUID"
    ANNOTATION = "uuid.UUID"
    INFO = "Definuje univerzální unikátní identifikátor"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, uuid.UUID):
            raise TypeError(f"Hodnota '{value}' není validní uuid.UUID objekt.")
        return True