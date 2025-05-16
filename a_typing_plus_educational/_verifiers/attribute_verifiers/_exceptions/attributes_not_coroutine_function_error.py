from typing import Any, Dict, Iterable

from ..._exceptions_base import VerifyValueError


class VerifyAttributesNotCoroutineFunctionError(VerifyValueError, AttributeError):

    # Specifický nadpis pro chyby nenalezených atributů
    title = "\n⚠ OBJEKT NEPROŠEL KONTROLOU COROUTINE FUNCTION ATRIBUTŮ!\n"

    def __init__(
            self,
            obj: Any,
            attribute_names: Iterable[str],
            outcome: Dict[str, Any]
    ):

        # Uložení hodnoty pro diagnostiku
        self.obj = obj
        self.attribute_names = list(attribute_names)
        self.not_coroutine_function = outcome["errors"]["not_coroutine_function"]
        self.not_str = outcome["errors"]["not_str"]
        self.absent = outcome["errors"]["absent"]
        self.not_access = outcome["errors"]["not_access"]
        self.success = set(attribute_names) - set(self.not_str + self.absent + self.not_access)


        # Vytvoření popisu problému
        what_happened = [
            "   - Funkce pro ověření zda jsou atributy objektu coroutine function zychytila chybu.\n",
            f"   - Objekt: {repr(self.obj)}\n",
            f"   - Ověřované atributy: {self._format_items(self.attribute_names)}\n",
            f"   - Úspěšně ověřené atributy: {self._format_items(self.success) if self.success else 'n/a'}\n",
            "   - Neúspěšně ověřené atributy:\n"
        ]

        # Přidání řádku pro nevolatelné atributy (jsou-li)
        if self.not_coroutine_function:
            what_happened.append(
                f"   - Atributy které neprošli kontrolou na coroutine function: {self._format_items(self.absent)}\n",
            )

        # Přidání řádku pro chybějící atributy (jsou-li)
        if self.absent:
            what_happened.append(
                f"   - Atributy které na objektu chybí: {self._format_items(self.absent)}\n",
            )

        # Přidání řádku atributy s odepřeným přístupem (jsou-li)
        if self.not_access:
            what_happened.append(
                f"   - Atributy ke kterým není přístup: {self._format_items(self.not_access)}\n",
            )

        # Přidání řádku pro chybně zadaného parametru jména atributů - nejsou řetězce (jsou-li)
        if self.not_str:
            what_happened.append(
                f"   - Atributy které nebylo možné ověřit: {self._format_items(self.not_str)}\n",
            )

        # Vytvoření pokynů k nápravě
        what_to_do = ["   - Zkontroluj definici objektu, který předáváš k ověření.\n",]

        # Přidání řádku pro chybějící atributy (jsou-li)
        if self.not_coroutine_function:
            what_to_do.append(
                "   - Zkontroluj, zda je objekt správně definován jako coroutine function.\n"
                "   - Například definované pomocí `async def`.\n",
            )

        # Přidání řádku pro chybějící atributy (jsou-li)
        if self.absent:
            what_to_do.append(
                "   - Zkontroluj zda objekt má obsahovat požadované atributy.\n",
            )

        # Přidání řádku atributy s odepřeným přístupem (jsou-li)
        if self.not_access:
            what_to_do.append(
                f"   - Zkontroluj objekt a ověř, zda nemá omezený nebo přepsaný přístup k atributům.\n",
            )

        # Přidání řádku pro chybně zadaného parametru jména atributů - nejsou řetězce (jsou-li)
        if self.not_str:
            what_to_do.append(
                f"   - Pokud některá jména atributů nebyla zadána jako řetězce, oprav zadání jmen parametrů\n",
            )

        # Přidání závěrečného řádku
        what_to_do.append(
            "   - Pro zjištění všech atributů objektu můžeš použít: print(dir(your_object)).\n",

        )

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)