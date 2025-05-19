from typing import Any, Dict, List
from ...._exceptions_base import VerifyError


class VerifyDuckTypingGetExceptionError(VerifyError):
    """Výjimka vyvolaná při zadání nevalidní instrukce pro duck typing."""

    title = "\n⚠ BĚHEM OVĚŘOVÁNÍ HODNOTY NA ZÁKLADĚ DUCK TYPING BYLA ZACHYCENA VÝJIMKA!\n"

    def __init__(
            self,
            value: Any,
            instruction: Dict[str, Any],
            exceptions: Dict[str, Any],
    ):

        self.value = value
        self.instruction = instruction
        self.exceptions = exceptions


        what_happened = [
            "   - Ověření hodnoty na základě duck typingu zachytilo vyvolání výjimky.\n",
            f"   - Objekt který byl ověřován: {repr(self.value)}"
            f"   - Předaný slovník s instrukcemi: {repr(self.instruction)}",
            f"   - Klíče které vyvolali výjimku: {self._format_items(self.exceptions.keys())}\n"
        ]

        what_to_do = [
            "   - Zkontroluj níže uvedený výpis pro výjimky vyvolané danými klíči a zkus dohledat jejich příčinu.\n",
            "   - (Pravděpodobně se jedná o chybnou definici předané hodnoty, nebo chybně vybranou validační metodou).\n",
        ] + self._exceptions_report()

        super().__init__(what_happened, what_to_do, self.title)

    def _exceptions_report(self) -> List[str]:
        """Metoda pro výpis zachycených chyb"""

        # Seznam pro text popisující výjimky
        report = [
            "   - - - \n",
            "   - Výpis zachycených chyb:\n",
            "   - - - \n"
        ]

        # Procházení jednotlivých chybových záznamů
        for order, (key, exception) in enumerate(self.exceptions.items(), start=1):
            report.append(f"   - {order}) Výjimka zachycena pro klíč: {key}\n")
            report.append(f"   - Název výjimky: \n{getattr(exception, 'title', str(type(exception).__name__))}\n")
            report.append(f"   - Popis výjimky: \n{getattr(exception, 'what_happened', str(exception))}\n")
            report.append(f"   - Možnosti nápravy: \n{getattr(exception, 'what_to_do', '   - Zachycená výjimka je bez této nápovědy.')}\n")
            report.append(f"   - - - \n")

        # Navrácení připraveného textu
        return report


