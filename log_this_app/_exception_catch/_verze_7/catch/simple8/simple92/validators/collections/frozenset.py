from ._base import BaseValidator
from ...verify import verify

class ListValidator(BaseValidator):

    NAME = "frozenset"
    TYPING = "FrozenSet[T]"
    TYPE = frozenset

