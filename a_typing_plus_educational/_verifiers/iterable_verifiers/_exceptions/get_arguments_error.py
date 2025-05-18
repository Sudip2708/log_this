from ..._exceptions_base import VerifyParameterError


class VerifyGetArgumentsError(VerifyParameterError):
    """Výjimka vyvolaná při neúspěšném získání argumentů pomocí get_args()."""

    title = "\n⚠ NELZE ZÍSKAT VNITŘNÍ TYPY Z ANOTACE!\n"

    def __init__(self, annotation):

        self.annotation = annotation

        what_happened = [
            f"   - Pokus o získání vnitřních typů z anotace selhal.\n"
            f"   - Problematická anotace: {repr(self.annotation)}\n",
            f"   - Anotace není kompatibilní s funkcí get_args() nebo nemá správnou strukturu.\n",
        ]

        what_to_do = [
            "   - Zkontrolujte, zda anotace je pro danou hodnotu správně zvolená.\n",
            "   - Je také možné, že jde jen o překlep v zápisu anotace.\n",
            "   - Anotace musí být generická (podporovat vnitřní typy a metodu get_origin z knihovny Typing).\n",
        ]

        super().__init__(what_happened, what_to_do)