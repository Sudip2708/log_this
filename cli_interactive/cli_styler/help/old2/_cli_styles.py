# cli_styles.py
from ._cli_color import *


BLUE = "#268bd2"
LAVENDER = "#d19bfe"
PINK = "#d270ba"
MAGENTA = "#c95fbb"
DARK_GREEN = "#4f9d4f"
GREEN = "#178f17"
LIGHT_GREEN = "#66cc66"
LIGHT_PURPLE = "#bf7fff"
PURPLE = "#ab72dc"
BROWN = "#bb8940"
ORANGE = "#f7a734"
RED = "#bb4040"
LIGHT_RED = "#e76b6b"


INTRO = " ■ "
INFO = " ☐ "
LIST = " - "
SUCCESS = " ☑ "
DROPDOWN = " ▼ "
SELECTED = " » "
UNSELECTED = "   "
ERROR = " ⛝ "
WARNING = " ⚠ "
NO_SIGN = None


### Styly pro cli_print()
PRINT_STYLES = {

    # Úvodní oznam a ukončení aplikace
    "cli_intro.title": f"{BLUE} bold reverse",
    "cli_intro.end": f"{BLUE}",

    # Výpis chyb
    "cli_error.title": f"{LIGHT_RED} bold reverse",
    "cli_error.text": f"{RED}",


    # Oznamy
    "cli_info.title": f"{LIGHT_PURPLE} bold reverse",
    "cli_info.text": f"{PURPLE}",

    "cli_success.title": f"{BROWN} bold reverse",
    "cli_success.text": f"{ORANGE}",


}

### Styly pro cli_style
DIALOG_STYLES = {

    # Interaktivní menu
    "cli_menu.title": f"{DARK_GREEN} bold reverse",
    "cli_menu.focus": f"{GREEN} bold reverse",
    "cli_menu.offer": f"{LIGHT_GREEN}",

    # Nápověda k ovládání interaktivního režimu
    "cli_hint.title": f"{PINK} bold reverse",
    "cli_hint.offer": f"{MAGENTA}",

    # Styl pro prompt() pro zadání hodnoty
    "prompt": f"{LAVENDER} bold",
}