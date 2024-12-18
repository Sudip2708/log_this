from typing import Any, Set, Dict


def serialize_dict(obj: Dict[Any, Any],
                   serialize_func: callable,
                   seen: Set[int],
                   depth: int) -> Dict[Any, Any]:
    """
    Serializuje slovníky.

    Args:
        obj (Dict[Any, Any]): Slovník k serializaci.
        serialize_func (callable): Funkce pro rekurzivní serializaci.
        seen (Set[int]): Sada zpracovaných objektů.
        depth (int): Aktuální hloubka rekurze.

    Returns:
        Dict[Any, Any]: Serializovaný slovník.
    """
    return {k: serialize_func(v, seen, depth + 1) for k, v in obj.items()}