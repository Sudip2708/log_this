from typing import Any
from collections.abc import Iterable


def is_iterable_container(obj: Any) -> bool:
    """Ověří zda jede o iterovatelný kontainer"""
    return (
            isinstance(obj, Iterable)
            and not isinstance(obj, (str, bytes, bytearray, memoryview))
    )