def apply_format(text: str, codes: list) -> str:
    """
    Obalí text zadanými ANSI kódy.

    Args:
        text (str): Text k obalení.
        codes (list): Seznam ANSI kódů jako řetězce.

    Returns:
        str: Formátovaný text s ANSI kódy.
    """
    codes_str = ";".join(map(str, codes))
    return f"\033[{codes_str}m{text}\033[0m"


import re


def process_text(text: str, new_codes: list) -> str:
    """
    Zpracuje text obsahující existující ANSI formátování a přidá nové formátování.

    Args:
        text (str): Text k úpravě, může obsahovat existující ANSI formátování.
        new_codes (list): Nové kódy pro formátování textu.

    Returns:
        str: Upravený text s kombinovaným formátováním.
    """
    # Regulární výraz na rozdělení textu (ANSI kódy a čistý text)
    pattern = re.compile(r"(\033\[[0-9;]*m)|([^\033]+)")

    # Inicializace výsledku a aktuálních kódů
    result = ""
    current_codes = set(new_codes)  # Používáme množinu pro jednodušší správu

    # Iterujeme přes všechny části textu
    for match in pattern.finditer(text):
        part = match.group(0)
        if part.startswith("\033"):  # Pokud jde o ANSI sekvenci
            # Extrakce kódů ze sekvence
            codes = part[2:-1].split(";")
            current_codes.update(codes)  # Přidání do aktuálních kódů
        else:  # Pokud jde o text
            # Obalíme text aktuálními kódy a přidáme do výsledku
            result += apply_format(part, sorted(current_codes))

    return result
