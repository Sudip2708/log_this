from typing import MutableSet, Any
from collections.abc import MutableSet as MutableSetOrigin

from ._set_alike_base import SetAlikeBase

T = Any


class MutableSetValidator(SetAlikeBase):
    """
    Validátor pro zápis MutableSet[T]

    Hint:
        MutableSet[T] = Měnitelná množina prvků typu T
    """

    VALIDATOR_KEY = "mutableset"
    ANNOTATION = MutableSet[T]
    INFO = "Definuje měnitelnou množinu prvků"
    GET_ORIGIN = MutableSetOrigin
