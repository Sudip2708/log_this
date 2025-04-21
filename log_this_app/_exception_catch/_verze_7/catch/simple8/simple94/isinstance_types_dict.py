import builtins

EXCLUDED_TYPES = {
    "BuiltinImporter": "interní implementační třída, ne datový typ pro běžné použití",
    "classmethod": "dekorátor, ne datový typ",
    "property": "dekorátor, ne datový typ",
    "staticmethod": "dekorátor, ne datový typ",
    "enumerate": "funkce, ne datový typ",
    "filter": "funkce, ne datový typ",
    "map": "funkce, ne datový typ",
    "range": "funkce, ne datový typ (pro anotaci použij range z typing)",
    "reversed": "funkce, ne datový typ",
    "super": "funkce, ne datový typ",
    "zip": "funkce, ne datový typ"
}

def get_all_builtin_types() -> dict[str, type]:
    """Metoda vrátí slovník se všemi typy z knihovny builtins"""

    # Připravení prázdné množiny pro nalezené typy
    native_types = dict()

    # Cyklus procházející knihovnu builtins
    for name in dir(builtins):

        # Odfiltrování objektů, které se nedají použít jako typové anotace
        if name in EXCLUDED_TYPES:
            continue

        # Získání jména typů (možná rovnou vytvořit slovník)
        obj = getattr(builtins, name)
        if isinstance(obj, type):
            native_types[obj.__name__] = obj

    return native_types

ISINSTANCE_TYPES = get_all_builtin_types()

"""
Seznam vrácených položek:

Zde jsou ty, které lze používat přímo jako typové anotace:
✅ bool - datový typ logické hodnoty
✅ bytearray - datový typ pro modifikovatelné pole bajtů
✅ bytes - datový typ pro bajty
✅ complex - datový typ komplexních čísel
✅ dict - datový typ slovníku
✅ float - datový typ pro reálná čísla
✅ frozenset - datový typ nemodifikovatelné množiny
✅ int - datový typ celých čísel
✅ list - datový typ seznamu
✅ memoryview - datový typ pro přístup k interní paměti objektů
✅ object - základní datový typ (všechny ostatní typy dědí od něj)
✅ set - datový typ množiny
✅ slice - datový typ řezu
✅ str - datový typ pro řetězce
✅ tuple - datový typ n-tice
✅ type - datový typ pro třídy (lze přímo použít, ale v typových anotacích je vhodnější Type z modulu typing)

Zde jsou ty, které lze použít jako typové anotace, ale odkazují na výjimku:
❌ ArithmeticError - výjimka, ne datový typ
❌ AssertionError - výjimka, ne datový typ
❌ AttributeError - výjimka, ne datový typ
❌ BaseException - výjimka, ne datový typ
❌ BaseExceptionGroup - výjimka, ne datový typ
❌ BlockingIOError - výjimka, ne datový typ
❌ BrokenPipeError - výjimka, ne datový typ
❌ BufferError - výjimka, ne datový typ
❌ BytesWarning - výjimka, ne datový typ
❌ ConnectionAbortedError - výjimka, ne datový typ
❌ ConnectionError - výjimka, ne datový typ
❌ ConnectionRefusedError - výjimka, ne datový typ
❌ ConnectionResetError - výjimka, ne datový typ
❌ DeprecationWarning - výjimka, ne datový typ
❌ EncodingWarning - výjimka, ne datový typ
❌ EOFError - výjimka, ne datový typ
❌ Exception - výjimka, ne datový typ
❌ ExceptionGroup - výjimka, ne datový typ
❌ FileExistsError - výjimka, ne datový typ
❌ FileNotFoundError - výjimka, ne datový typ
❌ FloatingPointError - výjimka, ne datový typ
❌ FutureWarning - výjimka, ne datový typ
❌ GeneratorExit - výjimka, ne datový typ
❌ ChildProcessError - výjimka, ne datový typ
❌ ImportError - výjimka, ne datový typ
❌ ImportWarning - výjimka, ne datový typ
❌ IndentationError - výjimka, ne datový typ
❌ IndexError - výjimka, ne datový typ
❌ InterruptedError - výjimka, ne datový typ
❌ IsADirectoryError - výjimka, ne datový typ
❌ KeyboardInterrupt - výjimka, ne datový typ
❌ KeyError - výjimka, ne datový typ
❌ LookupError - výjimka, ne datový typ
❌ MemoryError - výjimka, ne datový typ
❌ ModuleNotFoundError - výjimka, ne datový typ
❌ NameError - výjimka, ne datový typ
❌ NotADirectoryError - výjimka, ne datový typ
❌ NotImplementedError - výjimka, ne datový typ
❌ OSError - výjimka, ne datový typ
❌ OverflowError - výjimka, ne datový typ
❌ PendingDeprecationWarning - výjimka, ne datový typ
❌ PermissionError - výjimka, ne datový typ
❌ ProcessLookupError - výjimka, ne datový typ
❌ RecursionError - výjimka, ne datový typ
❌ ReferenceError - výjimka, ne datový typ
❌ ResourceWarning - výjimka, ne datový typ
❌ RuntimeError - výjimka, ne datový typ
❌ RuntimeWarning - výjimka, ne datový typ
❌ StopAsyncIteration - výjimka, ne datový typ
❌ StopIteration - výjimka, ne datový typ
❌ SyntaxError - výjimka, ne datový typ
❌ SyntaxWarning - výjimka, ne datový typ
❌ SystemError - výjimka, ne datový typ
❌ SystemExit - výjimka, ne datový typ
❌ TabError - výjimka, ne datový typ
❌ TimeoutError - výjimka, ne datový typ
❌ TypeError - výjimka, ne datový typ
❌ UnboundLocalError - výjimka, ne datový typ
❌ UnicodeDecodeError - výjimka, ne datový typ
❌ UnicodeEncodeError - výjimka, ne datový typ
❌ UnicodeError - výjimka, ne datový typ
❌ UnicodeTranslateError - výjimka, ne datový typ
❌ UnicodeWarning - výjimka, ne datový typ
❌ UserWarning - výjimka, ne datový typ
❌ ValueError - výjimka, ne datový typ
❌ Warning - výjimka, ne datový typ
❌ ZeroDivisionError - výjimka, ne datový typ
"""
