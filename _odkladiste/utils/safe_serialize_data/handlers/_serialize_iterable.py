from typing import Any, Set


def serialize_iterable(obj: Any,
                       serialize_func: callable,
                       seen: Set[int],
                       depth: int) -> list:
    """
    Serializuje iterovatelné struktury (list, tuple, set).

    Args:
        obj (Any): Iterovatelný objekt k serializaci.
        serialize_func (callable): Funkce pro rekurzivní serializaci.
        seen (Set[int]): Sada zpracovaných objektů.
        depth (int): Aktuální hloubka rekurze.

    Returns:
        list: Serializovaný seznam.
    """
    return [serialize_func(item, seen, depth + 1) for item in obj]