from typing import Any

from ..._exceptions_base import VerifyParameterError


class VerifyAttributesNotIterableError(VerifyParameterError, TypeError):


    # Specifický nadpis pro chyby nesprávného typu parametru
    title = "\n⚠ PARAMETR PRO JMÉNO ATRIBUTU BYL ZADÁN V NEVALIDNÍM FORMÁTU!\n"

    def __init__(self, attribute_name: Any):

        # Uložení hodnoty pro diagnostiku
        self.attribute = attribute_name

        # Vytvoření popisu problému
        what_happened = [
            "   - Funkce pro získání atributu objektu obdržela nesprávně zadaný parametr pro jméno hledaného atributu\n",
            "   - Název atributu může být předán funkci pouze jako iterovatelný objekt s řetězci.\n",
            f"   - Zadaný atribut: {repr(self.attribute)}\n",
            f"   - Typ atributu: {type(attribute_name).__name__}\n",
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj definici parametru pro jméno hledaného atributu.\n",
            "   - Ujisti se, že je předán jako iterovatelný objelt s řetězci.\n",
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)