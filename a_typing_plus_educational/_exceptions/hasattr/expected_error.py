from .._bases import VerifyTypeError
from .._tools import format_expected


class HasAttributeExpectedError(VerifyTypeError):
    """Výjimka vyvolaná při nevalidní hodnotě pro expected."""

    title = "\n⚠ ZACHYCENA NEVALIDNÍ PARAMETR EXCEPTED!\n"

    def __init__(self, expected):
        self.expected = expected

        what_happened = [
            f"   - Zadán neplatný vstupní parametr 'expected' pro ověření atributů hodnoty.\n"
            f"   - Zadaný parametr/parametry: {format_expected(self.expected)}\n",
            f"   - Parametr 'expected' musí být řetězec názvu atributu, nebo tuple obsahující tyto řetězce\n",
        ]

        what_to_do = [
            "   - Zkontroluj hodnotu 'expected', kterou předáváte.\n",
            "   - Ujistěte se, že odpovídá očekávanému zadání.\n"
        ]

        super().__init__(what_happened, what_to_do)
