from typing import MutableSequence, Any
from collections.abc import MutableSequence as MutableSequenceOrigin

from ._list_alike_base import ListAlikeBase

T = Any

class MutableSequenceValidator(ListAlikeBase):
    """
    Validátor pro zápis MutableSequence[T]

    Hint:
        MutableSequence[T] = Seznam s možností změny prvků
    """

    VALIDATOR_KEY = "mutable_sequence"
    ANNOTATION = MutableSequence[T]
    INFO = "Definuje zapisovatelnou sekvenci položek"
    GET_ORIGIN = MutableSequenceOrigin
