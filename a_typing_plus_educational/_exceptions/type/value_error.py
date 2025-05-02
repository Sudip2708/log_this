from .._bases import VerifyTypeError
from .._tools import format_expected


class TypeValueError(VerifyTypeError):
    """Výjimka vyvolaná při neplatné třídě nebo podtřídě."""

    title = "\n⚠ ZACHYCENA NESHODA TŘÍDY HODNOTY!\n"

    def __init__(self, value, expected):
        self.value = value
        self.expected = expected

        what_happened = [
            f"   - Ověřovaná hodnota není instancí očekávané třídy nebo její podtřídy.\n"
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
            f"   - Očekávaná třída/podtřída: {format_expected(self.expected)}\n"
        ]

        what_to_do = [
            "   - Ujistěte se, že hodnota je správným typem nebo podtypem.\n",
            "   - Zkontrolujte správnost očekávané třídy.\n"
        ]

        super().__init__(what_happened, what_to_do)
