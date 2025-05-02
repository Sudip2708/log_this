from .._bases import VerifyTypeError
from .._tools import format_expected


class IsSubclassValueError(VerifyTypeError):
    """Výjimka vyvolaná, když hodnota není podtřídou požadovaného typu."""

    title = "\n⚠ ZACHYCENA NESHODA PODTŘÍDY HODNOTY!\n"

    def __init__(self, value, expected):
        self.value = value
        self.expected = expected

        what_happened = [
            f"   - Ověřovaná hodnota není podtřídou požadované třídy nebo jejích typů.\n"
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
            f"   - Očekávaná třída/podtřída: {format_expected(self.expected)}\n"
        ]

        what_to_do = [
            "   - Zkontrolujte, zda hodnota je podtřídou požadovaného typu.\n",
            "   - Ujistěte se, že hodnota implementuje požadovanou třídu/podtřídu.\n"
        ]

        super().__init__(what_happened, what_to_do)
