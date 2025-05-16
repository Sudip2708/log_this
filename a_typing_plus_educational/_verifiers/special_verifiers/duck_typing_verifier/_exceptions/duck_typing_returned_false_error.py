from typing import Any, Dict, List
from ...._exceptions_base import VerifyValueError


class VerifyDuckTypingReturnedFalseError(VerifyValueError):
    """Výjimka vyvolaná při zadání nevalidní instrukce pro duck typing."""

    title = "\n⚠ DUCK TYPING VRÁTILO NEGATIVNÍ VÝSLEDEK!\n"

    def __init__(
            self,
            value: Any,
            instruction: Dict[str, Any],
            invalid_keys: List[str],
    ):

        self.value = value
        self.instruction = instruction
        self.invalid_keys = invalid_keys

        what_happened = [
            "   - Ověření hodnoty na základě duck typingu zachytilo negativní výsledek.\n",
            f"   - Objekt který byl ověřován: {repr(self.value)}.\n",
            f"   - Předaný slovník s instrukcemi: {repr(self.instruction)}.\n",
            f"   - Klíče které vrátili negativní výsledek: {self._format_items(self.invalid_keys)}\n"
        ]

        what_to_do = [
            "   - Zkontroluj ve slovníku s instrukcemi, zda je dobře definován příkaz k ověření.\n",
            "   - Pokud příkaz je v pořádku chyba je způsobena ověřovanou hodnotou, která neodpovídá nastavené kontrole.\n",
            "   - Opravte hodnotu a nebo pozměntě pravidla kontroli..\n",
            "   - Případně můžete prametr duck_typing skrýt a nebo nastavit na False a ověřovat podle typu.\n",
        ]

        super().__init__(what_happened, what_to_do, self.title)
