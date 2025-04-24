from .._bases import VerifyTypeError


class AnnotationDictArgsError(VerifyTypeError):
    """Výjimka vyvolaná při zjištění, že `get_args` pro slovníkovou anotaci nevrátil dvě hodnoty."""

    title = "\n⚠ NEPLATNÝ POČET TYPŮ VE SLOVNÍKOVÉ ANOTACI!\n"

    def __init__(self, inner_args):
        self.inner_args = inner_args

        what_happened = [
            "   - Funkce `get_args()` nevrátila dvě hodnoty pro klíč a hodnotu ve slovníku.\n",
            f"   - Získané hodnoty: {self.inner_args}\n",
            "   - Funkce `dictionary_validator` očekává anotaci ve formátu např. `dict[str, int]`.\n",
        ]

        what_to_do = [
            "   - Zkontroluj typovou anotaci, která byla předána jako parametr `annotation`.\n",
            "   - Ujisti se, že odpovídá formátu slovníku se dvěma typy: jeden pro klíče, druhý pro hodnoty.\n",
            "   - Pokud potřebuješ validovat např. `dict[str, Any]`, ujisti se, že anotace je správně zapsána.\n"
        ]

        super().__init__(what_happened, what_to_do)
