from ._verify_error import VerifyError


class VerifyInternalUnexpectedError(VerifyError):
    """Výjimka vyvolaná při nneočekávané události."""

    title = "\n⚠ PŘI OVĚŘOVÁNÍ DOŠLO K NEOČEKÁVANÉ INTERNÍ CHYBĚ!\n"

    def __init__(
        self,
        info: str,
        modul: str,
        original_exception: Exception
    ):
        self.info = info
        self.modul = modul
        self.exc = original_exception

        what_happened = [
            f"   - {self.info}.\n"
            f"   - {self.modul}.\n"
            "   - Tato situace by za běžných okolností neměla nastat a pravděpodobně značí chybu v kódu.\n",
        ]

        what_to_do = [
            "   - Zkontroluj vývojářskou logiku nebo prosím nahlas chybu s podrobným popisem..\n",
            f"   - Zachycená výjimka: {type(self.exc).__name__} - {str(self.exc)}.\n"
        ]

        super().__init__(what_happened, what_to_do)
