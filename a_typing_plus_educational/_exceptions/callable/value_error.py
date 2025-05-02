from .._bases import VerifyTypeError


class CallableValueError(VerifyTypeError):
    """Výjimka vyvolaná při neplatné volatelnosti hodnoty."""

    title = "\n⚠ ZACHYCENA NEVOLATELNÁ HODNOTA!\n"

    def __init__(self, value):
        self.value = value

        what_happened = [
            f"   - Ověřovaná hodnota není volatelná (`callable`).\n",
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
        ]

        what_to_do = [
            "   - Zkontroluj, zda je hodnota správně definována jako volatelný objekt.\n",
            "   - Například funkce, metoda, nebo objekt s definovanou metodou __call__.\n"
        ]

        super().__init__(what_happened, what_to_do)
