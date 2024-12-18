from ._is_cyclic_reference import is_cyclic_reference
from ._is_primitive_type import is_primitive_type
from ._is_serializable_attribute import is_serializable_attribute
from ._is_serialization_depth_exceeded import is_serialization_depth_exceeded

__all__ = [
    "is_cyclic_reference",  # Detekuje cyklické reference v objektu.
    "is_primitive_type",  # Kontroluje, zda je objekt primitivního typu.
    "is_serializable_attribute",  # Kontroluje, zda je atribut vhodný pro serializaci.
    "is_serialization_depth_exceeded",  # Zkontroluje, zda aktuální hloubka rekurze překračuje maximální povolenou hloubku.
]