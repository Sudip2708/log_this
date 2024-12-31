from typing import Any, Set, Dict


def serialize_object_with_dict(obj: Any,
                                serialize_func: callable,
                                seen: Set[int],
                                depth: int) -> Dict[str, Any]:
    """
    Serializuje objekty s __dict__ atributem.

    Args:
        obj (Any): Objekt k serializaci.
        serialize_func (callable): Funkce pro rekurzivní serializaci.
        seen (Set[int]): Sada zpracovaných objektů.
        depth (int): Aktuální hloubka rekurze.

    Returns:
        Dict[str, Any]: Serializovaný slovník.
    """
    result = {}
    for k, v in obj.__dict__.items():
        if not callable(v) and not k.startswith('_'):
            result[k] = serialize_func(v, seen, depth + 1)
    return result