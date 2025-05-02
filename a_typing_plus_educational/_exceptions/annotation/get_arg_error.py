from .._bases import VerifyTypeError
from .._tools import format_expected


class AnnotationGetArgsError(VerifyTypeError):
    """Výjimka vyvolaná při neúspěšném získání argumentů pomocí get_args()."""

    title = "\n⚠ NELZE ZÍSKAT VNITŘNÍ TYPY Z ANOTACE!\n"

    def __init__(self, annotation):
        self.annotation = annotation

        what_happened = [
            f"   - Pokus o získání vnitřních typů z anotace selhal.\n"
            f"   - Problematická anotace: {format_expected(self.annotation)}\n",
            f"   - Anotace není kompatibilní s funkcí get_args() nebo nemá správnou strukturu.\n",
        ]

        what_to_do = [
            "   - Zkontrolujte, zda anotace je správně formátovaná generická anotace.\n",
            "   - Ujistěte se, že používáte kompatibilní typ z modulu typing.\n"
        ]

        super().__init__(what_happened, what_to_do)