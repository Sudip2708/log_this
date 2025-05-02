from .._bases import VerifyTypeError


class GetSelfClassAttributeError(VerifyTypeError):
    """Výjimka vyvolaná při absenci atributu __class__ u objektu."""

    title = "\n⚠ ZACHYCENA NEPLATNÁ HODNOTA PRO KLÍČ SELF!\n"

    def __init__(self, expected, context):
        self.expected = expected
        self.context = context
        value = context.get(expected, None)

        what_happened = [
            f"   - Hodnota pro klíč {repr(self.expected)} nemá atribut __class__.\n",
            f"   - Získaná hodnota: {repr(value)}\n",
            f"   - Typ hodnoty: {type(value).__name__ if value is not None else 'Neznámý'}\n"
        ]

        what_to_do = [
            "   - Ujisti se, že hodnota odpovídající klíči je instance třídy (např. self).\n",
            f"   - Zkontroluj obsah custom_types[{repr(self.expected)}].\n"
        ]

        super().__init__(what_happened, what_to_do)



