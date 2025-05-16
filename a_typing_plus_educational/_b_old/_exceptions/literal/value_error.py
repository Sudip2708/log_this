from .._bases import VerifyTypeError


class LiteralValueError(VerifyTypeError):
    """Výjimka vyvolaná při neodpovídající hodnotě vůči definici Literal."""

    title = "\n⚠ ZACHYCENA NESHODA HODNOTY PRO LITERAL!\n"

    def __init__(self, value):
        self.value = value

        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá žádné hodnotě definované v `Literal`.\n",
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
        ]

        what_to_do = [
            "   - Zkontroluj, zda hodnota odpovídá některé z předdefinovaných hodnot.\n",
            "   - Ověř, že hodnoty v `Literal` jsou správně nastaveny.\n",
        ]

        super().__init__(what_happened, what_to_do)
