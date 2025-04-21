from .._base_type_validator import BaseTypeValidator
import re


class MatchValidator(BaseTypeValidator):
    """
    Validátor pro re.Match

    Hint:
        re.Match = Výsledek shody regulárního výrazu
    """

    VALIDATOR_KEY = "Match"
    ANNOTATION = "re.Match"
    INFO = "Definuje výsledek shody regulárního výrazu"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, re.Match):
            raise TypeError(f"Hodnota '{value}' není validní re.Match objekt.")
        return True