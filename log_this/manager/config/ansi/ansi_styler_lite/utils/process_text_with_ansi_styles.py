from typing import List, Set
import re
from ._wrap_text_whit_ansi_codes import wrap_text_whit_ansi_codes

def process_text(text: str, codes: List[str]) -> str:
    """Process text with ANSI sequences and apply new codes.

    Args:
        text: Input text that may contain ANSI sequences
        codes: New formatting codes to apply

    Returns:
        Processed text with all formatting applied
    """

    # Natsavení vzoru pro vyhledávání ansi sekvencí a textu
    pattern = re.compile(r"\033\[[0-9;]*m|[^\033]+")
    # Proměnná pro případné vnořené ansi kody
    current_codes: Set[str] = set()
    # Proměná pro výsledný seznam kodů a textů
    result: List[str] = []

    # Cyklus pro hledání definovaných sekvencí
    for match in pattern.finditer(text):
        # Načtení sekvence z výsledku hledání
        part = match.group(0)

        # Pokud se jedná o sekvenci s ansi kodem
        if part.startswith("\033"):

            # Vytažení samotných kodů ze sekvence
            codes_in_text = part[2:-1].split(";")

            # Cyklus procházející nalezené kody
            for code in codes_in_text:

                # Kontrola, zda se nejedná o kod pro resetování stylu
                if code != 0:
                    #Pokud ne, dojde přidání kodu do množiny pro kody vnořených sekvencí
                    current_codes.update(codes_in_text)

                # Pokud se jedná kod pro resetování stylu
                else:
                    # Dojde k vymazání množiny pro kody z vnořených sekvencí
                    current_codes.clear()

        # Pokud se jedná o sekvenci s textem
        else:

            # Kontrola zda proměná pro kody vnořených sekvencí obsahuje kody
            if current_codes:
                # Pokud ano, část bude obalena s těmito kody
                formatted_part = wrap_text_whit_ansi_codes(part, current_codes)

            # Pokud proměná pro kody vnořených sekvencí je prázdná
            else:
                # Část bude obalena s vstupními kody této unkce
                formatted_part = wrap_text_whit_ansi_codes(part, codes)

            # Přidání výsledného řetězce do seznamu řetězců
            result.append(formatted_part)

    # Navrácení výsledku jako jednoho řetězce
    return "".join(result)