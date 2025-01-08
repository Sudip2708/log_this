import re


def sloucit_ansi_kody(retezec):
    """
    Sloučí vedle sebe stojící ANSI kódy do jedné sekvence.

    Args:
        retezec (str): Řetězec s ANSI kódy.

    Returns:
        str: Řetězec se sloučenými ANSI kódy.
    """
    # Regulární výraz hledá sekvence typu \033[<kód1>m\033[<kód2>m
    vzor = re.compile(r"(\033\[)([0-9;]*)(m)(\033\[)([0-9;]*)(m)")

    def nahradit(match):
        # Spojí kódy oddělené středníkem
        sloucene_kody = ";".join(filter(None, [match.group(2), match.group(5)]))
        return f"{match.group(1)}{sloucene_kody}{match.group(3)}"

    while vzor.search(retezec):
        retezec = vzor.sub(nahradit, retezec)

    return retezec


def rozdelit_na_casti(retezec):
    """
    Rozdělí řetězec na části obsahující buď ANSI kódy, nebo text.

    Args:
        retezec (str): Řetězec s ANSI kódy.

    Returns:
        list: Seznam částí (texty a ANSI sekvence jako samostatné řetězce).
    """
    # Regulární výraz hledá ANSI sekvence a text
    vzor = re.compile(r"(\033\[[0-9;]*m)|([^\033]+)")
    vysledek = []

    for match in vzor.finditer(retezec):
        if match.group(1):  # ANSI sekvence
            vysledek.append(match.group(1))
        elif match.group(2):  # Text
            vysledek.append(match.group(2))

    return vysledek


# Vstupní řetězec
vstup = "\033[34mModrý\033[0m text a \033[32m\033[1mzelený\033[0m\033[0m."

# 1. Sloučení ANSI kódů
vstup_slouceny = sloucit_ansi_kody(vstup)
print("Po sloučení ANSI kódů:", repr(vstup_slouceny))

# 2. Rozdělení na části
casti = rozdelit_na_casti(vstup_slouceny)
print("Rozdělené části:", casti)
