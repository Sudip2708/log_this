from .._bases import VerifyTypeError


class GetSelfClassTypeError(VerifyTypeError):
    """Výjimka vyvolaná při neplatném typu objektu custom_types."""

    title = "\n⚠ ZACHYCEN NEPLATNÝ TYP CONTEXTU PRO SELF!\n"

    def __init__(self, expected, context):
        self.expected = expected
        self.context = context

        what_happened = [
            "   - Kontext není indexovatelný (není např. typu dict).\n",
            f"   - Očekávaný klíč: {repr(self.expected)}\n",
            f"   - Předaná hodnota contextu: {repr(self.context)}\n",
            f"   - Typ hodnoty: {type(self.context).__name__}\n"
        ]

        what_to_do = [
            "   - Předávej do parametru `custom_types` objekt typu dict.\n",
            "   - Ujisti se, že obsahuje záznam s klíčem 'Self' a hodnotou self.\n"
        ]

        super().__init__(what_happened, what_to_do)



