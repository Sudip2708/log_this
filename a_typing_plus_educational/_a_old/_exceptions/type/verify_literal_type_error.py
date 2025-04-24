from ._verify_type_error import VerifyTypeError


class VerifyLiteralTypeError(VerifyTypeError):
    """Výjimka vyvolaná při předání hodnoty mimo rozsah povolených hodnot Literal."""

    title = "\n⚠ ZACHYCENA NEPLATNÁ HODNOTA PRO LITERAL!\n"

    def __init__(self, value, allowed_values):
        self._value = value
        self._allowed_values = allowed_values

        what_happened = [
            f"   - Zadaná hodnota není mezi povolenými hodnotami typu `Literal`.\n",
            f"   - Ověřovaná hodnota: {repr(value)}\n",
            f"   - Typ hodnoty: {type(value).__name__}\n",
            f"   - Povolené hodnoty: {self._format_allowed()}\n"
        ]

        what_to_do = [
            "   - Použij jednu z předdefinovaných hodnot uvedených výše.\n",
            "   - Zkontroluj, zda není chyba v názvu nebo datovém typu.\n"
        ]

        super().__init__(what_happened, what_to_do)

    def _format_allowed(self):
        return ', '.join(repr(v) for v in self._allowed_values)
