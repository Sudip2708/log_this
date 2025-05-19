from typing import Any, Tuple
from ...._exceptions_base import VerifyParameterError


class VerifyDuckTypingInstructionEmptyError(VerifyParameterError, KeyError):
    """Výjimka vyvolaná pokud instrukce pro duck typing jsou prázdné."""

    title = "\n⚠ INSTRUKCI PRO DUCK TYPING JSOU PRÁZDNÉ!\n"

    def __init__(
            self,
            value: Any,
    ):

        self.value = value

        what_happened = [
            "   - Pro ověření duck typingu byly předány prázdné instrukce.\n",
            f"   - Objekt který byl ověřován: {repr(self.value)}"
        ]

        what_to_do = [
            "   - Zkontroluj definici instrukcí které měli být pro ověření předané.\n",
            "   - Pokud nejsou předané žádné validační instrukce, je potřeba je doplnit.\n",
            "   - Ověření za pomoci Duck typink vyžaduje instrukce a bez nich toto ověření není možné.\n",
            "   - (V takovém případě stačí parametr duck_typing skrýt a nebo změnit na False)."

        ]

        super().__init__(what_happened, what_to_do, self.title)
