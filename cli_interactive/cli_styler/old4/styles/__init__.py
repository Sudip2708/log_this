from .dialog_styles import *
from .print_styles import *
from .signs import *

__all__ = [

    ### Sloníky se přdpřipravenými styly
    "DIALOG_STYLES",  # Slovník se styli pro dialogy
    "PRINT_STYLES",  # Slovník se styli pro print

    ### Konstanty s předpřipravenými barvami
    # Barvy použité v DIALOG_STYLES
    "LAVENDER",  # Použito pro: prompt
    "PINK",  # Použito pro: hint.title
    "MAGENTA",  # Použito pro: hint.offer
    "DARK_GREEN",  # Použito pro: menu.title
    "GREEN",  # Použito pro: menu.focus
    "LIGHT_GREEN",  # Použito pro: menu.offer

    # Barvy použité v PRINT_STYLES
    "BLUE",  # Použito pro: intro.title, intro.end
    "LIGHT_PURPLE",  # Použito pro: info.title
    "PURPLE",  # Použito pro: info.text
    "BROWN",  # Použito pro: success.title
    "ORANGE",  # Použito pro: success.text
    "RED",  # Použito pro: error.title
    "LIGHT_RED",  # Použito pro: error.text

    ### Konstanty s předpřipraveným stylizačními prvky
    "INTRO",  # Zobrazí: " ■ "
    "INFO",  # Zobrazí: " ☐ "
    "LIST",  # Zobrazí: " - "
    "SUCCESS",  # Zobrazí: " ☑ "
    "DROPDOWN",  # Zobrazí: " ▼ "
    "SELECTED",  # Zobrazí: " » "
    "UNSELECTED",  # Zobrazí: "   "
    "ERROR",  # Zobrazí: " ⛝ "
    "WARNING",  # Zobrazí: " ⚠ "
    "NO_SIGN",  # Předá: None
    "END_LINE",  # Předá: " \n"
    "EMPTY_LINE",  # Předá: "\n"
]