from typing import Any

from ..._exceptions_base import VerifyValueError


class VerifyAttributeNotFoundError(VerifyValueError, AttributeError):

    # Specifický nadpis pro chyby nenalezených atributů
    title = "\n⚠ OBJEKT NEOBSAHUJE POŽADOVANÝ ATRIBUT!\n"

    def __init__(self, obj: Any, attribute_name: str):

        # Uložení hodnoty pro diagnostiku
        self.obj = obj
        self.attribute = attribute_name

        # Vytvoření popisu problému
        what_happened = [
            f"   - Funkce pro získání atributu objektu zjistila, že objekt neobsahuje požadovaný atribut.\n",
            f"   - Objekt: {repr(self.obj)}\n",
            f"   - Typ objektu: {type(self.obj).__name__}\n",
            f"   - Požadovaný atribut: {repr(self.attribute)}\n",
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj objekt a ověř, zda má mít požadovaný atribut.\n",
            "   - Pro zjištění všech atributů objektu můžeš použít: print(dir(your_object)).\n",
            "   - Pokud nechceš na tento objekt dostávat tuto výjimku, "
            "můžeš nastavit hodnotu, která se má vracet v případě nenalezení atributu, "
            "jakožto třetí parametr funkce get_attr_safe().\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)