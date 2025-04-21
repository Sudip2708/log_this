from typing import Any, Callable, Dict, List, Union
import typing

from .typing_validate_error import TypingValidateError
from .isinstance_types_dict import ISINSTANCE_TYPES

# Definice typové anotace pro typové anotace knihovny typing
TypingAnnotation = Any

def recursive_validator(
        command: Callable,  # Příkaz pro zpracování
        content: Union[List[str], str],  # Pokračování příkazu
        value: Any,  # Kontrolovaná hodnota
        type_annotation: TypingAnnotation,  # Typová anotace
        inner_check: Union[bool, int],  # Parametr definující, zda má dojít i k ověření vnitřního stavu
):

    try:

        # Provedení ověření
        a, b, c, d, e = command(content, value, type_annotation, inner_check)
        command, content, value, extras, inner_check = a, b, c, d, e

        # Ověření požadavku na vnitřní kontrolu
        if not inner_check or not content:
            return True

        # Rekurzivní volání pro hlubší úroveň porovnání
        recursive_validator(command, content, value, type_annotation, inner_check)


    # Předání případné výjimky ověření
    except TypingValidateError:
        raise

    # Zachycení všech ostaních výjimek
    except Exception as e:
        raise TypingValidateError("Vnitřní chyba validace")