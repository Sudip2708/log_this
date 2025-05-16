from .._bases import VerifyTypeError


class AnnotationGetArgsError(VerifyTypeError):
    """Výjimka vyvolaná při neúspěšném získání vnitřních typů z anotace pomocí `get_args`."""

    title = "\n⚠ ZACHYCENA CHYBA PŘI ZÍSKÁVÁNÍ TYPŮ Z ANOTACE!\n"

    def __init__(self, annotation):
        self.annotation = annotation

        what_happened = [
            f"   - Nepodařilo se získat vnitřní typy z anotace pomocí `get_args()`.\n"
            f"   - Zadaná anotace: {self.annotation}\n",
            f"   - Pravděpodobně nebyl předán platný typový náznak (např. List[int], tuple[str, int] atd.).\n",
        ]

        what_to_do = [
            "   - Zkontroluj parametr 'annotation', který byl předán funkci.\n",
            "   - Ujisti se, že jde o typovou anotaci kompatibilní s `typing.get_args()`.\n",
            "   - Pokud anotace není zadána nebo je běžný typ (např. int, str), je možné tuto část přeskočit.\n"
        ]

        super().__init__(what_happened, what_to_do)
