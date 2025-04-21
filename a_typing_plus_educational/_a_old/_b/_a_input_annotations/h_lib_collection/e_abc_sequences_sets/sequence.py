from typing import Sequence
from collections.abc import Sequence as SequenceOrigin

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class SequenceValidator(BaseIterableValidator):
    """
    Validátor pro zápis Sequence[T]

    Hint:
        Sequence[T] = Čtecí sekvence položek (např. tuple, list)
    """

    VALIDATOR_KEY = "sequence"
    ANNOTATION = Sequence[T]
    INFO = "Definuje čtecí sekvenci položek"
    GET_ORIGIN = SequenceOrigin
