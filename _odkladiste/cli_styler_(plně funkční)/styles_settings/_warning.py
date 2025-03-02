# cli_styler/styles/_warning.py
"""
Definice stylů pro varovný oznam
WARNING_TITLE: Nadpis
WARNING_TEXT: Položky oznamu
WARNING_DIRECTION: Směrování na provedený úkon
"""
from ..constants import (
    WARNING, LIST, SELECTED,
    LIGHT_RED, RED,
    BOLD_REVERSE, NONE,
    END_LINE, CONTINUE
)


WARNING_TITLE = {
    "symbol": WARNING,
    "color": LIGHT_RED,
    "style": BOLD_REVERSE,
    "end_line": CONTINUE
}

WARNING_TEXT = {
    "symbol": LIST,
    "color": RED,
    "style": NONE,
    "end_line": CONTINUE
}

WARNING_DIRECTION = {
    "symbol": SELECTED,
    "color": RED,
    "style": NONE,
    "end_line": END_LINE
}
