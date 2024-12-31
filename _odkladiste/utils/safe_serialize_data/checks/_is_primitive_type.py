from typing import Any


def is_primitive_type(obj: Any) -> bool:
    """
    Kontroluje, zda je objekt primitivního typu.

    Args:
        obj (Any): Kontrolovaný objekt.

    Returns:
        bool: True pro primitivní typy, jinak False.
    """
    return isinstance(obj, (int, float, str, bool, type(None)))