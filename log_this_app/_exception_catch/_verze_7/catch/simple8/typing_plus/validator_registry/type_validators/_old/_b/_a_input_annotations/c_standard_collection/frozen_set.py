from typing import FrozenSet, Any

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class FrozenSetValidator(BaseIterableValidator):
    """
    Validátor pro zápis FrozenSet[T]

    Hint:
        FrozenSet[T] = Neměnná množina prvků typu T
    """

    VALIDATOR_KEY = "frozenset"
    ANNOTATION = FrozenSet[T]
    INFO = "Definuje neměnnou množinu prvků"
    GET_ORIGIN = frozenset

