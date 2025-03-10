def get_method_hierarchy(style_method):
    """
    Rozdělí objekt `styler.cli_print.warning.text` na jednotlivé úrovně
    a vrátí je jako seznam.
    """
    hierarchy = []

    # Začneme od posledního prvku (např. `text`)
    current = style_method

    while hasattr(current, "__self__"):  # Pokud existuje __self__, pokračujeme zpět
        hierarchy.append(current.__name__)  # Přidáme název metody (např. "text")
        current = current.__self__  # Posuneme se na vyšší úroveň

    # Na vrcholu je `cli_print`, který nemá `__self__`, přidáme jeho jméno
    hierarchy.append(current.__class__.__name__)

    return list(reversed(hierarchy))  # Otočíme pořadí, aby začínalo `styler`
