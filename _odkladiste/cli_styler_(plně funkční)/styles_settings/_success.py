# cli_styler/styles/_success.py
"""
Definice stylů pro oznam o úspěšném provedení operace
SUCCESS_TITLE: Nadpis
SUCCESS_TEXT: Položky oznamu
"""
from ..constants import (
    SUCCESS, LIST,
    BROWN, ORANGE,
    BOLD_REVERSE, NONE,
    CONTINUE
)

SUCCESS_TITLE = {
    "symbol": SUCCESS,
    "color": BROWN,
    "style": BOLD_REVERSE,
    "end_line": CONTINUE
}

SUCCESS_TEXT = {
    "symbol": LIST,
    "color": ORANGE,
    "style": NONE,
    "end_line": CONTINUE
}
