from .._bases import VerifyTypeError


class NeverValueError(VerifyTypeError):
    """Výjimka pro hodnoty, které nemohou být typu Never."""

    title = "\n⚠ NEPLATNÁ HODNOTA PRO TYP `Never`!\n"

    def __init__(self, value):
        self.value = value

        what_happened = [
            f"   - Byl zadán typově neplatný vstup: {repr(self.value)}\n",
            f"   - Typ `Never` značí, že hodnota by nikdy neměla existovat.\n"
        ]

        what_to_do = [
            "   - Možná se jedná o chybně navrženou větev nebo nesprávnou anotaci.\n"
            "   - Pokud se tato hodnota vůbec nemá vyskytovat, ujistěte se, "
            "že logika kódu k této části nedospěje.\n",
        ]

        super().__init__(what_happened, what_to_do)
