from typing import Iterable, Tuple, Union
from collections.abc import Iterable as IterableOrigin


class VerifyToStrTupleValueNotStrError(VerifyValueError):

    # Specifický nadpis pro chyby nevolatelných hodnot
    title = "\n⚠ ZACHYCENA NEVALIDNÍ VSTUPNÍ HODNOTA PRO PŘEVOD NA TUPLE STRINGŮ!\n"

    def __init__(self, value: Any):
        # Uložení hodnoty pro diagnostiku
        self.value = value

        # Vytvoření popisu problému
        what_happened = [
            "   - Funkce pro převod řetězcového vstupu na tuple zachytila nevalidní parametr.\n",
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
            "   - Funkce očekává jako vstup řetězec a nebo iterovatelný seznam řetězců"
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj, hodnotu která je předávána.\n",
            "   - Ověřte, zda se jedná o řetězec a nebo iterovatelný objekt s řetězci.\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)


class VerifyToStrTupleIterableValueNotStrError(VerifyValueError):

    # Specifický nadpis pro chyby nevolatelných hodnot
    title = "\n⚠ ZACHYCEN OBJEKT OBSAHUJÍCÍ NEŘETĚZCOVÉ POLOŽKY"

    def __init__(self, value: Any):
        # Uložení hodnoty pro diagnostiku
        self.value = value

        # Vytvoření popisu problému
        what_happened = [
            "   - Funkce pro převod řetězcového vstupu na tuple zachytila nevalidní parametr.\n",
            "   - Zachyceno při kontrole vnitřních prvků iterovatelného obejktu, zda jsou řetězce"
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj, hodnotu která je předávána.\n",
            "   - Ověřte, že všechny vnitřní hodnoty iterovatelného objektu jsou řetězce.\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)


def to_str_tuple(
        value: Union[str, Iterable[str]],
        inner_check: bool = False
) -> Tuple[str, ...]:
    """
    Pomocná funkce která převede str vstup na tuple

    Funkce očekává jako vstup řetězec a nebo iterovatelný objekt s řetězci.
    Vrací tuple s řetězci.

    Jedná se o pomocnou funkci kteá není z venčí přístupná a není zde ošetřeno,
    při předání iterovatelného objektu, zda jeho vnitřní prvky jsou řetězce.
    Toto je z důvodu rychlejšího vyřízení, a také proto že se počítá s tím,
    že pokud by v iterovatelnému objektu naebyli řetězce odhalí to nadřazená funkce,
    takže zde to není potřeba kontrolovat.

    Funkce vyvolává výjimku jen v případě že vstup není str a nebo iterovatelný.
    """

    # Pokud je vstup předán jako řetězec
    if isinstance(value, str):
        return (value,)

    # Pokud je vstup předán jako iterovatelný objekt
    if isinstance(value, IterableOrigin):

        # Pokud není požadavek na kontrolu vnitřních hodnot
        if not inner_check:
            return tuple(value)

        # Pokud je zadán požadavek na kontrolu vnitřních hodnot
        else:

            # Pokud všechny hodnoty jsou str
            if all(isinstance(item, str) for item in value):
                return tuple(value)

            # Pokud nejsou všechny hodnoty str
            raise VerifyToStrTupleIterableValueNotStrError(value)

    # Ve všech ostatních případech
    raise VerifyToStrTupleValueNotStrError(value)
