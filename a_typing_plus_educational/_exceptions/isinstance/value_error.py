from .._bases import VerifyTypeError
from .._tools import format_expected


class IsInstanceValueError(VerifyTypeError):
    """Výjimka vyvolaná při neplatném typu hodnoty."""

    title = "\n⚠ ZACHYCENA NESHODA TYPU HODNOTY!\n"

    def __init__(self, value, expected):
        self.value = value
        self.expected = expected

        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá požadovaným kritériím.\n"
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
            f"   - Požadovaný typ/typy: {format_expected(self.expected)}\n"
        ]

        what_to_do = [
            "   - Zkontroluj typ hodnoty, kterou předáváte.\n",
            "   - Ujistěte se, že odpovídá očekávanému typu.\n"
        ]

        super().__init__(what_happened, what_to_do)


