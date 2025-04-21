import os
import traceback
import sys
import site
from typing import Any, Union, Tuple

class VerifyError(Exception):
    """VZákladní výjimky knihovny Verify."""

class VerifyUnexpectedError(VerifyError):
    """Výjimka vyvolaná při neočekávané události."""

class VerifyTypeError(VerifyError, TypeError):
    """Výjimka vyvolaná při neplatném ověření hodnoty."""


def is_user_code(filename):
    """Vrací True, pokud soubor nepatří do systémového nebo knihovního kódu"""

    if not filename or filename == '<string>':
        return False

    abs_filename = os.path.abspath(filename)

    # Ignorované cesty - systémové a knihovní kód
    ignore_paths = [
        os.path.dirname(os.__file__),  # standardní knihovna
        *site.getsitepackages(),  # nainstalované balíčky
        site.getusersitepackages(),  # uživatelské balíčky
    ]

    # Dodatečné vzory pro ignorování
    ignore_patterns = ['site-packages', 'dist-packages', '.venv', 'virtualenv',
                       'venv']

    # Kombinovaná kontrola cest a vzorů
    return not (
        any(path and abs_filename.startswith(path) for path in ignore_paths) or
        any(pattern in abs_filename for pattern in ignore_patterns)
    )


def get_simplified_traceback():
    """Vrátí zjednodušený traceback ošetřený o systémové záznamy"""
    try:
        # Získání aktuálního tracebacku
        _, _, tb_obj = sys.exc_info()
        stack_summary = (
            traceback.extract_tb(tb_obj) if tb_obj
            else traceback.extract_stack()[ :-2]  # Odstraníme 2 poslední záznamy (pro tuto funkci, a předešlou)
        )

        trace_lines = ["» Stručný přehled návazností (kód řádku → podrobnosti):"]

        for frame in stack_summary:
            if is_user_code(frame.filename):
                module_info = f" → [modul: {frame.name}]" if frame.name != "<module>" else ""
                trace_lines.append(
                    f"   - {frame.line}"
                    f" → [file: {os.path.basename(frame.filename)}]"  
                    f" → [line: {frame.lineno}]"
                    + module_info
                )

        trace_lines.append(
            "   (Ve výše uvedeném tracebacku nebyl nalezen žádný odkaz na uživatelem vytvořený kód.)"
            if len(trace_lines) == 1
            else "  (Odkazy k dispozici výše, v podrobném výpisu tracebacku.)"
        )

        return "\n".join(trace_lines)

    except Exception as e:
        # Ošetření případů, kdy by samotná funkce způsobila chybu
        return f"Chyba při generování zjednodušeného tracebacku: {e}"

def validate_native_type(value: Any, expected: Union[type, Tuple[type, ...]]) -> bool:
    """
    Ověří, zda zadaná hodnota odpovídá očekávanému typu (nebo více typům).

    Args:
        value (Any): Hodnota, která má být ověřena.
        expected (Union[type, Tuple[type, ...]]): Očekávaný typ nebo n-tice typů.

    Returns:
        bool: True, pokud typ odpovídá.

    Raises:
        ValidatorTypeError: Pokud hodnota neodpovídá očekávanému typu.
    """

    if isinstance(value, expected):
        return True

    expected_text = (
        f"Požadované typy (instance): {', '.join(t.__name__ for t in expected)}"
        if isinstance(expected, tuple)
        else f"Požadovaný typ (instance): {expected.__name__}"
    )

    raise VerifyTypeError(
        f"\n{get_simplified_traceback()}\n"
        "\n⚠ ZACHYCENA NESHODA OVĚŘOVANÉ HODNOTY!\n"
        "» Co se stalo:\n"
        f"   - Ověřovaná hodnota neodpovídá požadovaným kritériím.\n"
        f"   - Ověřovaná hodnota: {repr(value)}\n"
        f"   - Typ (instance) ověřované hodnoty: {type(value).__name__}\n"
        f"   - {expected_text}\n"
        "» Jak to opravit:\n"
        "   - Zkontrolujte kód volající tuto funkci a hodnoty, které jsou předány a očekávány.\n"
        "   - Prohlédněte si stručný přehled návazností (výše), zda chybu neoběvíte tam."
    )


validate_native_type("123", (int, bool))