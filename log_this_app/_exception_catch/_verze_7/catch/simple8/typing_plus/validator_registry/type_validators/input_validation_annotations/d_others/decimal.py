from .._base_type_validator import BaseTypeValidator
import decimal


class DecimalValidator(BaseTypeValidator):
    """
    Validátor pro decimal.Decimal

    Hint:
        decimal.Decimal = Objekt reprezentující přesné desetinné číslo
    """

    VALIDATOR_KEY = "Decimal"
    ANNOTATION = "decimal.Decimal"
    INFO = "Definuje objekt reprezentující přesné desetinné číslo"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, decimal.Decimal):
            raise TypeError(f"Hodnota '{value}' není validní decimal.Decimal objekt.")
        return True