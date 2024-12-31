from typing import Any, Set, Optional
from collections import namedtuple  # Pro prospoznání '_asdict'

from .safe_serialize_data import *


def safe_serialize(
        obj: Any,
        max_depth: int,
        seen: Optional[Set[int]] = None,
        depth: int = 0
    ) -> Any:
    """
    Bezpečná serializace objektů pro logging s kontrolou času.

    Args:
        obj (Any): Objekt k serializaci.
        max_depth (int): Maximální povolená hloubka rekurze.
        seen (Optional[Set[int]], optional): Sada zpracovaných objektů. Defaults to None.
        depth (int, optional): Aktuální hloubka rekurze. Defaults to 0.

    Returns:
        Any: Serializovaný objekt nebo chybová zpráva.
    """
    try:
        # Kontrola maximální hloubky rekurze
        if depth >= max_depth:
            return f"<SerializationError: Maximum serialization depth exceeded>"

        # Inicializace množiny pro zápis rekurzivních objektů
        if seen is None:
            seen = set()

        # Kontrola přímé rekurze (objekty mají shodné ID)
        if id(obj) in seen:
            return "<SerializationError: Cyclic reference detected>"

        # Přidání aktuálního objektu do `seen`
        seen.add(id(obj))

        try:
            # Objekty s __dict__
            if hasattr(obj, '__dict__'):
                return serialize_object_with_dict(obj, safe_serialize, seen, depth)

            # Speciální typy
            if hasattr(obj, '_asdict'):  # namedtuple
                return serialize_namedtuple(obj, safe_serialize, seen, depth)

            if hasattr(obj, '__dataclass_fields__'):  # dataclass
                return serialize_dataclass(obj, safe_serialize, seen, depth)

            # Iterovatelné struktury
            if isinstance(obj, (list, tuple, set)):
                return serialize_iterable(obj, safe_serialize, seen, depth)

            # Slovníky
            if isinstance(obj, dict):
                return serialize_dict(obj, safe_serialize, seen, depth)

            # Základní typy
            if is_primitive_type(obj):
                return obj

            # Poslední záchrana
            return str(obj)

        except Exception as e:
            return f"<SerializationError: {str(e)}>"

        finally:
            seen.remove(id(obj))

    except Exception as e:
        return f"<SerializationError: {str(e)}>"