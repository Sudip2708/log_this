from .._base_type_validator import BaseTypeValidator
import datetime


class DatetimeValidator(BaseTypeValidator):
    """
    Validátor pro datetime.datetime

    Hint:
        datetime.datetime = Objekt reprezentující datum a čas
    """

    VALIDATOR_KEY = "datetime"
    ANNOTATION = "datetime.datetime"
    INFO = "Definuje objekt reprezentující datum a čas"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, datetime.datetime):
            raise TypeError(f"Hodnota '{value}' není validní datetime.datetime objekt.")
        return True