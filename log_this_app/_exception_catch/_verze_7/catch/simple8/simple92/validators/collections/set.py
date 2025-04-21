from ._base import BaseValidator
from ...verify import verify

class ListValidator(BaseValidator):

    NAME = "set"
    TYPING = "Set[T]"
    TYPE = set

