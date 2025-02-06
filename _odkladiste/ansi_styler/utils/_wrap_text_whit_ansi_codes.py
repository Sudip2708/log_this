print("_wrap_text_whit_ansi_codes.py")
from typing import Union, List, Tuple, Set

def wrap_text_whit_ansi_codes(
        text: str,
        codes: Union[str, int, List[str], Tuple[str, ...], Set[str]]
) -> str:
    """Wrap text with ANSI escape sequences.

    Args:
        text: Text to be wrapped
        codes: ANSI codes to apply

    Returns:
        Text wrapped with ANSI escape sequences
    """

    # Kontrola zda jsou dodané nějaké ansi kody pro formátování textu
    if not codes:
        # Pokud ano, bude vrácen pouze text
        return text

    # Kontrola, zda kody byli dodané jako množina, nebo seznam, nebo tuple
    if isinstance(codes, (list, tuple, set)):
        # Pokud ano, vytvoří se řetězec obsahující ansi kody oddělené středníkem
        codes_str = ";".join(str(code) for code in codes)

    # Pokud byl dodán pouze jeden kod samostatně
    else:
        # Převod kodu na str
        codes_str = str(codes)

    # Navrácení výstupního řetězce
    return f"\033[{codes_str}m{text}\033[0m"