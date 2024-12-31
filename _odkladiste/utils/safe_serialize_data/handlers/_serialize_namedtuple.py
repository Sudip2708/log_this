from typing import Any, Set, Dict
from collections import namedtuple


def serialize_namedtuple(obj: namedtuple,
                          serialize_func: callable,
                          seen: Set[int],
                          depth: int) -> Dict[str, Any]:
    """
    Serializuje namedtuple objekty.

    Args:
        obj (namedtuple): Namedtuple objekt k serializaci.
        serialize_func (callable): Funkce pro rekurzivní serializaci.
        seen (Set[int]): Sada zpracovaných objektů.
        depth (int): Aktuální hloubka rekurze.

    Returns:
        Dict[str, Any]: Serializovaný slovník.
    """
    return serialize_func(obj._asdict(), seen, depth + 1)