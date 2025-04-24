from ._verify_type_error import VerifyTypeError


class VerifyExpectedTypeError(VerifyTypeError):
    """Výjimka vyvolaná při nevalidní hodnotě pro expected."""

    title = "\n⚠ ZACHYCENA NEVALIDNÍ PARAMETR EXCEPTED!\n"

    def __init__(self, expected):
        self._expected = expected

        what_happened = [
            f"   - Zadán neplatný vstupní parametr 'expected' pro ověření hodnoty.\n"
            f"   - Zadaný parametr/parametry: {self._format_expected}\n",
            f"   - Parametr 'expected' musí být nativní typ, nebo tuple obsahující nativní typy\n",
        ]

        what_to_do = [
            "   - Zkontroluj hodnotu 'expected', kterou předáváte.\n",
            "   - Ujistěte se, že odpovídá očekávanému zadání.\n"
        ]

        super().__init__(what_happened, what_to_do)

    def _format_expected(self):
        if isinstance(self._expected, tuple):
            return ', '.join(t.__name__ for t in self._expected)
        return self._expected.__name__
