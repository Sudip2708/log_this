from typing import Any, Tuple

from .._exceptions import VerifyArgumentsNotDictionaryError


def get_key_value_safe(
        inner_args: Tuple[Any, ...],
        annotation: Any = None,
):
    """
    Pomocná funkce pro ověření, že `get_args` vrátil právě dva vnořené typy (pro klíč a hodnotu slovníku).

    Používá se interně ve funkci `dictionary_validator`, kde slouží ke kontrole, že typová anotace
    odpovídá očekávanému formátu pro slovníky, tj. např. `dict[str, int]`, `Dict[CustomKey, CustomVal]` atd.

    """

    # Kontrola zda inner_args obsahuje pouze dvě položky
    if len(inner_args) == 2:
        return inner_args

    # Pokud ne, vyvolá se výjimka
    raise VerifyArgumentsNotDictionaryError(inner_args, annotation)