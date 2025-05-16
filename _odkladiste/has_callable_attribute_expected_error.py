from typing import Any

from ._parameter_base import VerifyParameterError


class VerifyHasCallableAttributeExpectedError(VerifyParameterError):
    """
    Výjimka vyvolaná při neplatné specifikaci očekávaných atributů pro ověření volatelnosti.

    Tato výjimka je vyvolána, když parametr `expected_attribute` předaný do funkce
    `callable_attribute_verifier()` nemá očekávaný formát. Očekává se, že tento
    parametr bude buď řetězec s názvem jednoho atributu, nebo iterovatelná kolekce
    řetězců obsahujících názvy atributů, které by měly být volatelné.

    Klíčové koncepty:
    -----------------
    * Validace vstupních parametrů - Kontrola správnosti formátu očekávaných atributů
    * Očekávání struktury dat - Požadavky na typ a formát parametru `expected_attribute`
    * Nápověda k správnému použití API - Poskytnutí informací o validních formátech specifikace atributů

    Architekturální kontext:
    -----------------------
    Tato výjimka spadá do kategorie chyb souvisejících s nesprávným použitím
    API knihovny Verify. Vzniká na začátku procesu ověřování, když je zjištěno,
    že způsob, jakým byly specifikovány očekávané atributy, je neplatný.

    Detaily implementace:
    --------------------
    * Uchovává referenci na chybně zadanou hodnotu parametru `expected_attribute`
    * Obsahuje jasné instrukce a příklady, jak správně definovat očekávané atributy
    * Používá specifický nadpis, který upozorňuje na chybu ve specifikaci atributů
    * Vysvětluje, jaké formáty jsou pro specifikaci atributů akceptovatelné (řetězec nebo iterovatelná kolekce řetězců)

    Povinné atributy:
    ----------------
    * expected (Any): Původní, chybně zadaná hodnota parametru `expected_attribute`

    Příklady použití:
    ---------------
    ```python
    class MyObject:
        def method(self):
            pass

    obj = MyObject()

    try:
        # Předpokládejme, že existuje funkce callable_attribute_verifier
        from your_module import callable_attribute_verifier
        callable_attribute_verifier(obj, obj.method)  # Chyba: Předán objekt metody místo názvu atributu
    except VerifyHasCallableAttributeExpectedError as e:
        print(f"Chyba specifikace atributu: {e}")
        # Náprava problému
    ```

    Souvislosti s ověřováním volatelných atributů:
    ---------------------------------------------
    Pro správné ověření, zda objekt obsahuje atributy, které jsou volatelné,
    je nutné poskytnout názvy těchto atributů ve správném formátu. Tato výjimka
    pomáhá uživatelům knihovny vyhnout se běžným chybám při této specifikaci,
    jako je například předání samotného objektu atributu místo jeho názvu.
    """

    # Specifický nadpis pro chyby specifikace očekávaných atributů
    title = "\n⚠ CHYBNÁ SPECIFIKACE OČEKÁVANÝCH ATRIBUTŮ!\n"

    def __init__(self, expected_attribute: Any):
        """
        Inicializuje výjimku s informacemi o chybné specifikaci očekávaných atributů
        pro ověření volatelnosti.

        Vytváří podrobnou zprávu, která popisuje chybně zadaný parametr
        `expected_attribute` a poskytuje návod, jak správně specifikovat
        očekávané atributy (jako řetězce nebo iterovatelnou kolekci řetězců).

        Args:
            expected_attribute (Any): Neplatná hodnota parametru `expected_attribute`.

        Algoritmus:
        ----------
        1. Uložení reference na chybně zadanou hodnotu parametru.
        2. Vytvoření informativní zprávy s detaily o zjištěném problému.
        3. Poskytnutí jasných pokynů k nápravě, včetně správných a špatných příkladů.
        4. Inicializace nadřazené výjimky s vytvořenou zprávou.

        Poznámky:
        --------
        Tato výjimka indikuje problém s použitím API, který vyžaduje zásah
        na straně volajícího kódu. Správná specifikace atributů je klíčová
        pro funkčnost ověřování přítomnosti a volatelnosti atributů.
        """
        # Uložení hodnoty pro diagnostiku
        self.expected = expected_attribute

        # Vytvoření popisu problému
        what_happened = [
            "   - Byl předán neplatný vstup definující atributy pro ověření volatelnosti atributů.\n",
            f"   - Předaná hodnota: {repr(self.expected)}\n",
            f"   - Typ hodnoty: {type(self.expected).__name__}\n",
            "   - Očekávaná hodnota: Řetězec s názvem atributu, nebo iterovatelný kontejner těchto řetězců.\n"

        ]

        # Vytvoření pokynů k nápravě s konkrétními příklady
        what_to_do = [
            "   - Ujistěte se, že předáváte atributy v povoleném formátu.\n",
            "   - Správně: callable_attribute_verifier(value, 'attribute_name')  # použití řetězce\n",
            "   - Špatně: callable_attribute_verifier(value, attribute_name)  # zapomenutí apostrofů\n",
            "   - Pro více atributů použijte iterovatelný kontejner (tuple, list, set): ('attr1', 'attr2')\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)