from typing import Any, Set


def is_cyclic_reference(obj: Any, seen: Set[int]) -> bool:
    """
    Detekuje cyklické reference v objektu.

    Args:
        obj (Any): Kontrolovaný objekt.
        seen (Set[int]): Sada již zpracovaných objektů.

    Returns:
        bool: True, pokud je detekována cyklická reference, jinak False.
    """
    return id(obj) in seen