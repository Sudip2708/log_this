from .._bases import VerifyTypeError

class ArrayValueError(VerifyTypeError):
    """Výjimka vyvolaná při nevalidním typovém kódu v poli typu array.array."""

    title = "\n⚠ ZACHYCENA NESHODA TYPOVÉHO KÓDU V ARRAY!\n"

    def __init__(self, value):
        self.value = value

        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá požadovanému typovému kódu.\n",
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
            f"   - Typový kód hodnoty: {self.value.typecode}\n",
        ]

        what_to_do = [
            "   - Zkontroluj typový kód pole.\n",
            "   - Ujistěte se, že odpovídá požadovanému typovému kódu.\n"
        ]

        super().__init__(what_happened, what_to_do)
