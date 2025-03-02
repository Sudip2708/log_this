# cli_styler/styles/_intro.py
"""
Definice stylů pro zavedení a ukončení interaktivního režimu
INTRO_TITLE: Vstupní text interaktivního režimu
INTRO_END: Výstupní text interaktivního režimu
"""
from ..constants import (
    INTRO, NO_SIGN,
    BLUE,
    BOLD_REVERSE, NONE,
    END_LINE
)

INTRO_TITLE = {
    "symbol": INTRO,
    "color": BLUE,
    "style": BOLD_REVERSE,
    "end_line": END_LINE
}

INTRO_END = {
    "symbol": NO_SIGN,
    "color": BLUE,
    "style": NONE,
    "end_line": END_LINE
}
