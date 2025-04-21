from collections import UserString

from .._base_type_validator import BaseTypeValidator


class UserStringValidator(BaseTypeValidator):
    """
    Validátor pro zápis UserString

    Hint:
        UserString = Speciální řetězec určený k dědění a přizpůsobení chování
    """

    VALIDATOR_KEY = "userstring"
    ANNOTATION = UserString
    INFO = "Definuje přizpůsobitelný řetězec založený na UserString"
    ORIGIN = UserString
