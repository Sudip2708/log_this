from .signs import SIGNS_SET
from .colors import COLORS_SET

def get_styles_dict(sings_id, colors_id):

    # Definice proměnných
    s, c = SIGNS_SET, COLORS_SET
    si, ci = sings_id, colors_id
    b, br = " bold", " bold reverse"

    # Navrácení stylů
    return {
        # Název stylu      : (Úvodní znak,     Styl)
        "intro_title"      : (s["INTRO"][si],      c["BLUE"][ci] + br),
        "intro_end"        : (s["NO_SIGN"][si],    c["BLUE"][ci]),
        "menu_title"       : (s["DROPDOWN"][si],   c["DARK_GREEN"][ci] + br),
        "menu_offer"       : (s["UNSELECTED"][si], c["LIGHT_GREEN"][ci]),
        "menu_selected"    : (s["SELECTED"][si],   c["GREEN"][ci] + br),
        "hint_title"       : (s["INFO"][si],       c["PINK"][ci] + br),
        "hint_offer"       : (s["LIST"][si],       c["MAGENTA"][ci]),
        "error_title"      : (s["ERROR"][si],      c["LIGHT_RED"][ci] + br),
        "error_text"       : (s["LIST"][si],       c["RED"][ci]),
        "warning_title"    : (s["WARNING"][si],    c["LIGHT_RED"][ci] + br),
        "warning_text"     : (s["LIST"][si],       c["RED"][ci]),
        "warning_direction": (s["SELECTED"][si],   c["RED"][ci]),
        "info_title"       : (s["INFO"][si],       c["LIGHT_PURPLE"][ci] + br),
        "info_text"        : (s["LIST"][si],       c["PURPLE"][ci]),
        "success_title"    : (s["SUCCESS"][si],    c["BROWN"][ci] + br),
        "success_text"     : (s["LIST"][si],       c["ORANGE"][ci]),
        "prompt_input"     : (s["SELECTED"][si],   c["LAVENDER"][ci] + b)
    }