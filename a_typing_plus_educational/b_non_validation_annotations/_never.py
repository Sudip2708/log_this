try:
    from typing import Never
except ImportError:
    Never = type("NeverUnavailable", (), {})  # fallback pro starší Python

from .._base_type_validator import TypeValidator


class NeverValidator(TypeValidator):
    """
    Validátor pro zápis Never (od Pythonu 3.11)

    Používá se pro situace, které by za běhu neměly nastat.

    Hint:
        Never = Hodnota by nikdy neměla být vytvořena

    Příklad použití:
        def never_called() -> Never:
    """

    VALIDATOR_KEY = "never"
    ANNOTATION = Never
    INFO = "Definuje typ, který by nikdy neměl být instancován."
    GET_ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Jakákoliv hodnota je neplatná (i None)
        return self.validate_typing(False, bool_only=bool_only)
