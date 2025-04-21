import os
import traceback
import sys

def is_user_code(filename):
    """Vrací True, pokud soubor nepatří do systémového nebo knihovního kódu"""
    ignore_paths = [
        os.path.dirname(os.__file__),            # např. C:\Python312\Lib
        os.path.join(sys.prefix, 'lib'),         # systémové knihovny
        os.path.join(sys.prefix, 'lib', 'site-packages'),  # third-party packages
        # os.path.dirname(__file__),               # adresář této knihovny
    ]
    abs_filename = os.path.abspath(filename)
    return not any(abs_filename.startswith(p) for p in ignore_paths)


def get_user_stack(max_items=False):
    """Vrátí jen ty stack záznamy, které patří do uživatelského kódu"""

    # Načtení zásobníku a vynechání posledního záznamu (tento soubor)
    stack_summary = traceback.extract_stack()[:-1]

    # Vytvoření záznamů z uživatelem napsaného kodu
    user_frames = []
    for frame in reversed(stack_summary):
        if is_user_code(frame.filename):
            user_frames.append(frame)
            if max_items and len(user_frames) >= max_items:
                break
    return user_frames


def get_user_stack_text():
    user_trace = get_user_stack()
    # Stručný přehled návazností
    msg = ["» Stručný přehled návazností (soubor → kód):"]
    for frame in user_trace:
        filename = os.path.basename(frame.filename)
        code = frame.line.strip() if frame.line else ""
        msg.append(f"   - {filename} → {code}")
    if not user_trace:
        msg.append("   - (Žádný uživatelský kód nebyl nalezen ve stacku)")
    else:
        msg.append("  (Odkazy naleznete ve výše uvedeném tracebacku.)")
    return msg


class ValidatorTypeError(TypeError):

    TITLE = "\n\n⚠ ZACHYCENA NESHODA OVĚŘOVANÉ HODNOTY!"

    def __init__(self, value, expected, file, function_str):
        super().__init__()
        self.value = value
        self.expected = expected
        self.file_name = os.path.basename(__file__)
        self.function = function_str

    def __str__(self):
        return self.build_message()

    def build_message(self):
        value_type = type(self.value).__name__
        expected_types = (
            ', '.join([t.__name__ for t in self.expected])
            if isinstance(self.expected, tuple)
            else self.expected.__name__
        )

        # Nadpis a stručná přehled návazností
        msg = [
            "\n"
            "⚠ ZACHYCENA NESHODA OVĚŘOVANÉ HODNOTY!",
            *get_user_stack_text(),
            "» Co se stalo:",
            "   - Ověřovaná hodnota neodpovídá požadovaným kritériím.",
            f"   - Ověřovaná hodnota: {repr(self.value)}",
            f"   - Typ (instance) ověřované hodnoty: {value_type}",
            f"   - Požadované typy (instance): {expected_types}",
            "» Jak to opravit:",
            "   - Zkontrolujte kód volající tuto funkci a hodnoty, které jsou předány a očekávány."
        ]

        return "\n".join(msg)


def validate_native_type(value, expected):
    if not isinstance(value, expected):
        raise ValidatorTypeError(value, expected, __file__, "validate_native_type(value, expected)")


# Testovací volání
if __name__ == "__main__":
    validate_native_type("123", (int, bool))
