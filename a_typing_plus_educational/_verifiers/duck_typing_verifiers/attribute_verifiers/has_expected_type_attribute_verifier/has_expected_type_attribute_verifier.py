from typing import Any, Iterable, Type, Union
from collections.abc import Iterable as IterableOrigin

from .._exceptions import VerifyAttributeParameterError
from .has_expected_type_attr_verifier import has_expected_type_attr_verifier
from .has_expected_type_attrs_verifier import has_expected_type_attrs_verifier


def has_expected_type_attribute_verifier(
    obj: Any,
    attribute: Union[str, Iterable[str]],
    expected_type: Type,
    bool_only: bool = False
) -> bool:
    """
    Ověřuje, zda objekt obsahuje očekávaný atribut nebo skupinu atributů.

    Tato funkce nabízí vylepšenou verzi standardní funkce `hasattr()` s rozšířenou
    diagnostikou chyb a možností kontrolovaného selhání. Slouží jako základní
    validační nástroj pro ověření existence atributů objektů a je využívána jak
    interně v rámci validační knihovny, tak samostatně pro specifické validace.

    Klíčové koncepty:
    -----------------
    - **Rozšíření hasattr()**: Funkce obaluje standardní `hasattr()` a přidává
      podrobné chybové zprávy pro snadnější identifikaci problémů.
    - **Kontrola více atributů**: Na rozdíl od standardní funkce `hasattr()` umožňuje
      jedním voláním ověřit existenci více atributů najednou.
    - **Duální režim**: Může pracovat buď v režimu vyvolávání výjimek (výchozí)
      nebo v režimu vracení boolean hodnoty (při `bool_only=True`).
    - **Hierarchie výjimek**: Používá specializované výjimky pro různé typy chyb,
      což usnadňuje jejich zachycení a zpracování.

    Architekturální kontext:
    -----------------------
    Funkce `has_attribute_verifier` je jednou ze základních validačních funkcí
    knihovny, která se zaměřuje na ověřování struktury objektů. Je často využívána
    při validaci složitějších typů a protokolů, kde je potřeba ověřit přítomnost
    určitých metod nebo vlastností. V hierarchii validačních funkcí slouží jako
    specializovaný validátor pro strukturální kontroly.

    Parametry:
    ---------
    obj : Any
        Objekt, u kterého má být ověřena existence atributu nebo atributů.
        Může být libovolného typu.

    attribute_name : Union[str, Iterable[str]]
        Očekávaný atribut nebo kolekce atributů, které má objekt obsahovat.
        Může být buď řetězec pro jeden atribut (např. "__len__") nebo
        iterovatelná kolekce řetězců pro více atributů (např. ["__len__", "__iter__"]).

    bool_only : bool, optional (default=False)
        Režim funkce:
        - False (výchozí): V případě neúspěšné validace vyvolá výjimku
          `VerifyHasAttributeValueError` s podrobným popisem problému.
        - True: V případě neúspěšné validace vrátí `False` místo vyvolání výjimky.

        Poznámka: Výjimka `VerifyHasAttributeExpectedError` je vyvolána vždy,
        bez ohledu na hodnotu `bool_only`, pokud je parametr `attribute_name`
        neplatného typu.

    Návratové hodnoty:
    ----------------
    bool
        - True: Pokud objekt obsahuje všechny očekávané atributy.
        - False: Pouze v případě, že objekt neobsahuje některý z očekávaných
          atributů a `bool_only=True`.

    Výjimky:
    -------
    VerifyHasAttributeValueError
        Vyvolána, když objekt neobsahuje některý z očekávaných atributů
        a `bool_only=False`. Obsahuje podrobné informace o:
        - Objektu a jeho typu
        - Chybějících atributech
        - Dostupných atributech objektu pro snadnější diagnózu problému

    VerifyHasAttributeExpectedError
        Vyvolána, když parametr `attribute_name` není platným řetězcem
        nebo iterovatelnou kolekcí řetězců. Vyvolána vždy bez ohledu na hodnotu
        `bool_only`. Obsahuje informace o:
        - Předané neplatné hodnotě parametru
        - Očekávaném formátu parametru
        - Příkladech správného použití

    VerifyUnexpectedInternalError
        Interní výjimka zachycující neočekávané chyby při validaci.
        Tato výjimka by za normálních okolností neměla být vyvolána.

    Příklady použití:
    ---------------
    Základní použití s jedním atributem:
    '>>> class TestObj:
    '...     x = 10
    '>>> obj = TestObj()
    '>>> has_attribute_verifier(obj, "x")  # Vrátí True
    '>>> has_attribute_verifier(obj, "y")  # Vyvolá VerifyHasAttributeValueError

    Použití s více atributy:
    '>>> class TestObj:
    '...     x = 10
    '...     y = 20
    '>>> obj = TestObj()
    '>>> has_attribute_verifier(obj, ["x", "y"])  # Vrátí True
    '>>> has_attribute_verifier(obj, ["x", "z"])  # Vyvolá VerifyHasAttributeValueError

    Režim pouze boolean hodnoty:
    '>>> has_attribute_verifier(obj, "x", bool_only=True)  # Vrátí True
    '>>> has_attribute_verifier(obj, "z", bool_only=True)  # Vrátí False bez výjimky

    Neplatný parametr attribute_name:
    '>>> has_attribute_verifier(obj, 123)  # Vyvolá VerifyHasAttributeExpectedError

    Použití v bloku try-except:
    '>>> try:
    '...     has_attribute_verifier(obj, ["x", "z"])
    '... except VerifyHasAttributeValueError as e:
    '...     print(f"Objekt nemá požadované atributy: {e}")

    Pokročilé koncepty:
    ------------------
    Funkce implementuje přístup "all-or-nothing", což znamená, že vrací True
    pouze pokud objekt obsahuje všechny specifikované atributy. To je užitečné
    pro implementaci validace proti protokolům nebo abstraktním typům, kde je
    potřeba ověřit, že objekt má všechny potřebné metody nebo vlastnosti.

    Poznámky k rozšíření:
    -------------------
    Při rozšiřování této funkce zvažte, zda by nebylo užitečné přidat podporu pro
    podmíněné ověření atributů (např. "alespoň jeden z uvedených atributů")
    nebo hlubší kontrolu hodnot atributů. Je důležité zachovat konzistenci s ostatními
    validačními funkcemi, zejména v oblasti formátu chybových zpráv a chování
    parametru `bool_only`.

    Viz také:
    --------
    typing_verifier: Hlavní validační funkce knihovny pro validaci hodnot
                    proti typovým anotacím.
    is_instance_verifier: Základní validátor pro ověření typu hodnoty.
    VerifyHasAttributeValueError: Výjimka vyvolaná při chybějícím atributu.
    VerifyHasAttributeExpectedError: Výjimka vyvolaná při neplatném parametru.
    """

    # Vyřízení pro jednu položku
    if isinstance(attribute, str):
        return has_expected_type_attr_verifier(
            obj, attribute, expected_type, bool_only
        )

    # Vyřízení pro více položek
    if isinstance(attribute, IterableOrigin):
        return has_expected_type_attrs_verifier(
            obj, attribute, expected_type, bool_only
        )

    # Výjimka pro nevalidní vstup
    raise VerifyAttributeParameterError(attribute)



