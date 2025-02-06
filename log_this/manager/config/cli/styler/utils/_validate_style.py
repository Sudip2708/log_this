from ..config import SUPPORTED_STYLES

def validate_style(style: str) -> bool:
    """Ověří, zda je styl podporován.

    Args:
        style: Název stylu k validaci

    Returns:
        True pokud je styl podporován

    Raises:
        ValueError: Pokud styl není podporován
    """
    if style not in SUPPORTED_STYLES.keys():
        raise ValueError(f"Neplatný styl: {style}")
    return True