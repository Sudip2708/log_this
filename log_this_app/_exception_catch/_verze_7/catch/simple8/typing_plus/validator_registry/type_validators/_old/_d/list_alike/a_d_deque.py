from typing import Deque, Any
from collections import deque

from ._list_alike_base import ListAlikeBase

T = Any

class DequeValidator(ListAlikeBase):
    """
    Validátor pro zápis Deque[T]

    Hint:
        Deque[T] = Oboustranná fronta (double-ended queue)
    """

    VALIDATOR_KEY = "deque"
    ANNOTATION = Deque[T]
    INFO = "Definuje oboustrannou frontu položek"
    GET_ORIGIN = deque
