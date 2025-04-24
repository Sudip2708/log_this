from ._verify_type_error import VerifyTypeError


class VerifyValueTypeError(VerifyTypeError):
    """Výjimka vyvolaná při neplatném typu hodnoty."""

    title = "\n⚠ ZACHYCENA NESHODA TYPU HODNOTY!\n"

    def __init__(self, value, expected):
        self._value = value
        self._expected = expected

        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá požadovaným kritériím.\n"
            f"   - Ověřovaná hodnota: {repr(value)}\n",
            f"   - Typ hodnoty: {type(value).__name__}\n",
            f"   - Požadovaný typ/typy: {self._format_expected()}\n"
        ]

        what_to_do = [
            "   - Zkontroluj typ hodnoty, kterou předáváte.\n",
            "   - Ujistěte se, že odpovídá očekávanému typu.\n"
        ]

        super().__init__(what_happened, what_to_do)

    def _format_expected(self):
        if isinstance(self._expected, tuple):
            return ', '.join(t.__name__ for t in self._expected)
        return self._expected.__name__

