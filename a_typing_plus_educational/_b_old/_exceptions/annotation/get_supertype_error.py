from .._bases import VerifyTypeError
from .._tools import format_expected


class AnnotationGetSuperTypeError(VerifyTypeError):
    """Výjimka vyvolaná při neúspěšném získání __supertype__ atributu z NewType anotace."""

    title = "\n⚠ NELZE ZÍSKAT NADŘAZENÝ TYP Z NEWTYPE!\n"

    def __init__(self, annotation):
        self.annotation = annotation

        what_happened = [
            f"   - Pokus o získání nadřazeného typu z NewType anotace selhal.\n"
            f"   - Problematická anotace: {format_expected(self.annotation)}\n",
            f"   - Anotace buď není typu NewType, nebo nemá atribut __supertype__.\n",
        ]

        what_to_do = [
            "   - Zkontrolujte, zda anotace je skutečně NewType vytvořený pomocí typing.NewType().\n",
            "   - Ujistěte se, že pracujete s platnou instancí NewType, ne s typem samotným.\n"
        ]

        super().__init__(what_happened, what_to_do)