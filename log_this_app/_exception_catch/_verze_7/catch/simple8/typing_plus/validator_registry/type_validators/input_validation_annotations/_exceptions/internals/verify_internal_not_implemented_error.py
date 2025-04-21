from typing import List
from ._verify_error import VerifyError


class VerifyInternalNotImplementedError(VerifyError):
    """Výjimka vyvolaná pokud potomek neobsahuje povinný atribut definovaný v předku."""

    title = "\n⚠ ZJIŠTĚN CHYBĚJÍCÍ POVINÝ ATRIBUT!\n"

    def __init__(
        self,
        class_name: str,
        missing: List[str]
    ):
        self.class_name = class_name
        self.missing = ', '.join(missing)

        what_happened = [
            f"   - Třída: {self.class_name}, nemá implementované následující atributy: {self.missing}.\n"
            f"   - Tyto atributy jsou vyžadovány v ABC definici BaseValidator.\n"
        ]

        what_to_do = [
            "   - Zkontroluj Definici dané třídy a doplňte požadované atributy.\n",
        ]

        super().__init__(what_happened, what_to_do)
