from log_this.manager.config import get_config

def is_serialization_depth_exceeded(depth: int) -> bool:
    """
    Zkontroluje, zda aktuální hloubka rekurze překračuje maximální povolenou hloubku.

    Args:
        depth (int): Aktuální hloubka rekurze.

    Returns:
        bool: True, pokud je hloubka překročena, jinak False.
    """
    max_depth = get_config().max_depth
    return depth >= max_depth