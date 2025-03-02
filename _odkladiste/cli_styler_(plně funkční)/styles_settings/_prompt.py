# cli_styler/styles/_prompt.py
"""
Definice stylů pro pole pro zadání hodnoty
PROMPT_INPUT: Výzva pro zadání hodnoty
"""
from ..constants import (
    SELECTED,
    LAVENDER,
    BOLD,
    CONTINUE
)

PROMPT_INPUT = {
    "symbol": SELECTED,
    "color": LAVENDER,
    "style": BOLD,
    "end_line": CONTINUE
}

