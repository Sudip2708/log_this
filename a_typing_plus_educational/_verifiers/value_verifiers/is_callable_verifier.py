from typing import Any

from .._exceptions_base import VerifyUnexpectedInternalError
from ._exceptions import VerifyNotCallableError

"""
Ověřuje, zda je hodnota volatelná (callable).

Tato funkce nabízí vylepšenou verzi standardní funkce `callable()` s rozšířenou
diagnostikou chyb a možností kontrolovaného selhání. Slouží jako jeden z koncových
validátorů pro ověření volatelnosti objektů v rámci typové validace knihovny
a zároveň jako samostatně použitelný nástroj pro vývojáře.

Klíčové koncepty:
-----------------
- **Rozšíření callable()**: Funkce obaluje standardní `callable()` a přidává
  podrobné chybové zprávy s informacemi o problému volatelnosti.
- **Duální režim**: Může pracovat buď v režimu vyvolávání výjimek (výchozí)
  nebo v režimu vracení boolean hodnoty (při `bool_only=True`).
- **Hierarchie výjimek**: Používá specializované výjimky pro různé typy chyb,
  což usnadňuje jejich zachycení a zpracování.

Architekturální kontext:
-----------------------
Funkce `callable_verifier` je jednou z koncových validačních funkcí knihovny
používanou pro ověření volatelnosti objektů. Je využívána hlavní funkcí
`typing_verifier` při validaci callables a function typů. Zajišťuje konzistentní
chování a detailní zpětnou vazbu při validaci volatelných objektů napříč celou
knihovnou.

Parametry:
---------
obj : Any
    Hodnota, která má být ověřena na volatelnost. Může být libovolného typu.
    Volatelné objekty zahrnují funkce, metody, třídy a objekty s implementovanou
    metodou `__call__`.

bool_only : bool, optional (default=False)
    Režim funkce:
    - False (výchozí): V případě neúspěšné validace vyvolá výjimku
      `VerifyCallableValueError` s podrobným popisem problému.
    - True: V případě neúspěšné validace vrátí `False` místo vyvolání výjimky.

Návratové hodnoty:
----------------
bool
    - True: Pokud je hodnota volatelná (implementuje protokol volání).
    - False: Pouze v případě, že hodnota není volatelná a `bool_only=True`.

Výjimky:
-------
VerifyCallableValueError
    Vyvolána, když hodnota není volatelná a `bool_only=False`.
    Obsahuje podrobné informace o:
    - Aktuální hodnotě a jejím typu
    - Očekávaném chování (volatelnost)
    - Pokynech k nápravě problému

VerifyUnexpectedInternalError
    Interní výjimka zachycující neočekávané chyby při validaci.
    Tato výjimka by za normálních okolností neměla být vyvolána.

Příklady použití:
---------------
Základní použití s výjimkou při neúspěchu:
'>>> callable_verifier(print)  # Vrátí True pro funkci
'>>> callable_verifier(lambda x: x)  # Vrátí True pro lambda
'>>> callable_verifier(str)  # Vrátí True pro třídu (konstruktor)
'>>> callable_verifier("text")  # Vyvolá VerifyCallableValueError

Režim pouze boolean hodnoty:
'>>> callable_verifier(print, bool_only=True)  # Vrátí True
'>>> callable_verifier("text", bool_only=True)  # Vrátí False bez výjimky

Použití s objekty implementujícími __call__:
'>>> class Callable:
'...     def __call__(self):
'...         return "Jsem volatelný"
'>>> obj = Callable()
'>>> callable_verifier(obj)  # Vrátí True

Použití v bloku try-except:
'>>> try:
'...     callable_verifier(123)
'... except VerifyCallableValueError as e:
'...     print(f"Hodnota není volatelná: {e}")

Pokročilé koncepty:
------------------
Funkce implementuje vzor "fail fast", který okamžitě identifikuje a hlásí
problémy s volatelností objektů, což zlepšuje detekci chyb a usnadňuje ladění.
Na rozdíl od standardní funkce `callable()` poskytuje podrobné diagnostické
informace o nevolatelných objektech a jejich typech.

Poznámky k rozšíření:
-------------------
Při rozšiřování této funkce je důležité zachovat její duální charakter
(výjimky vs. bool návratová hodnota) a udržet konzistentní formát
chybových zpráv. Pro speciální případy validace volatelných objektů
(např. ověření signatury funkce) zvažte vytvoření specializované
validační funkce namísto rozšiřování této základní funkce.

Viz také:
--------
typing_verifier: Hlavní validační funkce knihovny pro validaci hodnot
                proti typovým anotacím.
is_instance_verifier: Základní validační funkce pro ověření typu objektu.
VerifyCallableValueError: Výjimka vyvolaná když hodnota není volatelná.
"""
def is_callable_verifier(
        obj: Any,
        bool_only: bool = False
) -> bool:
    """
    Ověřuje, zda je hodnota volatelná (callable).

    Tato funkce nabízí vylepšenou verzi standardní funkce `callable()` s rozšířenou
    diagnostikou chyb a možností kontrolovaného selhání. Slouží jako jeden z koncových
    validátorů pro ověření volatelnosti objektů v rámci typové validace knihovny
    a zároveň jako samostatně použitelný nástroj pro vývojáře.

    Výjimky které může vyvolat is_callable_verifier funkce:
        VerifyNotCallableError: Pokud validace selže (a bool_only=False). (VerifyValueError, ValueError)
        VerifyUnexpectedInternalError: Pro neočekávané chyby mimo knihovnu. (VerifyInternalError, RuntimeError)
    """
    try:

        # Pokud je objekt volatelná, vrať True
        if callable(obj):
            return True

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise VerifyNotCallableError(obj)

    # Propagace vnitřní výjimky
    except VerifyNotCallableError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e


# Přejmenování funkce pro vnější výstup
verify_callable = is_callable_verifier