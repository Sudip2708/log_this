# base_validator.py
from typing import TypeVar, get_origin, get_args
from abc import ABC, abstractmethod
from ...verify import verify

class BaseValidator(ABC):
    """Základní třída pro validátory typů."""

    NAME = None
    TYPING = None
    TYPE = None

    def __str__(self):
        return f"Validator for {self.TYPING} types"

    def validate_type(self, value):
        """Ověří základní typ."""
        return isinstance(value, self.TYPE)

    @staticmethod
    def validate_items(value, expected_type, deep_check):
        inner_type = get_args(expected_type)
        return all(
            verify(item, inner_type, deep_check)
            for item in value
        )



