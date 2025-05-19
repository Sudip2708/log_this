from typing import Any, Tuple, Union

from .._exceptions_base import VerifyUnexpectedInternalError
from ._exceptions import (
    VerifyIsInstanceReturnedFalseError,
    VerifyTypeParameterError
)

"""
Ověřuje, zda hodnota odpovídá očekávanému typu nebo skupině typů.

Tato funkce nabízí vylepšenou verzi standardní funkce `isinstance()` s rozšířenou
diagnostikou chyb a možností kontrolovaného selhání. Slouží jako základní
stavební kámen pro komplexnější validační mechanismy v rámci knihovny
a zároveň jako samostatně použitelný nástroj pro vývojáře.

Klíčové koncepty:
-----------------
- **Rozšíření isinstance()**: Funkce obaluje standardní `isinstance()` a přidává
  podrobné chybové zprávy s návodem k řešení problémů.
- **Duální režim**: Může pracovat buď v režimu vyvolávání výjimek (výchozí)
  nebo v režimu vracení boolean hodnoty (při `bool_only=True`).
- **Hierarchie výjimek**: Používá specializované výjimky pro různé typy chyb,
  což usnadňuje jejich zachycení a zpracování.

Architekturální kontext:
-----------------------
Funkce `is_instance_verifier` je jednou z nejzákladnějších validačních
funkcí knihovny. Většina ostatních validátorů ji přímo či nepřímo využívá
pro ověření primitivních typů. Zároveň je sdíleným koncovým bodem validační
logiky, který zajišťuje konzistentní chování napříč celou knihovnou.

Parametry:
---------
value : Any
    Hodnota, která má být ověřena. Může být libovolného typu.

expected : Union[type, Tuple[type, ...]]
    Očekávaný typ nebo n-tice typů, kterým má hodnota odpovídat.
    Musí být platným typem (např. `str`, `int`) nebo n-ticí typů
    (např. `(str, int)`), stejně jako u standardní funkce `isinstance()`.

bool_only : bool, optional (default=False)
    Režim funkce:
    - False (výchozí): V případě neúspěšné validace vyvolá výjimku
      `VerifyIsInstanceValueError` s podrobným popisem problému.
    - True: V případě neúspěšné validace vrátí `False` místo vyvolání výjimky.

    Poznámka: Výjimka `VerifyIsInstanceParameterError` je vyvolána vždy,
    bez ohledu na hodnotu `bool_only`, pokud je parametr `expected`
    neplatného typu.

Návratové hodnoty:
----------------
bool
    - True: Pokud hodnota odpovídá očekávanému typu nebo jednomu z typů v n-tici.
    - False: Pouze v případě, že hodnota neodpovídá očekávanému typu a `bool_only=True`.

Výjimky:
-------
VerifyIsInstanceValueError
    Vyvolána, když hodnota neodpovídá očekávanému typu a `bool_only=False`.
    Obsahuje podrobné informace o:
    - Aktuální hodnotě a jejím typu
    - Očekávaném typu nebo typech
    - Pokynech k nápravě problému

VerifyIsInstanceExpectedError
    Vyvolána, když parametr `expected` není platným typem nebo n-ticí typů.
    Vyvolána vždy bez ohledu na hodnotu `bool_only`. Obsahuje informace o:
    - Předané neplatné hodnotě parametru
    - Očekávaném formátu parametru
    - Příkladech správného použití

VerifyUnexpectedInternalError
    Interní výjimka zachycující neočekávané chyby při validaci.
    Tato výjimka by za normálních okolností neměla být vyvolána.

Příklady použití:
---------------
Základní použití s výjimkou při neúspěchu:
'>>> is_instance_verifier("text", str)  # Vrátí True
'>>> is_instance_verifier(123, str)  # Vyvolá VerifyIsInstanceValueError

Použití s více typy:
'>>> is_instance_verifier(123, (str, int, float))  # Vrátí True
'>>> is_instance_verifier(None, (str, int))  # Vyvolá VerifyIsInstanceValueError

Režim pouze boolean hodnoty:
'>>> is_instance_verifier("text", str, bool_only=True)  # Vrátí True
'>>> is_instance_verifier(123, str, bool_only=True)  # Vrátí False bez výjimky

Neplatný parametr expected:
'>>> is_instance_verifier(123, "str")  # Vyvolá VerifyIsInstanceParameterError

Použití v bloku try-except:
'>>> try:
'>>>     is_instance_verifier(123, str)
'>>> except VerifyIsInstanceValueError as e:
'>>>     print(f"Hodnota má nesprávný typ: {e}")

Pokročilé koncepty:
------------------
Funkce implementuje vzor "fail fast", který okamžitě identifikuje a hlásí
problémy s typy, což zlepšuje detekci chyb a usnadňuje ladění. Současně
nabízí flexibilitu pro případy, kdy je vhodnější tichá kontrola bez vyvolání
výjimky.

Poznámky k rozšíření:
-------------------
Při rozšiřování této funkce je důležité zachovat její duální charakter
(výjimky vs. bool návratová hodnota) a udržet konzistentní formát
chybových zpráv. Pokud přidáváte podporu pro nové speciální případy,
zvažte, zda by nebylo vhodnější vytvořit specializovanou validační funkci
místo rozšiřování této základní funkce.

Viz také:
--------
typing_verifier: Hlavní validační funkce knihovny pro validaci hodnot
                proti typovým anotacím.
VerifyIsInstanceValueError: Výjimka vyvolaná při neshodě typů.
VerifyIsInstanceParameterError: Výjimka vyvolaná při neplatném parametru.

Výjimky které může vyvolat isinstance funkce:
    VerifyIsInstanceReturnedFalseError: Pokud validace selže (a bool_only=False). (VerifyValueError)
    VerifyTypeParameterError: Pokud je špatně zadán parametr `expected`. (VerifyParameterError)
    VerifyUnexpectedInternalError: Pro neočekávané chyby mimo knihovnu. (VerifyInternalError)
"""
def is_instance_verifier(
        value: Any,
        expected_type: Union[type, Tuple[type, ...]],
        bool_only: bool = False
) -> bool:
    """
    Ověřuje, zda hodnota odpovídá očekávanému typu nebo skupině typů.

    Tato funkce nabízí vylepšenou verzi standardní funkce `isinstance()` s rozšířenou
    diagnostikou chyb a možností kontrolovaného selhání. Slouží jako základní
    stavební kámen pro komplexnější validační mechanismy v rámci knihovny
    a zároveň jako samostatně použitelný nástroj pro vývojáře.

    Výjimky které může vyvolat is_instance_verifier funkce:
        VerifyIsInstanceReturnedFalseError: Pokud validace selže (a bool_only=False). (VerifyValueError, ValueError)
        VerifyTypeParameterError: Pokud je špatně zadán parametr `expected`. (VerifyParameterError, TypeError)
        VerifyUnexpectedInternalError: Pro neočekávané chyby mimo knihovnu. (VerifyInternalError, RuntimeError)
    """
    try:

        # Pokud hodnota odpovídá očekávanému typu, vrať True
        if isinstance(value, expected_type):
            return True

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise VerifyIsInstanceReturnedFalseError(value, expected_type)

    # Propagace vnitřní výjimky
    except VerifyIsInstanceReturnedFalseError:
        raise

    # Ošetření špatného zadání parametru `expected`
    except TypeError as e:
        raise VerifyTypeParameterError(expected_type) from e

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e


# Přejmenování funkce pro vnější výstup
verify_type = is_instance_verifier