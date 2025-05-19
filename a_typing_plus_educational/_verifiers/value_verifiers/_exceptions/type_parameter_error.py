from typing import Any

from ..._exceptions_base import VerifyParameterError


class VerifyTypeParameterError(VerifyParameterError, TypeError):
    """
    Výjimka vyvolaná při nesprávné specifikaci očekávaného typu v ověřovací funkci.

    Tato výjimka je vyvolána, když parametr `expected` předaný do funkce
    `is_instance_verifier()` není validním typem nebo n-ticí typů, což znemožňuje
    provedení ověření pomocí funkce `isinstance()`.

    Klíčové koncepty:
    -----------------
    * Validace vstupních parametrů - Kontrola správnosti specifikace ověřovacích kritérií
    * Typový systém Pythonu - Požadavky na parametry funkce `isinstance()`
    * Edukativní zpětná vazba - Vysvětlení správného způsobu specifikace typů

    Architekturální kontext:
    -----------------------
    Tato výjimka patří do kategorie chyb v použití API knihovny, nikoliv chyb
    v samotných validovaných hodnotách. Je vyvolána před samotným ověřením hodnoty,
    pokud je detekován problém s formátem parametru `expected`.

    Detaily implementace:
    --------------------
    * Uchovává referenci na problematickou hodnotu parametru `expected`
    * Poskytuje konkrétní pokyny a příklady správné specifikace typů
    * Upravuje výchozí nadpis pro zdůraznění charakteru chyby specifikace
    * Nabízí podrobné vysvětlení požadavků funkce `isinstance()`

    Povinné atributy:
    ----------------
    * expected (Any): Původní problematická hodnota parametru `expected`

    Příklady použití:
    ---------------
    ```python
    # Zachycení chyby specifikace typu
    try:
        is_instance_verifier(value, "string")  # Chyba: "string" není typ
    except IsInstanceExpectedError as e:
        print(f"Chyba specifikace typu: {e}")
        # Oprava problému
    ```

    Souvislosti s typovým systémem Pythonu:
    --------------------------------------
    Funkce `isinstance(obj, class_or_tuple)` vyžaduje, aby parametr `class_or_tuple`
    byl typem nebo n-ticí typů. Tato výjimka pomáhá identifikovat a opravit běžné chyby
    při specifikaci typů, jako je předání řetězce místo skutečného typu (např. `"str"`
    místo `str`).
    """

    # Specifický nadpis pro chyby specifikace typu
    title = "\n⚠ NEPLATNÁ SPECIFIKACE OČEKÁVANÉHO TYPU!\n"

    def __init__(self, expected_type: Any):
        """
        Inicializuje výjimku s informacemi o neplatné specifikaci typu.

        Vytváří detailní zprávu obsahující informace o problematickém parametru
        `expected` a nabízí pokyny, jak správně specifikovat typy pro ověření.

        Args:
            expected_type (Any): Neplatná hodnota parametru `expected`.

        Algoritmus:
        ----------
        1. Uložení reference na problematickou hodnotu parametru
        2. Vytvoření informativní zprávy s detaily o problému
        3. Sestavení praktických pokynů k nápravě s konkrétními příklady
        4. Inicializace nadřazené výjimky s formátovanou zprávou

        Poznámky:
        --------
        Tato výjimka nemůže být potlačena parametrem `bool_only`, protože
        indikuje fundamentální problém s použitím API, který musí být opraven.
        """
        # Uložení hodnoty pro diagnostiku
        self.expected = expected_type

        # Vytvoření popisu problému
        what_happened = [
            "   - Byl předán neplatný vstup pro ověření typu hodnoty",
            f"   - Předaná hodnota: {repr(self.expected)}\n",
            f"   - Typ hodnoty: {type(self.expected).__name__}\n",
            "   - Očekávaná hodnota: Definice typu, nebo tuple s více definicemi.\n"
        ]

        # Vytvoření pokynů k nápravě s konkrétními příklady
        what_to_do = [
            "   - Ujistěte se, že předáváte skutečný typ, nikoliv jeho textovou reprezentaci.\n",
            "   - Správně: is_instance_verifier(value, str)  # použití typu str\n",
            "   - Špatně: is_instance_verifier(value, 'str')  # použití řetězce 'str'\n",
            "   - Pro více typů použijte n-tici: (str, int, float)\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)



