from .run import (
    cli_styler, cli_print, cli_style,

    get_menu_title, get_menu_offer, get_menu_selected,
    get_hint_title, get_hint_offer,
    get_prompt_input,

    print_intro_title, print_intro_end,
    print_error_title, print_error_text,
    print_warning_title, print_warning_text, print_warning_direction,
    print_info_title, print_info_text,
    print_success_title, print_success_text,

)

__all__ = [

    # Hlavní třída styleru
    "CLIStyler",

    # Styelr pro interaktivní menu (vrací nastylovaný text)
    "get_menu_title",  # Nadpis menu
    "get_menu_offer",  # Položka menu
    "get_menu_selected",  # Vybraná položka menu

    # Styler pro nápovědu pro ovládání interaktivního menu (vrací nastylovaný text)
    "get_hint_title",  # Nadpis nápovědy
    "get_hint_offer",  # Položka nápovědy

    # Styler pro uvodní část interaktivního režimu (tiskne nastylovaný text)
    "print_intro_title",  # Vstup do interaktivního režimu
    "print_intro_end",  # Opuštění interaktivního režimu

    # Styler pro chybové oznamy (tiskne nastylovaný text)
    "print_error_title",  # Nadpis chybového oznamu
    "print_error_text",  # Položka chybového oznamu

    # Styler pro varovné zprávy (tiskne nastylovaný text)
    "print_warning_title",  # Nadpis varovné zprávy
    "print_warning_text",  # Položka varovné zprávy
    "print_warning_direction",  # Směžovaní z varvoné zprávy

    # Styler pro informativní oznamy (tiskne nastylovaný text)
    "print_info_title",  # Nadpis informativního oznamu
    "print_info_text",  # Položka informativního oznamu

    # Styler pro oznamy o úspěšném provedení úkonu (tiskne nastylovaný text)
    "print_success_title",  # Nadpis oznamu
    "print_success_text",  # Položka oznamu

    # Styler pro prompt input dialog (pro zadávání vstupních hodnot ručně)
    "get_prompt_input",
]
