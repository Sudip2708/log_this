from typing import FrozenSet, Any

from ._set_alike_base import SetAlikeBase

T = Any


class FrozenSetValidator(SetAlikeBase):
    """
    Validátor pro zápis FrozenSet[T]

    Hint:
        FrozenSet[T] = Neměnná množina prvků typu T
    """

    VALIDATOR_KEY = "frozenset"
    ANNOTATION = FrozenSet[T]
    INFO = "Definuje neměnnou množinu prvků"
    GET_ORIGIN = frozenset

