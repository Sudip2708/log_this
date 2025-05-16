from typing import Any, Optional, Union

from ._exceptions_base import VerifyUnexpectedInternalError, VerifyError
from ._tools import get_validate_class
from .value_verifiers import (
    is_instance_verifier,
    custom_types_verifier,
    self_verifier
)


def typing_verifier(
        value: Any,
        annotation: Any  = None,
        custom_types: Optional[dict] = None,
        inner_check: Union[bool, int] =True,
        duck_typing: bool  = False,
        bool_only: bool  = False
):
    """
    Hlavní funkce pro validaci na základě typových anotací

    Rozbor vstupních hodnot:
        value: Any,  # Hodnota která se má ověřit
        annotation: Any  = None,  # Typová onotace podle které se má ověřit
        custom_types: Optional[dict] = None,  # Specifikace vlastních typů, a tříd, předaných jako tuple pro kontrolu vzorů
        inner_check: Union[bool, int] =True,  # Parametr nastavující zda se má provádět i hloubková kontrola (a jak moc hluboko)
        duck_typing: bool  = False,  # Nastavení zda se má provádět kontrola jen na základě duck typing porovnání
        bool_only: bool  = False  # Specifkace zda vyvysovat neshody jako výjimky a nebo jen vracet false


    Rozbor logiky:

        # Přednostní vyřízení nativních typů
        # Nativní typy neobsahují vnitřní prvky a tak se hned vracejí
        # (nevstahuje se na ně ani ověření přes duck typing a ani přes předané vlastní typi)
        if isinstance(annotation, type):
            return is_instance_verifier(value, annotation, bool_only)

        # Získání validační třídy
        # Pokud byla získána validační třídy
        # Volání validační logiky definované pro danou anotaci
        validate_class = get_validate_class(annotation)
        if validate_class:
            return validate_class(value, annotation, custom_types, duck_typing, inner_check, bool_only)

        # Pokud validační třída pro anotaci nebyla nalezena
        # Kontrola zda je přidán parametr pro vlastní anotace (klíčem slovníku)
        # Validace na základě předaných dat
        if custom_types and annotation in custom_types:
            return custom_types_verifier(value, custom_types[annotation], duck_typing, inner_check, bool_only)

        # Pokud nebyla anotace zachycena, dojde k ověření zda nemá implementované validační metody
        # Self validátor by měla být funkce která se pokusí prohledat objekt na všechny možné způsoby nastavení sebevalidace
        # Když selže vyvolá výjimku která se pak zpracuje vě větvi except
        return self_verifier(value, annotation, bool_only)
    """

    try:

        # Přednostní vyřízení nativních typů (na nativní typy se nepoužívá duck typing)
        if isinstance(annotation, type):
            return is_instance_verifier(value, annotation, bool_only)

        # Vyřízení na základě validační třídy
        validate_class = get_validate_class(annotation)
        if validate_class:
            return validate_class(
                value,
                annotation,
                custom_types,
                duck_typing,
                inner_check,
                bool_only
            )

        # Vyřízení na základě vlastních anotací
        if custom_types and annotation in custom_types:
            return custom_types_verifier(
                value,
                custom_types[annotation],
                duck_typing,
                inner_check,
                bool_only
            )

        # Vyřízení na základě vnitřních validátorů objektu
        return self_verifier(value, annotation, bool_only)

    # Propagace vnitřních výjimek
    except VerifyError:
        raise

    # Zachycení všech neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e

