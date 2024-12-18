from typing import Any, Set, Dict
from dataclasses import fields


def serialize_dataclass(obj: Any,
                        serialize_func: callable,
                        seen: Set[int],
                        depth: int) -> Dict[str, Any]:
    """
    Serializuje dataclass objekty.

    Args:
        obj (Any): Dataclass objekt k serializaci.
        serialize_func (callable): Funkce pro rekurzivní serializaci.
        seen (Set[int]): Sada zpracovaných objektů.
        depth (int): Aktuální hloubka rekurze.

    Returns:
        Dict[str, Any]: Serializovaný slovník.
    """
    result = {}
    for field in fields(obj):
        result[field.name] = serialize_func(getattr(obj, field.name), seen, depth + 1)
    return result