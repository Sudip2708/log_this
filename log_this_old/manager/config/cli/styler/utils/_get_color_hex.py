from ..config import SUPPORTED_COLORS
from ._validate_color import validate_color


def get_color_hex(color: str) -> str:
    """Vrátí hex kód pro zadaný název barvy.

    Args:
        color: Název barvy k vyhledání

    Returns:
        Hex kód odpovídající barvě

    Raises:
        ValueError: Pokud barva není podporována
    """
    if validate_color(color):
        return SUPPORTED_COLORS[color]
    return ''  # Nikdy se neprovede kvůli raise v validate_color
