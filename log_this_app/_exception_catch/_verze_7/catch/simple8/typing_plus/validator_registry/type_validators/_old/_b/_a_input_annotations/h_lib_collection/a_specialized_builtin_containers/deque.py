from typing import Deque
from collections import deque

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class DequeValidator(BaseIterableValidator):
    """
    Validátor pro zápis Deque[T]

    Hint:
        Deque[T] = Oboustranná fronta (double-ended queue)
    """

    VALIDATOR_KEY = "deque"
    ANNOTATION = Deque[T]
    INFO = "Definuje oboustrannou frontu položek"
    GET_ORIGIN = deque
