from .._verify_error import VerifyError
from .._get_module_trace_info import get_module_trace_info


class VerifyUnexpectedInternalError(VerifyError):
    """Výjimka vyvolaná při nneočekávané události."""

    title = "\n⚠ DOŠLO K NEOČEKÁVANÉ INTERNÍ CHYBĚ!\n"

    def __init__(
        self,
        error_info: str,
        modul_info: str,
        original_exception: Exception,

    ):
        self.error_info = error_info
        self.modul_info = modul_info
        self.exc = original_exception

        what_happened = [
            f"   - {self.error_info}\n"
            f"   - {self.modul_info}\n"
            f"   - Zachycená výjimka: {type(self.exc).__name__} - {str(self.exc)}.\n"
        ]

        what_to_do = [
            "   - Tato situace by za běžných okolností neměla nastat a pravděpodobně značí chybu v kódu.\n",
            "   - Zkontroluj vývojářskou logiku nebo prosím nahlas chybu s podrobným popisem.\n",
        ]

        super().__init__(what_happened, what_to_do)


"""
Ukázkový zápis:
        except Exception as e:
            raise VerifyUnexpectedInternalError(
                info = f"Chyba nastala při generování zjednodušeného tracebacku.",
                modul = "Zachyceno v metodě __call__ třídy GetSimplifiedTraceback",
                original_exception = e
            ) from e
"""