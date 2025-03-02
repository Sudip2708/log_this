# cli_styler/styles/_info.py
"""
Definice stylů pro informační oznamy
INFO_TITLE: Nadpis
INFO_TEXT: Položky nápovědy
"""
from ..constants import (
    INFO, LIST,
    LIGHT_PURPLE, PURPLE,
    BOLD_REVERSE, NONE,
    CONTINUE
)


INFO_TITLE = {
    "symbol": INFO,
    "color": LIGHT_PURPLE,
    "style": BOLD_REVERSE,
    "end_line": CONTINUE
}

INFO_TEXT = {
    "symbol": LIST,
    "color": PURPLE,
    "style": NONE,
    "end_line": CONTINUE
}
