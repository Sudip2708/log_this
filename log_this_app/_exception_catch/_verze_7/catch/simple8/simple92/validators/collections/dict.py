from typing import TypeVar, get_origin, get_args

from ._base import BaseValidator
from ...verify import verify

class ListValidator(BaseValidator):

    NAME = "dict"
    TYPING = "Dict[K, V]"
    TYPE = dict

    @staticmethod
    def validate_items(value, expected_type, deep_check):
        inner_type = get_args(expected_type)
        return all(
            verify(ikey, inner_type[0])
            and verify(ivalue, inner_type[1])
            for ikey, ivalue in value.items()
        )

