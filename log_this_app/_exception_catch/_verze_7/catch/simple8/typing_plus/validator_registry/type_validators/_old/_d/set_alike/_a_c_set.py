from typing import Set, Any

from ._a_set_alike_base import SetAlikeBase

T = Any

class SetValidator(SetAlikeBase):
    """
    Validátor pro zápis Set[T]

    Hint:
        Set[T] = Množina prvků typu T
    """

    VALIDATOR_KEY = "set"
    ANNOTATION = Set[T]
    INFO = "Definuje množinu prvků"
    GET_ORIGIN = set


