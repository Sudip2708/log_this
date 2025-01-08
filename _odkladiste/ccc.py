import re


def obalit_retezec(retezec, kody):
    """Obalí řetězec ANSI kódy."""
    return f"\033[{';'.join(map(str, kody))}m{retezec}\033[0m"


def rozebrat_a_slozit_retezec(retezec, kody):
    """Obalí všechny neformátované části řetězce zadanými ANSI kódy."""
    vysledek = ""
    posledni_konec = 0

    for match in re.finditer(r"\033\[.*?m", retezec):
        vysledek += obalit_retezec(retezec[posledni_konec:match.start()], kody)
        vysledek += match.group(0)
        posledni_konec = match.end()

    return vysledek + obalit_retezec(retezec[posledni_konec:], kody)


# Testovací vstupy
vstup1 = "Toto je text."
vstup2 = "Toto je \033[31mčervený text\033[0m a další část."
vstup3 = "\033[34mModrý\033[0m text a \033[32mzelený\033[0m."

# Výsledky
print(repr(rozebrat_a_slozit_retezec(vstup1, (31, 1))))  # Očekáváme celý text obalený červeně a tučně
print(repr(rozebrat_a_slozit_retezec(vstup2, (34,))))    # Neformátované části obaleny modře
print(repr(rozebrat_a_slozit_retezec(vstup3, (35, 4))))  # Neformátované části obaleny fialově a podtrženě
