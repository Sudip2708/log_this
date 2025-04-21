from ._verify_type_error import VerifyTypeError


class VerifyValueHasAttributeError(VerifyTypeError):
    """Výjimka vyvolaná při neplatném typu hodnoty."""

    title = "\n⚠ ZACHYCENA NESHODA OČEKÁVANÝCH ATRIBUTŮ!\n"

    def __init__(self, value, expected, annotation, missing):
        self._value = value
        self._expected = expected
        self._annotation = annotation
        self._missing = missing

        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá požadovaným kritériím.\n"
            f"   - Ověřovaná hodnota: {repr(self._value)}\n",
            f"   - Očekávaná annotace: {repr(self._annotation)}\n",
            f"   - Chybějící atributy: {self._format_missing()}\n"
        ]

        what_to_do = [
            "   - Zkontroluj definici hodnoty kterou předáváte.\n",
            "   - Ujistěte se, že obsahuje všecny potřebné atributy.\n"
        ]

        super().__init__(what_happened, what_to_do)

    def _format_missing(self):
        if isinstance(self._missing, tuple):
            return ', '.join(self._missing)
        return self._missing

