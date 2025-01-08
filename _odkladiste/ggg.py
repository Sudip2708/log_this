import re
from typing import Any
from _odkladiste._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS

def list_of_allowed_codes():
    """Vrací množinu povolených hodnot"""
    dictionary = {**TEXT_STYLES, **TEXT_COLORS, **BACKGROUND_COLORS}
    return set(dictionary.values())


def check_codes(codes):
    """Validuje kod"""
    for code in tuple(codes):
        if str(code) not in list_of_allowed_codes():
            raise ValueError(f"Neplatný kod: {code}, povolené hodnoty: {list_of_allowed_codes}")


def wrap_with_codes(text: str, codes: Any):
    """
    Obalí text danými ANSI kódy.
    """
    # Kontrola nezadání parametru codes
    if codes is None or not codes:
        return text

    #Pokud se jedná o str a nebo int
    if isinstance(codes, (int, str)):
        check_codes((codes,))
        return f"\033[{codes}m{text}\033[0m"

    if isinstance(codes, (list, set)):
        codes = tuple(set(codes))

    if len(codes) == 1:
        check_codes(codes)
        codes = codes[0]
        if not isinstance(codes, (int, str)):
            raise TypeError("Kód musí být int nebo str")
        return f"\033[{codes}m{text}\033[0m"

    try:
        codes_str = ";".join(str(code) for code in codes)
    except TypeError:
        raise TypeError("Všechny kódy musí být převoditelné na str")
    check_codes(codes)
    return f"\033[{codes_str}m{text}\033[0m"


def process_text(text, new_codes):
    """
    Zpracuje text s ohledem na ANSI sekvence a přidá nové kódy formátování.

    Args:
        text (str): Text obsahující ANSI sekvence a text mezi nimi.
        new_codes (set): Sada nových kódů pro obalení textu.

    Returns:
        str: Výsledný zpracovaný text.
    """
    # Regulární výraz pro hledání ANSI sekvencí a textu mezi nimi
    pattern = re.compile(r"\033\[[0-9;]*m|[^\033]+")
    # Množina aktuálních kódů získaných z textu
    current_codes = set()
    # Sestavení výsledného textu
    result = []

    # Iterace přes části textu
    for match in pattern.finditer(text):
        part = match.group(0)

        # Pokud jde o ANSI sekvenci
        if part.startswith("\033"):
            # Extrakce kódů ze sekvence
            codes = part[2:-1].split(";")  # Odebrání \033[ a m, rozdělení podle ";"

            if "0" in codes:  # Resetovací sekvence (obsahuje "0")
                current_codes.clear()  # Vyprázdnění aktuálních kódů
            else:
                current_codes.update(codes)  # Přidání kódů do množiny

        # Pokud jde o text
        else:
            if current_codes:  # Pokud existují kódy v current_codes
                formatted_part = wrap_with_codes(part, current_codes)
            else:  # Pokud žádné aktuální kódy nejsou, použijeme nové kódy
                formatted_part = wrap_with_codes(part, new_codes)

            result.append(
                formatted_part)  # Přidání naformátovaného textu do výsledku

    return "".join(result)




# Testovací vstupy
vstup1 = "Toto je text."
vstup2 = "Toto je \033[1;31mčervený text\033[0m a další část."
vstup3 = "\033[34mModrý\033[0m text a \033[32mzelený\033[0m."

# Výsledky
print(process_text(vstup1, (31, 1)))  # Očekáváme celý text obalený červeně a tučně
print(process_text(vstup2, (34,)))    # Neformátované části obaleny modře
print(process_text(vstup3, (35, 4)))  # Neformátované části obaleny fialově a podtrženě

# Výsledky
print(repr(process_text(vstup1, (31, 1))))  # Očekáváme celý text obalený červeně a tučně
print(repr(process_text(vstup2, (34,))))    # Neformátované části obaleny modře
print(repr(process_text(vstup3, (35, 4))))  # Neformátované části obaleny fialově a podtrženě