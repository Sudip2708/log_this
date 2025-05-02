from .._bases import VerifyTypeError

class PandasValueError(VerifyTypeError):
    """Výjimka vyvolaná při nevalidních vlastnostech pandas objektů."""

    title = "\n⚠ ZACHYCENA NESHODA VLASTNOSTÍ PANDAS OBJEKTU!\n"

    def __init__(self, value, detail_message=None):
        self.value = value
        self.detail_message = detail_message

        what_happened = [
            f"   - Ověřovaný pandas objekt neodpovídá požadovaným vlastnostem.\n",
            f"   - Ověřovaný objekt: typ={type(self.value).__name__}\n",
        ]

        # Přidání detailů
        if hasattr(value, 'shape'):
            what_happened.append(f"   - Tvar (shape): {value.shape}\n")
        if hasattr(value, 'dtypes'):
            what_happened.append(f"   - Datové typy (dtypes): {value.dtypes}\n")
        elif hasattr(value, 'dtype'):
            what_happened.append(f"   - Datový typ (dtype): {value.dtype}\n")

        # Přidání detailní zprávy, pokud je poskytnuta
        if detail_message:
            what_happened.append(f"   - Detail: {detail_message}\n")

        what_to_do = [
            "   - Zkontrolujte vlastnosti pandas objektu.\n",
            "   - Ujistěte se, že odpovídá požadovaným parametrům v anotaci.\n"
        ]

        super().__init__(what_happened, what_to_do)