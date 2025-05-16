from typing import Any

from ..._exceptions_base import VerifyValueError


class VerifyInnerCheckError(VerifyValueError):
    """
    Výjimka vyvolaná při chybě během vykonávání ověření vnitřních prvků.
    """

    title = "\n⚠ CHYBA OVĚŘENÍ VNITŘNÍCH PRVKŮ HODNOTY\n"

    def __init__(
            self,
            value: Any,
            annotation: Any,
            original_exception: Exception,
    ):
        self.value = value
        self.annotation = annotation
        self.original_exception = original_exception

        what_happened = [
            "   - Ověření základního typu hodnoty proběhlo v pořádku, ale během ověření ověření vnitřních prvků došlo k vyvolání výjimky.\n",
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Předaná anotace definující hodnotu: {repr(self.annotation)}\n",
            f"   - Název zachycené výjimky: \n{getattr(self.original_exception, 'title', str(type(self.original_exception).__name__))}\n"
            f"   - Popis výjimky: \n{getattr(self.original_exception, 'what_happened', str(self.original_exception))}\n"
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj hodnotu a předanou anotaci zda jsou správně definované a odpovídají očekávání.\n",
            "   - Níže je uveden popis nápravy převzatý ze zachycené výjimky:\n",
            f"\n{getattr(self.original_exception, 'what_to_do', '   - (Zachycená výjimka nemá definovanou nápovědu).')}\n",
        ]

        super().__init__(what_happened, what_to_do, self.title)

