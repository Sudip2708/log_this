from .._bases import VerifyTypeError


class NumpyArrayValueError(VerifyTypeError):
    """Výjimka vyvolaná při nevalidních vlastnostech pole numpy.ndarray."""

    title = "\n⚠ ZACHYCENA NESHODA VLASTNOSTÍ NUMPY ARRAY!\n"

    def __init__(self, value, detail_message=None):
        self.value = value
        self.detail_message = detail_message

        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá požadovaným vlastnostem numpy.ndarray.\n",
            f"   - Ověřovaná hodnota: typ={type(self.value).__name__}\n",
        ]

        # Přidání detailů o array
        if hasattr(value, 'dtype'):
            what_happened.append(f"   - Datový typ (dtype): {value.dtype}\n")
        if hasattr(value, 'shape'):
            what_happened.append(f"   - Tvar (shape): {value.shape}\n")

        # Přidání detailní zprávy, pokud je poskytnuta
        if detail_message:
            what_happened.append(f"   - Detail: {detail_message}\n")

        what_to_do = [
            "   - Zkontrolujte dtype a tvar (shape) numpy pole.\n",
            "   - Ujistěte se, že odpovídá požadovaným vlastnostem v anotaci.\n"
        ]

        super().__init__(what_happened, what_to_do)