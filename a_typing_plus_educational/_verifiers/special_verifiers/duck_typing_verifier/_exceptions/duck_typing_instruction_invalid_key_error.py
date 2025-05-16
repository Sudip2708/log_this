from typing import Any, Dict, Tuple
from ...._exceptions_base import VerifyParameterError


class VerifyDuckTypingInstructionInvalidKeyError(VerifyParameterError, KeyError):
    """Výjimka vyvolaná při zadání nevalidní instrukce pro duck typing."""

    title = "\n⚠ NEVALIDNÍ KLÍČ V INSTRUKCI PRO DUCK TYPING!\n"

    def __init__(
            self,
            value: Any,
            instruction: Dict[str, Any],
            key: Any,
            valid_keys: Tuple[str, ...]
    ):

        self.value = value
        self.instruction = instruction
        self.invalid_key = key
        self.valid_keys = valid_keys

        what_happened = [
            "   - Při pokusu o ověření duck typingu byl ve slovníku použit neplatný klíč instrukce.\n",
            f"   - Objekt který byl ověřován: {repr(self.value)}\n",
            f"   - Předaný slovník: {repr(self.instruction)}\n",
            f"   - Neplatný klíč: {repr(self.invalid_key)}\n",
            f"   - Dostupné klíče: {self._format_items(self.valid_keys)}\n"
        ]

        what_to_do = [
            "   - Zkontroluj název klíče ve slovníku instrukcí.\n",
            "   - Použij pouze klíče, které odpovídají podporovaným typům ověření.\n",
            "   - Pokud mezi klíči není vaše požadovaná operace, můžete ji buď předat jako lambda funkci.\n",
            "   - Případně pokud máte přístup do knihovny, můžete si definovat vlastní funkci a namapovat ji do duck typing logiky.\n",
            "   - Pro více informací navštive edukativní verzy této knihovny, kde jsou všechny tyto postupy vysvětlené.\n",
        ]

        super().__init__(what_happened, what_to_do, self.title)
