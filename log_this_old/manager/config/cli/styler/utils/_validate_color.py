from ..config import SUPPORTED_COLORS

def validate_color(color: str) -> bool:
    """Ověří, zda je barva podporována.

    Args:
        color: Název barvy k validaci

    Returns:
        True pokud je barva podporována

    Raises:
        ValueError: Pokud barva není podporována
    """
    if color not in SUPPORTED_COLORS.keys():
        raise ValueError(f"Neplatná barva: {color}")
    return True