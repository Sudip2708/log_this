# cli_styler/styles/_menu.py
"""
Definice stylů pro výběrové menu
MENU_TITLE: Nadpis
MENU_OFFER: Položky výběrového menu, které nejsou aktuálně vybrané
MENU_SELECTED: Aktuálně vybraná položka výběrového menu
"""
from ..constants import (
    DROPDOWN, UNSELECTED, SELECTED,
    DARK_GREEN, LIGHT_GREEN, GREEN,
    BOLD_REVERSE, NONE,
    END_LINE
)

MENU_TITLE = {
    "symbol": DROPDOWN,
    "color": DARK_GREEN,
    "style": BOLD_REVERSE,
    "end_line": END_LINE
}

MENU_OFFER = {
    "symbol": UNSELECTED,
    "color": LIGHT_GREEN,
    "style": NONE,
    "end_line": END_LINE
}

MENU_SELECTED = {
    "symbol": SELECTED,
    "color": GREEN,
    "style": BOLD_REVERSE,
    "end_line": END_LINE
}

