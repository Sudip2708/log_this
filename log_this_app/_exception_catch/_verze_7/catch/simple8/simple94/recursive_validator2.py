from typing import List

from .typing_validate_error import TypingValidateError
from .get_command_and_content import _get_command_and_content


def recursive_validator(
        code,
        value,
        inner_check,
        extras = None
):
    """Rekurzivní metoda pro validaci kodu"""
    command, content = _get_command_and_content(code)

    try:

        # Provedení ověření
        a, b, c = command(content, value, extras, inner_check)
        new_value, new_extras, new_inner_check = a, b, c


        # Pokud je zaplá vnitřní kontrola
        if inner_check and content:

            # Rekurzivní volání pro hlubší úroveň porovnání
            recursive_validator(content, new_value, new_inner_check, new_extras)

        # Pokud není zaplá vnitřní kontrola (nebo je vyčerpaná) oznak o úspěšném ověření
        else:
            return True


    # Pokud dojde k vyvolání výjimky (Možná na místo výjimek jen předáváát chybovou zprávu)
    except Exception as e:
        raise TypingValidateError("Vnitřní chyba validace")