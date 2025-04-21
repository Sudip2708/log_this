import traceback
from logging import raiseExceptions
from typing import Any, Tuple, Union
import sys
import inspect
import os

# from .typing_validate_error import TypingValidateError

class ValidatorError(Exception):
    """Základní třída pro výjimky validace."""
    pass


class ValidatorTypeError(ValidatorError):
    """Výjimka pro chyby typování při validaci."""
    pass


"""
Co se stalo
Kde se to stalo
Jak to opravit
"""

def validate_native_type(
        value: Any,
        expected: Union[type, Tuple[type, ...]]
):
    """
    Ověření nativního typu.

    Vstupní parametry:
        value: Any - Hodnota pro ověření (Může mít jakoukoliv podobu)
        expected: Union[Type, ParamSpec] - typ pro ověření
            (Může být předán jako nativní type a nebo jako objekt získaný
            skrze metodu get_origin() z kknihovny typing)

    Popis vyřízení:
        - Metoda ověří, zda hodnota odpovídá předanému typu
        - Pokud ano vrátí True
        - Pokud ne Vyvolá výjimku s popisem

    Dodatečná ochrana:
        - try/except blok pro zachycení pádu během úkonu
        - Vrací podrobný report
    """
    try:

        # Ověření, zda hodnota odpovídá očekávané instanci
        if isinstance(value, expected):
            return True

        # Pokud ověření neprojde (a nevyvolá výjimku)
        # dojde k vytvoření výjimky informující o daném stavu

        # Získání textu očekávaných hodnot
        expected_message = (
            f"Požadované typy (instance): {', '.join(t.__name__ for t in expected)}"
            if isinstance(expected, tuple)
            else f"Požadovaný typ (instance): {expected.__name__}"
        )

        # Sestavení zjednodušené hierarchie volání
        stack = inspect.stack()
        hierarchy = ""
        for index, frame in enumerate(stack):
            if index > 0:
                hierarchy += (
                    f"   - {os.path.basename(frame.filename)}"
                    f" - {frame.lineno}"
                    f" - {frame.code_context[0].strip()}\n"
                )

        # Získání zachycení
        hierarchy += (
            f"   - {os.path.basename(__file__)}"
            f" - zde došlo k vyvolání výjimky funkcí: "
            f"validate_native_type(value, expected)\n"
        )

        # Vytvoření a vyvolání výjimky
        raise ValidatorTypeError(
            f"\n\n» Stručný přehled návazností (soubor - číslo řádku - kod řádku):\n"
            f"{hierarchy}"
            f"  (Odkazy naleznete ve výše uvedeném tracebacku.)\n"
            f"\n"
            f"⚠ ZACHYCENA NESHODA OVĚŘOVANÉ HODNOTY!\n"
            f"» Co se stalo:\n"
            f"   - Ověřovaná hodnota neodpovídá požadovaným kritériům.\n"
            f"   - Ověřovaná hodnota: {repr(value)}\n"
            f"   - Typ (instance) ověřované hodnoty: {type(value).__name__}\n"
            f"   - {expected_message}\n"
            f"» Jak to opravit:\n"
            f"   - Zkontrolujte kód volající tuto funkci a hodnoty které jsou předány a očekávány.\n"
        )




    # Puštění zpracovaných výjimek
    except ValidatorTypeError:
        raise

    # Zachycení výjimky způsobené špatně zadaným parametrem "expected_type"
    except TypeError as e:
        raise ValidatorParametrError(
            f"\nZadán neplatný vstupní parametr do funkce: validate_native_type(value, expected_type)\n"
            f"- Parametr expected_type must be a type, a tuple of types, or a union.\n"
            f"- Předaný parametr: {expected_type}\n"
            f"- Návrh řešení: Zkontrolujte kod volající tuto funkci. (Odkaz naleznete jako první záznam tracebacku).\n"
        )

    # Zachycení všech ostatních nečekaných výjimek
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()  # Získáme informace o aktuální výjimce
        stack = inspect.stack()  # Získáme celý stack frames (včetně volání z hlavního skriptu)
        caller_frame = stack[1]  # Frame který vyvolal naši funkci (o jednu úroveň výš než current frame)
        raise ValidatorUnexpectedError(
            f'\nZachycena neočekávaná vyjimka.\n'
            f'- Výjimka zachycena funkcí: validate_native_type(value, expected_type)\n'
            f'- Výjimku vyvolal kod: {caller_frame.code_context[0].strip()}\n'
            f'- Popis výjimky: {exc_type.__name__} = {str(exc_value)}\n'
            f'- Návrh řešení: Zkontrolujte popis výjimky a nahlédněte do záznamu tracebacku (výše).\n'
        )

validate_native_type("123", (int, bool))



        # return False
        # raise TypingValidateError(
        #     f"Ověření hodnoty selhalo. "
        #     f"Funkce validate_native_type(value, expected_type) "
        #     f"zjistila, že hodnota neodpovídá požadovanému typu. \n"
        #     f"Požadovaný typ: {expected_type}. "
        #     f"Typ ověřované hodnoty: {type(value)} "
        #     f"Ověřovaná hodnota: {repr(value)} \n"
        # )

        # # Případná druhá forma zápisu
        # raise TypingValidateError(
        #     f"[validate_native_type]: Ověření hodnoty selhalo: "
        #     f"Hodnota neodpovídá požadovanému typu. \n"
        #     f"Požadovaný typ: {expected_type}. "
        #     f"Typ ověřované hodnoty: {type(value)} "
        #     f"Ověřovaná hodnota: {value} \n"
        # )

    # return True

    # except TypingValidateError:
    #     raise
    #
    # except Exception as e:
    #     tb = traceback.extract_tb(e.__traceback__)[-1]
    #
    #     raise TypingValidateError(
    #         f"Neočekávaná chyba při ověření nativního typu. "
    #         f"Funkce: validate_native_type(value: Any, expected_type: Type). "
    #         f"Vstupní parametry: value={value}, expected_type={expected_type}. \n"
    #         f"Popis chyby: {e.__class__.__name__} - {str(e)}. \n"
    #         f"Soubor: {tb.filename}. "
    #         f"Řádek: {tb.lineno}. "
    #         f"Kod: {tb.line}. \n"
    #     )

# Příklady které projdou
# print(validate_native_type(123, int))
# print(validate_native_type("ahoj", str))
# print(validate_native_type(3.14, float))
# print(validate_native_type([1, 2, 3], list))
# print(validate_native_type((1, 2), tuple))

# # Příklady které selžou
# validate_native_type("123", int)  # Špatný typ - místo int je to str
# validate_native_type((1, 2, 3), list)  # Špatný typ - místo list je to tuple
# validate_native_type(10, float)  # Špatný typ - místo float je to int
# validate_native_type("True", bool)  # Špatný typ - místo bool je to string
