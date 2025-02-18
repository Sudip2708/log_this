# cli_styles.py
from ._cli_color import *

### Styly pro cli_print()
PRINT_STYLES = {

    # Úvodní oznam a ukončení aplikace
    "cli_intro.title": f"{BLUE_LIGHT} bold reverse",
    "cli_intro.end": f"{BLUE_LIGHT}",

    # Výpis chyb
    "cli_error": f"{RED_DARK} bold reverse",

    # Oznamy
    "cli_info.title": f"{VIOLET_LIGHT} bold reverse",
    "cli_info.text": f"{VIOLET_DARK}",

    "cli_success.title": f"{ORANGE_YELLOW_LIGHT} bold reverse",
    "cli_success.text": f"{ORANGE_YELLOW_DARK}",


}

### Styly pro cli_style
DIALOG_STYLES = {

    # Interaktivní menu
    "cli_menu.title": f"{GREEN_DARK} bold reverse",
    "cli_menu.focus": f"{GREEN_LIGHT} bold reverse",
    "cli_menu.offer": f"{GREEN_DARK}",

    # Nápověda k ovládání interaktivního režimu
    "cli_hint.title": f"{BLUE_VIOLET_LIGHT} bold reverse",
    "cli_hint.offer": f"{BLUE_VIOLET_DARK}",

    # Styl pro prompt() pro zadání hodnoty
    "prompt": f"{VIOLET_LIGHT} bold",
    "input": f"{BLUE_LIGHT} bold",
}