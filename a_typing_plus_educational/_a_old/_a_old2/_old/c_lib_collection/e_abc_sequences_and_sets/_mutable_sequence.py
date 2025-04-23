from typing import MutableSequence
from collections.abc import MutableSequence as MutableSequenceOrigin

from ..._base_iterable_validator import BaseIterableValidator
from ..._base_type_variables import T


class MutableSequenceValidator(BaseIterableValidator):
    """
    Validátor pro zápis MutableSequence[T]

    Hint:
        MutableSequence[T] = Seznam s možností změny prvků
    """

    VALIDATOR_KEY = "mutable_sequence"
    ANNOTATION = MutableSequence[T]
    INFO = "Definuje zapisovatelnou sekvenci položek"
    ORIGIN = MutableSequenceOrigin
