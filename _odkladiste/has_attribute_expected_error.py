from typing import Any

from ._parameter_base import VerifyParameterError


class VerifyHasAttributeExpectedError(VerifyParameterError):
    """
    Výjimka vyvolaná při nesprávné specifikaci očekávaných atributů v ověřovací funkci.

    Tato výjimka je vyvolána, když parametr `expected_attributes` předaný do funkce
    `has_attribute_verifier()` není validním formátem pro specifikaci atributů
    (např. řetězec nebo iterovatelná kolekce řetězců). Tím je znemožněno
    správné provedení ověření přítomnosti atributů.

    Klíčové koncepty:
    -----------------
    * Validace vstupních parametrů - Kontrola správnosti definice očekávaných atributů
    * Očekávání struktury dat - Požadavky na formát specifikace atributů
    * Nápověda k správnému použití API - Poskytnutí informací o validních formátech

    Architekturální kontext:
    -----------------------
    Tato výjimka spadá do kategorie chyb souvisejících s nesprávným použitím
    API knihovny Verify. Vzniká před samotnou kontrolou objektu, když je zjištěn
    problém s formátem, v jakém byly očekávané atributy zadány.

    Detaily implementace:
    --------------------
    * Uchovává referenci na chybně zadanou hodnotu parametru `expected_attributes`
    * Obsahuje jasné instrukce a příklady, jak správně definovat očekávané atributy
    * Používá specifický nadpis, který upozorňuje na chybu ve specifikaci
    * Vysvětluje, jaké formáty jsou pro specifikaci atributů akceptovatelné

    Povinné atributy:
    ----------------
    * expected (Any): Původní, chybně zadaná hodnota parametru `expected_attributes`

    Příklady použití:
    ---------------
    ```python
    # Zachycení chyby při nesprávné specifikaci atributu
    try:
        # Předpokládejme, že existuje funkce has_attribute_verifier
        from your_module import has_attribute_verifier
        has_attribute_verifier(my_object, object)  # Chyba: 'object' není řetězec
    except HasAttributeExpectedError as e:
        print(f"Chyba specifikace atributu: {e}")
        # Náprava problému
    ```

    Souvislosti s ověřováním struktury objektů:
    -------------------------------------------
    Pro správné ověření, zda objekt obsahuje požadované atributy, je nutné
    poskytnout názvy těchto atributů ve správném formátu (řetězec pro jeden
    atribut, iterovatelná kolekce řetězců pro více atributů). Tato výjimka
    pomáhá uživatelům knihovny vyhnout se běžným chybám při této specifikaci.
    """

    # Specifický nadpis pro chyby specifikace očekávaných atributů
    title = "\n⚠ CHYBNÁ SPECIFIKACE OČEKÁVANÝCH ATRIBUTŮ!\n"

    def __init__(self, expected_attribute: Any):
        """
        Inicializuje výjimku s informacemi o chybné specifikaci očekávaných atributů.

        Vytváří podrobnou zprávu, která popisuje chybně zadaný parametr
        `expected_attributes` a poskytuje návod, jak správně specifikovat
        očekávané atributy pro ověření.

        Args:
            expected_attribute (Any): Neplatná hodnota parametru `expected_attributes`.

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
        pro funkčnost ověřování přítomnosti atributů.
        """
        # Uložení hodnoty pro diagnostiku
        self.expected = expected_attribute

        # Vytvoření popisu problému
        what_happened = [
            "   - Byl předán neplatný vstup pro ověření přítomnosti atributů.\n",
            f"   - Předaná hodnota: {repr(self.expected)}\n",
            f"   - Typ hodnoty: {type(self.expected).__name__}\n",
            "   - Očekávaná hodnota: Řetězec s názvem atributu, nebo iterovatelný kontejner těchto řetězců.\n"

        ]

        # Vytvoření pokynů k nápravě s konkrétními příklady
        what_to_do = [
            "   - Ujistěte se, že předáváte atributy v povoleném formátu.\n",
            "   - Správně: has_attribute_verifier(value, 'attribute_name')  # použití řetězce\n",
            "   - Špatně: has_attribute_verifier(value, attribute_name)  # zapomenutí apostrofů\n",
            "   - Pro více atributů použijte iterovatelný kontejner (tuple, list, set): ('attr1', 'attr2')\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)