from cli_styler import (
    CliStyler, cli_style, add_style, cli_print,
)
from .styles import (
    LAVENDER, PINK, MAGENTA, DARK_GREEN, GREEN, LIGHT_GREEN,
    BLUE, LIGHT_PURPLE, PURPLE, BROWN, ORANGE, RED, LIGHT_RED,
    INTRO, INFO, LIST, SUCCESS, DROPDOWN, SELECTED, UNSELECTED,
    ERROR, WARNING, NO_SIGN, END_LINE, EMPTY_LINE,
)

__all__ = [

    ### Metody printeru
    "CliStyler",  # Hlavní třída Cli Styleru
    "cli_style",  # Metoda pro stylování dialogů
    "add_style",  # Metoda pro dinamické přidání nového stylu
    "cli_print",  # Metoda pro tisktnutí stylizovaného textu

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