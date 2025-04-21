from .._base_type_validator import BaseTypeValidator


class NoneValidator(BaseTypeValidator):
    """
    Validátor pro zápis `None`.

    Používá se tam, kde se očekává, že hodnota bude přesně `None`.

    Hint:
        None = Hodnota musí být výslovně None

    Příklad použití:
        def reset() -> None:
    """

    VALIDATOR_KEY = "none"
    ANNOTATION = None  # Typ None v Pythonu (typ(None))
    INFO = "Definuje typ, jehož jedinou platnou hodnotou je `None`."
    GET_ORIGIN = None
