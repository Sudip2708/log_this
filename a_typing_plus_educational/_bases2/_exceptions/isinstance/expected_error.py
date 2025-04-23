from .._bases import VerifyTypeError
from .._tools import format_expected


class IsInstanceExpectedError(VerifyTypeError):
    """Výjimka vyvolaná při nevalidní ověření isinstance pro expected."""

    title = "\n⚠ ZACHYCENA NEVALIDNÍ PARAMETR EXCEPTED!\n"

    def __init__(self, expected):
        self.expected = expected

        what_happened = [
            f"   - Zadán neplatný vstupní parametr 'expected' pro ověření hodnoty.\n"
            f"   - Zadaný parametr/parametry: {format_expected(self.expected)}\n",
            f"   - Parametr 'expected' musí být nativní typ, nebo tuple obsahující nativní typy\n",
        ]

        what_to_do = [
            "   - Zkontroluj hodnotu 'expected', kterou předáváte.\n",
            "   - Ujistěte se, že odpovídá očekávanému zadání.\n"
        ]

        super().__init__(what_happened, what_to_do)
