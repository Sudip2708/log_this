from .checks import (
    is_cyclic_reference,
    is_primitive_type,
    is_serializable_attribute,
    is_serialization_depth_exceeded
)

from .handlers import (
    serialize_dataclass,
    serialize_dict,
    serialize_iterable,
    serialize_namedtuple,
    serialize_object_with_dict
)

__all__ = [
    "is_cyclic_reference",  # Detekuje cyklické reference v objektu.
    "is_primitive_type",  # Kontroluje, zda je objekt primitivního typu.
    "is_serializable_attribute",  # Kontroluje, zda je atribut vhodný pro serializaci.
    "is_serialization_depth_exceeded",  # Zkontroluje, zda aktuální hloubka rekurze překračuje maximální povolenou hloubku.

    "serialize_dataclass",  # Serializuje dataclass objekty.
    "serialize_dict",  # Serializuje slovníky.
    "serialize_iterable", # Serializuje iterovatelné struktury (list, tuple, set).
    "serialize_namedtuple",  # Serializuje namedtuple objekty.
    "serialize_object_with_dict",  # Serializuje objekty s __dict__ atributem.
]