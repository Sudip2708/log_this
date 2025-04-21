import traceback
import sys
import inspect

def new_exception_raiser():
    """
    Výstup:
        Výjimku zachycena v souboru: "C:\Users\Sudip2708\Documents\GitHub\log_this\log_this_app\_exception_catch\_verze_7\catch\simple8\simple94\validate_native_type.py"
        Modul: validate_native_type. Číslo řádku: 42. Kod řádku: new_exception_raiser()
        Výjimku vyvolal kod souboru: "C:\Users\Sudip2708\Documents\GitHub\log_this\log_this_app\_exception_catch\_verze_7\catch\simple8\simple94\validate_native_type.py"
        Modul: validate_native_type. Číslo řádku: 36. Kod řádku: if not isinstance(value, expected_type):
        Popis výjimky: TypeError = isinstance() arg 2 must be a type, a tuple of types, or a union
    """

    # Získáme informace o aktuální výjimce
    exc_type, exc_value, exc_traceback = sys.exc_info()

    # Získáme celý stack frames (včetně volání z hlavního skriptu)
    stack = inspect.stack()

    # Frame který vyvolal naši funkci (o jednu úroveň výš než current frame)
    caller_frame = stack[1]
    print(f'Výjimku zachycena v souboru: "{caller_frame.filename}"')
    print(
        f'Modul: {"n/a" if caller_frame.function == "<module>" else caller_frame.function}. Číslo řádku: {caller_frame.lineno}. Kod řádku: {caller_frame.code_context[0].strip()}')

    # Frame kde vznikla výjimka
    tb_list = traceback.extract_tb(exc_traceback)
    cause_frame = tb_list[0]
    print(f'Výjimku vyvolal kod souboru: "{cause_frame.filename}"')
    print(
        f'Modul: {cause_frame.name}. Číslo řádku: {cause_frame.lineno}. Kod řádku: {cause_frame.line}')

    # Typ a popis výjimky
    print(f'Popis výjimky: {exc_type.__name__} = {str(exc_value)}')