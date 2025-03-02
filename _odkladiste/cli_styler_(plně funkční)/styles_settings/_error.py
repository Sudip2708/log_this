# cli_styler/styles/_error.py
"""
Definice stylů pro oznamy chyb
ERROR_TITLE: Nadpis
ERROR_TEXT: Položky textu
"""
from ..constants import (
    ERROR, LIST,
    LIGHT_RED, RED,
    BOLD_REVERSE, NONE,
    END_LINE
)


ERROR_TITLE = {
    "symbol": ERROR,
    "color": LIGHT_RED,
    "style": BOLD_REVERSE,
    "end_line": END_LINE
}

ERROR_TEXT = {
    "symbol": LIST,
    "color": RED,
    "style": NONE,
    "end_line": END_LINE
}
