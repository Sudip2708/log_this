from .._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS

def get_available_styles() -> str:
    """
    Returns a formatted string containing all available styles organized by category.

    Returns:
        str: Formatted string with all available styles and their codes
    """

    # Proměnná pro seznam sekvencí výstupu
    output = []

    # Vnitřní funkce pro formátování výstupu
    def format_section(title: str, styles: dict) -> str:

        # Proměnná pro seznam sekvencí dané kategorie (obsahující její nadpis)
        section = [f"\n{title}:"]
        # Cyklus procházející slovník pro danou kategorii
        for name, code in sorted(styles.items()):
            # Vložení klíče a hodnoty do proměnné pro seznam sekvencí
            section.append(f"  {name}: {code}")
        # Vložení prázdného řádku oddělující jednotlivé kategorie
        return "\n".join(section)

    # Vytvoření a přídání sekvencí jednotlivých kategorií
    output.append(format_section("Text Styles", TEXT_STYLES))
    output.append(format_section("Text Colors", TEXT_COLORS))
    output.append(format_section("Background Colors", BACKGROUND_COLORS))

    # Navrácení spojeného textu z vrchu odděleného jednou řádkou
    return "\n".join(output)