from typing import Any

from ...._exceptions_base import VerifyParameterError


class VerifyDuckTypingInstructionNotDictError(VerifyParameterError, TypeError):
    """
    Výjimka vyvolaná při neplatném zadání parametru `instruction`
    pro duck typing validaci. Očekáván je slovník s platnými klíči
    pro duck typing instrukce.
    """

    title = "\n⚠ PARAMETR PRO DUCK TYPING INSTRUKCI BYL ZADÁN V NEVALIDNÍM FORMÁTU!\n"

    def __init__(
            self,
            value: Any,
            instruction: Dict[str, Any]
    ):

        self.value = value
        self.instruction = instruction

        what_happened = [
            "   - Funkce pro ověření duck typing instrukce obdržela neplatný parametr.\n",
            "   - Očekáván byl slovník (`dict`) s odpovídajícími klíči (např. 'has_attr', 'lambda' atd.).\n",
            f"   - Objekt který byl ověřován: {repr(self.value)}.\n",
            f"   - Zadaná hodnota pro parametr očekávající slovník s instrukcemi: {repr(self.instruction)}\n",
            f"   - Typ této hodnoty: {type(self.instruction).__name__}\n",
        ]

        what_to_do = [
            "   - Zkontroluj, že parametr `instruction` je typu `dict`.\n",
            "   - Klíče musí odpovídat jedné z podporovaných instrukcí jako 'has_attr', 'lambda' apod.\n",
            "   - Hodnoty by měly odpovídat očekávanému formátu podle instrukce.\n",
        ]

        super().__init__(what_happened, what_to_do, self.title)
