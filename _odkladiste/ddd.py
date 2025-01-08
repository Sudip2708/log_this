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
    Obalí všechny neformátované části řetězce zadanými ANSI kódy.

    Args:
        retezec (str): Vstupní řetězec.
        kody (tuple): ANSI kódy pro obalení.

    Returns:
        str: Výsledný řetězec.
    """
    # Regulární výraz hledá celé formátovací sekvence (\033[...m) i text mezi nimi
    vzor = re.compile(r"(\033\[[0-9;]*m.*?\033\[0m)|([^\\033]+)")
    vysledek = ""

    for match in vzor.finditer(retezec):
        if match.group(1):  # Již naformátovaná část (ponechat beze změny)
            vysledek += match.group(1)
        elif match.group(2):  # Neformátovaný text
            vysledek += obalit_retezec(match.group(2), kody)

    return vysledek


# Testovací vstupy
vstup1 = "Toto je text."
vstup2 = "Toto je \033[31mčervený text\033[0m a další část."
vstup3 = "\033[34mModrý\033[0m text a \033[32mzelený\033[0m."

# Výsledky
print(rozebrat_a_slozit_retezec(vstup1, (31, 1)))  # Očekáváme celý text obalený červeně a tučně
print(rozebrat_a_slozit_retezec(vstup2, (34,)))    # Neformátované části obaleny modře
print(rozebrat_a_slozit_retezec(vstup3, (35, 4)))  # Neformátované části obaleny fialově a podtrženě


# Testovací vstupy
vstup1 = "Toto je text."
vstup2 = "Toto je \033[31mčervený text\033[0m a další část."
vstup3 = "\033[34mModrý\033[0m text a \033[32mzelený\033[0m."

# Výsledky
print(repr(rozebrat_a_slozit_retezec(vstup1, (31, 1))))  # Očekáváme celý text obalený červeně a tučně
print(repr(rozebrat_a_slozit_retezec(vstup2, (34,))))    # Neformátované části obaleny modře
print(repr(rozebrat_a_slozit_retezec(vstup3, (35, 4))))  # Neformátované části obaleny fialově a podtrženě
