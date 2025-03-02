# cli_styler/__init__.py
from .output import (
    CLIStyler,

    set_colors_mode, set_symbols_mode,
    get_current_symbols_mode, get_symbols_modes_dict,
    get_current_colors_mode, get_colors_modes_dict,



    get_styled_menu_title, get_styled_menu_offer, get_styled_menu_selected,
    get_styled_hint_title, get_styled_hint_text,
    get_styled_prompt_input,

    print_styled_intro_title, print_styled_intro_end,
    print_styled_error_title, print_styled_error_text,
    print_styled_warning_title, print_styled_warning_text, print_styled_warning_direction,
    print_styled_info_title, print_styled_info_text,
    print_styled_success_title, print_styled_success_text,

)

__all__ = [

    # Hlavní třída styleru
    "CLIStyler",

    # Nastavení modů
    "set_colors_mode",
    "set_symbols_mode",
    "get_current_symbols_mode", "get_symbols_modes_dict",
    "get_current_colors_mode", "get_colors_modes_dict",

    # Styelr pro interaktivní menu (vrací nastylovaný text)
    "get_styled_menu_title",  # Nadpis menu
    "get_styled_menu_offer",  # Položka menu
    "get_styled_menu_selected",  # Vybraná položka menu

    # Styler pro nápovědu pro ovládání interaktivního menu (vrací nastylovaný text)
    "get_styled_hint_title",  # Nadpis nápovědy
    "get_styled_hint_text",  # Položka nápovědy

    # Styler pro uvodní část interaktivního režimu (tiskne nastylovaný text)
    "print_styled_intro_title",  # Vstup do interaktivního režimu
    "print_styled_intro_end",  # Opuštění interaktivního režimu

    # Styler pro chybové oznamy (tiskne nastylovaný text)
    "print_styled_error_title",  # Nadpis chybového oznamu
    "print_styled_error_text",  # Položka chybového oznamu

    # Styler pro varovné zprávy (tiskne nastylovaný text)
    "print_styled_warning_title",  # Nadpis varovné zprávy
    "print_styled_warning_text",  # Položka varovné zprávy
    "print_styled_warning_direction",  # Směžovaní z varvoné zprávy

    # Styler pro informativní oznamy (tiskne nastylovaný text)
    "print_styled_info_title",  # Nadpis informativního oznamu
    "print_styled_info_text",  # Položka informativního oznamu

    # Styler pro oznamy o úspěšném provedení úkonu (tiskne nastylovaný text)
    "print_styled_success_title",  # Nadpis oznamu
    "print_styled_success_text",  # Položka oznamu

    # Styler pro prompt input dialog (pro zadávání vstupních hodnot ručně)
    "get_styled_prompt_input",
]
