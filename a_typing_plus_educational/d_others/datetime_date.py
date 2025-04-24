from ..._bases import IsInstanceValidatorBase
import datetime


class DateValidator(IsInstanceValidatorBase):
    """
    Validátor pro datetime.date

    Hint:
        datetime.date = Objekt reprezentující pouze datum
    """

    VALIDATOR_KEY = "date"
    ANNOTATION = "datetime.date"
    INFO = "Definuje objekt reprezentující pouze datum"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, datetime.date):
            raise TypeError(f"Hodnota '{value}' není validní datetime.date objekt.")
        return True