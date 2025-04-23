from typing import MutableSet
from collections.abc import MutableSet as MutableSetOrigin

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class MutableSetValidator(BaseIterableValidator):
    """
    Validátor pro zápis MutableSet[T]

    Hint:
        MutableSet[T] = Měnitelná množina prvků typu T
    """

    VALIDATOR_KEY = "mutableset"
    ANNOTATION = MutableSet[T]
    INFO = "Definuje měnitelnou množinu prvků"
    ORIGIN = MutableSetOrigin
