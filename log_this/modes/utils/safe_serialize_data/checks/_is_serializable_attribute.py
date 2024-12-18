from typing import Any


def is_serializable_attribute(key: str, value: Any) -> bool:
    """
    Kontroluje, zda je atribut vhodný pro serializaci.

    Args:
        key (str): Klíč atributu.
        value (Any): Hodnota atributu.

    Returns:
        bool: True, pokud je atribut vhodný pro serializaci, jinak False.
    """
    return not callable(value) and not key.startswith('_')