from typing import Set, Any

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class SetValidator(BaseIterableValidator):
    """
    Validátor pro zápis Set[T]

    Hint:
        Set[T] = Množina prvků typu T
    """

    VALIDATOR_KEY = "set"
    ANNOTATION = Set[T]
    INFO = "Definuje množinu prvků"
    GET_ORIGIN = set