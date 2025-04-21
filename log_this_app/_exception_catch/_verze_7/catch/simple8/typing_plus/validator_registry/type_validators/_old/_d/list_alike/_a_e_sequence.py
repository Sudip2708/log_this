from typing import Sequence, Any
from collections.abc import Sequence as SequenceOrigin

from ._list_alike_base import ListAlikeBase

T = Any

class SequenceValidator(ListAlikeBase):
    """
    Validátor pro zápis Sequence[T]

    Hint:
        Sequence[T] = Čtecí sekvence položek (např. tuple, list)
    """

    VALIDATOR_KEY = "sequence"
    ANNOTATION = Sequence[T]
    INFO = "Definuje čtecí sekvenci položek"
    GET_ORIGIN = SequenceOrigin
