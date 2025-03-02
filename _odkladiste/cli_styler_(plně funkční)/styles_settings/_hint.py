# cli_styler/styles/_hint.py
"""
Definice stylů pro nápovědu k používání interaktivního režimu
HINT_TITLE: Nadpis
HINT_TEXT: Položky nápovědy
"""
from ..constants import (
    INFO, LIST,
    PINK, MAGENTA,
    BOLD_REVERSE, NONE,
    END_LINE
)


HINT_TITLE = {
    "symbol": INFO,
    "color": PINK,
    "style": BOLD_REVERSE,
    "end_line": END_LINE
}

HINT_TEXT = {
    "symbol": LIST,
    "color": MAGENTA,
    "style": NONE,
    "end_line": END_LINE
}
