# cli_styles.py
from ._cli_color import *

PRINT_STYLES = {
    "main.title": f"{BLUE_LIGHT} bold",
    "main.line": f"{BLUE_LIGHT}",
    "main.end": f"{BLUE_LIGHT}",
}

DIALOG_STYLES = {
    "selection.title": f"{GREEN_LIGHT} bold",
    "selection.focus": f"{GREEN_LIGHT} bold reverse",
    "selection.offer": F"{GREEN_DARK}",
    "instructions.title": f"{BLUE_VIOLET_LIGHT} bold",
    "instructions.offer": f"{BLUE_VIOLET_DARK}",
}