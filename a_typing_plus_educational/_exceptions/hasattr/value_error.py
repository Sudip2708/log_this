from .._bases import VerifyTypeError
from .._tools import format_missing


class HasAttributeValueError(VerifyTypeError):
    """Výjimka vyvolaná při neplatném typu hodnoty."""

    title = "\n⚠ ZACHYCENA NESHODA OČEKÁVANÝCH ATRIBUTŮ!\n"

    def __init__(self, value, annotation, missing):
        self.value = value
        self.annotation = annotation
        self.missing = missing

        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá požadovaným kritériím.\n"
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Očekávaná annotace: {repr(self.annotation)}\n",
            f"   - Chybějící atributy: {format_missing(self.missing)}\n"
        ]

        what_to_do = [
            "   - Zkontroluj definici hodnoty kterou předáváte.\n",
            "   - Ujistěte se, že obsahuje všecny potřebné atributy.\n"
        ]

        super().__init__(what_happened, what_to_do)


