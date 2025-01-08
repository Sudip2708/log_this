import re


def obalit_retezec(retezec, kody):
    """
    Obalí řetězec ANSI kódy.

    Args:
        retezec (str): Text k obalení.
        kody (tuple): ANSI kódy (např. (31, 1)).

    Returns:
        str: Řetězec obalený do zadaných kódů.
    """
    kody_str = ";".join(map(str, kody))
    return f"\033[{kody_str}m{retezec}\033[0m"


def rozebrat_a_slozit_retezec(retezec, kody):
    """
    Rozebere a složí řetězec tak, aby všechny neformátované části byly obaleny zadanými ANSI kódy.

    Args:
        retezec (str): Vstupní řetězec.
        kody (tuple): ANSI kódy pro obalení.

    Returns:
        str: Výsledný řetězec.
    """
    vysledek = ""
    posledni_konec = 0

    # Procházení všech formátovacích sekvencí
    for match in re.finditer(r"\033\[.*?m", retezec):
        start, end = match.span()

        # Zpracování neformátované části před sekvencí
        if start > posledni_konec:
            neformatovany = retezec[posledni_konec:start]
            vysledek += obalit_retezec(neformatovany, kody)

        # Přidání formátovací sekvence
        vysledek += match.group(0)
        posledni_konec = end

    # Zpracování zbytku řetězce
    if posledni_konec < len(retezec):
        neformatovany = retezec[posledni_konec:]
        vysledek += obalit_retezec(neformatovany, kody)

    return vysledek


# Testovací vstupy
vstup1 = "Toto je text."
vstup2 = "Toto je \033[31mčervený text\033[0m a další část."
vstup3 = "\033[34mModrý\033[0m text a \033[32mzelený\033[0m."

# Výsledky
print(rozebrat_a_slozit_retezec(vstup1, (31, 1)))  # Očekáváme celý text obalený červeně a tučně
print(rozebrat_a_slozit_retezec(vstup2, (34,)))    # Neformátované části obaleny modře
print(rozebrat_a_slozit_retezec(vstup3, (35, 4)))  # Neformátované části obaleny fialově a podtrženě
