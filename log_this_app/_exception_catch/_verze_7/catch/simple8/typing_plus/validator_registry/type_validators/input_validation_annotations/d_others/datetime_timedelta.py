from .._base_type_validator import BaseTypeValidator
import datetime


class TimedeltaValidator(BaseTypeValidator):
    """
    Validátor pro datetime.timedelta

    Hint:
        datetime.timedelta = Objekt reprezentující časový interval
    """

    VALIDATOR_KEY = "timedelta"
    ANNOTATION = "datetime.timedelta"
    INFO = "Definuje objekt reprezentující časový interval"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, datetime.timedelta):
            raise TypeError(f"Hodnota '{value}' není validní datetime.timedelta objekt.")
        return True