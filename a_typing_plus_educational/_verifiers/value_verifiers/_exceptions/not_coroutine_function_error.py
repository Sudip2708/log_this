from typing import Any

from ..._exceptions_base import VerifyValueError


class VerifyNotCoroutineFunctionError(VerifyValueError, ValueError):

    # Specifický nadpis pro chyby nevolatelných hodnot
    title = "\n⚠ ZACHYCEN OBJEKT KTERÝ NENÍ COROUTINE FUNCTION!\n"

    def __init__(self, value: Any):
        # Uložení hodnoty pro diagnostiku
        self.value = value

        # Vytvoření popisu problému
        what_happened = [
            f"   - Ověřovaný objekt neprošel kontrolou na coroutine function.\n",
            f"   - Ověřovaná objekt: {repr(self.value)}\n",
            f"   - Typ objekt: {type(self.value).__name__}\n",
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj, zda je objekt správně definován jako coroutine function.\n",
            "   - Například definované pomocí `async def`.\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)