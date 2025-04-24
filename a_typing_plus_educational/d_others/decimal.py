from ..._bases import IsInstanceValidatorBase
import decimal


class DecimalValidator(IsInstanceValidatorBase):
    """
    Validátor pro decimal.Decimal

    Hint:
        decimal.Decimal = Objekt reprezentující přesné desetinné číslo
    """

    VALIDATOR_KEY = "Decimal"
    ANNOTATION = "decimal.Decimal"
    INFO = "Definuje objekt reprezentující přesné desetinné číslo"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, decimal.Decimal):
            raise TypeError(f"Hodnota '{value}' není validní decimal.Decimal objekt.")
        return True