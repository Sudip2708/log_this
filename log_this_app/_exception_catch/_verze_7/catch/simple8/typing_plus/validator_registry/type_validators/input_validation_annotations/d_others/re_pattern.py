from .._base_type_validator import BaseTypeValidator
import re


class PatternValidator(BaseTypeValidator):
    """
    Validátor pro re.Pattern

    Hint:
        re.Pattern = Kompilovaný regulární výraz
    """

    VALIDATOR_KEY = "Pattern"
    ANNOTATION = "re.Pattern"
    INFO = "Definuje kompilovaný regulární výraz"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, re.Pattern):
            raise TypeError(
                f"Hodnota '{value}' není validní re.Pattern objekt.")

        # Pokud má anotace specifikované vlastnosti jako flagy
        if hasattr(annotation, "flags") and annotation.flags is not None:
            if value.flags != annotation.flags:
                raise TypeError(
                    f"Pattern má nesprávné flagy. Očekáváno: {annotation.flags}, získáno: {value.flags}")

        return True