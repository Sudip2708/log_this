from .._bases import VerifyTypeError


class GetSelfClassKeyError(VerifyTypeError):
    """Výjimka vyvolaná při chybějícím klíči v custom_types."""

    title = "\n⚠ ZACHYCEN CHYBĚJÍCÍ KLÍČ V CONTEXTU PRO SELF!\n"

    def __init__(self, expected, context):
        self.expected = expected
        self.context = context

        what_happened = [
            f"   - V custom_types chybí požadovaný klíč: {repr(self.expected)}\n",
            f"   - Předaný context: {repr(self.context)}\n"
        ]

        what_to_do = [
            f"   - Přidej do custom_types klíč {repr(self.expected)} s hodnotou self.\n",
            "   - Například: custom_types = {'Self': self}\n"
        ]

        super().__init__(what_happened, what_to_do)




