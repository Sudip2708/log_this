from ._base import BaseValidator
from ...verify import verify

class ListValidator(BaseValidator):

    NAME = "list"
    TYPING = "List[T]"
    TYPE = list

