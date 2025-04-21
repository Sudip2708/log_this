from typing import NoneType

from .._base_type_validator import TypeValidator


class NoneValidator(TypeValidator):
    """
    Validátor pro zápis `None`.

    Používá se tam, kde se očekává, že hodnota bude přesně `None`.

    Hint:
        None = Hodnota musí být výslovně None

    Příklad použití:
        def reset() -> None:
    """

    VALIDATOR_KEY = "none"
    ANNOTATION = NoneType  # Typ None v Pythonu (typ(None))
    INFO = "Definuje typ, jehož jedinou platnou hodnotou je `None`."
    GET_ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Kontrola zda je hodnota None
        return self.validate_typing(value is None, bool_only=bool_only)
