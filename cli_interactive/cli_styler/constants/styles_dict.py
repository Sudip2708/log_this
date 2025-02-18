from .colors import *
from .signs import *

styles_dict = {
    # Název stylu      : (Úvodní znak,     Styl)
    "intro_title"      : (f"{INTRO}",      f"{BLUE} bold reverse"),
    "intro_end"        : (f"{NO_SIGN}",    f"{BLUE}"),
    "menu_title"       : (f"{DROPDOWN}",   f"{DARK_GREEN} bold reverse"),
    "menu_offer"       : (f"{UNSELECTED}", f"{LIGHT_GREEN}"),
    "menu_selected"    : (f"{SELECTED}",   f"{GREEN} bold reverse"),
    "hint_title"       : (f"{INTRO}",      f"{PINK} bold reverse"),
    "hint_offer"       : (f"{LIST}",       f"{MAGENTA}"),
    "error_title"      : (f"{ERROR}",      f"{LIGHT_RED} bold reverse"),
    "error_text"       : (f"{LIST}",       f"{RED}"),
    "warning_title"    : (f"{WARNING}",    f"{LIGHT_RED} bold reverse"),
    "warning_text"     : (f"{LIST}",       f"{RED}"),
    "info_title"       : (f"{INTRO}",      f"{LIGHT_PURPLE} bold reverse"),
    "info_text"        : (f"{INTRO}",      f"{PURPLE}"),
    "success_title"    : (f"{SUCCESS}",    f"{BROWN} bold reverse"),
    "success_text"     : (f"{LIST}",       f"{ORANGE}"),
    "cli_input"        : (f"{SELECTED}",   f"{LAVENDER} bold")
}