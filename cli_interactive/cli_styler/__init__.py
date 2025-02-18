from .cli_styler import (
    CLIStyler,
    intro_title, intro_end,
    menu_title, menu_offer, menu_selected,
    hint_title, hint_offer,
    error_title, error_text,
    warning_title, warning_text,
    info_title, info_text,
    success_title, success_text,
    cli_input
)

__all__ = [

    # Hlavní třída styleru
    "CLIStyler",

    # Styler pro uvodní část interaktivního režimu
    "intro_title",  # Vstup do interaktivního režimu
    "intro_end",  # Opuštění interaktivního režimu

    # Styelr pro interaktivní menu
    "menu_title",  # Nadpis menu
    "menu_offer",  # Položka menu
    "menu_selected",  # Vybraná položka menu

    # Styler pro nápovědu pro ovládání interaktivního menu
    "hint_title",  # Nadpis nápovědy
    "hint_offer",  # Položka nápovědy

    # Styler pro chybové oznamy
    "error_title",  # Nadpis chybového oznamu
    "error_text",  # Položka chybového oznamu

    # Styler pro varovné zprávy
    "warning_title",  # Nadpis varovné zprávy
    "warning_text",  # Položka varovné zprávy

    # Styler pro informativní oznamy
    "info_title",  # Nadpis informativního oznamu
    "info_text",  # Položka informativního oznamu

    # Styler pro oznamy o úspěšném provedení úkonu
    "success_title",  # Nadpis oznamu
    "success_text",  # Položka oznamu

    # Styler pro prompt input dialog (pro zadávání vstupních hodnot ručně)
    "cli_input",
]
