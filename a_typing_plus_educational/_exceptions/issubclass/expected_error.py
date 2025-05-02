from .._bases import VerifyTypeError
from .._tools import format_expected


class IsSubclassExpectedError(VerifyTypeError):
    """Výjimka vyvolaná při nevalidním parametru 'expected' pro ověření podtřídy."""

    title = "\n⚠ ZACHYCENA NEVALIDNÍ PARAMETR EXPECTED!\n"

    def __init__(self, expected):
        self.expected = expected

        what_happened = [
            f"   - Zadaný parametr 'expected' není platný pro ověření podtřídy.\n"
            f"   - Zadaný parametr/parametry: {format_expected(self.expected)}\n",
            f"   - Parametr 'expected' musí být nativní typ nebo n-tice typů.\n"
        ]

        what_to_do = [
            "   - Ověřte, že 'expected' obsahuje platný typ nebo tuple typů.\n",
            "   - Ujistěte se, že hodnota 'expected' je správně zadaná.\n"
        ]

        super().__init__(what_happened, what_to_do)
