# cli_styler/styles/styles_dict.py
"""
Hlavní slovník spojující všechny ostatní slovníky s jednotlivými styly
"""
from ._intro import INTRO_TITLE, INTRO_END
from ._menu import MENU_TITLE, MENU_OFFER, MENU_SELECTED
from ._hint import HINT_TITLE, HINT_TEXT
from ._error import ERROR_TITLE, ERROR_TEXT
from ._warning import WARNING_TITLE, WARNING_TEXT, WARNING_DIRECTION
from ._info import INFO_TITLE, INFO_TEXT
from ._success import SUCCESS_TITLE, SUCCESS_TEXT
from ._prompt import PROMPT_INPUT

# Klíče se musí shodovat s atributy třídy definovaných v CLIStyler
STYLES_DICT = {

    # Úvod a ukončení interaktivního režimu
    "intro_title"       : INTRO_TITLE,
    "intro_end"         : INTRO_END,

    # Položky pro interaktivní menu
    "menu_title"        : MENU_TITLE,
    "menu_offer"        : MENU_OFFER,
    "menu_selected"     : MENU_SELECTED,

    # Položky nápovědy pro ovládání interaktivního menu
    "hint_title"        : HINT_TITLE,
    "hint_text"         : HINT_TEXT,

    # Chybové oznamy
    "error_title"       : ERROR_TITLE,
    "error_text"        : ERROR_TEXT,

    # Varování
    "warning_title"     : WARNING_TITLE,
    "warning_text"      : WARNING_TEXT,
    "warning_direction" : WARNING_DIRECTION,

    # Informativní oznamy
    "info_title"        : INFO_TITLE,
    "info_text"         : INFO_TEXT,

    # Oznamy o úspěchu
    "success_title"     : SUCCESS_TITLE,
    "success_text"      : SUCCESS_TEXT,

    # Styl pro vstupní pole
    "prompt_input"      : PROMPT_INPUT,
}