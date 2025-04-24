from ..._bases import IsInstanceValidatorBase
import datetime


class TimeValidator(IsInstanceValidatorBase):
    """
    Validátor pro datetime.time

    Hint:
        datetime.time = Objekt reprezentující pouze čas
    """

    VALIDATOR_KEY = "time"
    ANNOTATION = "datetime.time"
    INFO = "Definuje objekt reprezentující pouze čas"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, datetime.time):
            raise TypeError(f"Hodnota '{value}' není validní datetime.time objekt.")
        return True