from typing import Any, Optional, Union

from .base_validator import BaseValidator
from .._verifiers import iterable_item_verifier

class BaseIterableItemValidator(BaseValidator):
    """
    Základní třída pro validátory iterovatelných kolekcí s validací vnitřních prvků.

    BaseIterableItemValidator poskytuje implementaci pro validaci generických kontejnerových
    typů, jako jsou List[T], Set[T], Tuple[T, ...], a další struktury, které obsahují prvky
    jednoho specifikovaného typu. Tato třída zajišťuje dvouúrovňovou validaci - nejprve
    ověří, že hodnota je instancí očekávaného kontejnerového typu, a následně validuje
    každý jednotlivý prvek uvnitř kontejneru proti definovanému vnitřnímu typu.

    Klíčové koncepty:
    ================

    1. Generické typy a typové parametry
       Tato třída pracuje s generickými typy, které jsou v Pythonu reprezentovány
       prostřednictvím modulu typing. Generické typy jako List[int], Set[str], apod.
       obsahují dodatečné informace o očekávaném typu prvků uvnitř kontejneru.
       Tyto informace jsou extrahovány a využity pro validaci jednotlivých prvků.

    2. Rekurzivní typová validace
       Validace prvků uvnitř kontejneru je prováděna rekurzivně, což umožňuje zpracovat
       i vnořené struktury (např. List[List[int]]). Toto rekurzivní volání validace
       respektuje nastavený limit hloubky (parametr depth_check), aby se předešlo
       potenciálním nekonečným smyčkám při validaci cyklických datových struktur.

    3. Kontrola hloubky validace
       Parametr depth_check řídí, jak hluboko v hierarchii vnořených struktur má
       validace pokračovat. Může být nastaven jako boolean hodnota (True/False) nebo
       jako konkrétní číselná hodnota určující maximální hloubku validace.

    4. Delegování validace
       Podobně jako u BaseIsInstanceValidator, i tato třída deleguje vlastní validační
       logiku na specializovanou funkci (iterable_item_verifier), což zajišťuje
       oddělení zodpovědností a umožňuje znovupoužití validační logiky.

    Architekturální kontext:
    ======================

    V hierarchii validátorů představuje BaseIterableItemValidator druhý stupeň
    složitosti validace. Zatímco BaseIsInstanceValidator pracuje pouze s přímou
    kontrolou typu, tato třída přidává validaci vnitřních prvků kontejneru.

    Validátory odvozené od této třídy typicky:
    1. Nastavují atribut ORIGIN na požadovaný kontejnerový typ (list, set, tuple, atd.)
    2. Definují VALIDATOR_KEY a ANNOTATION pro příslušný typ z modulu typing (List, Set, Tuple, atd.)
    3. Ve většině případů nemusí přepisovat metodu __call__, protože zdědí její
       implementaci z této třídy

    Mezi běžné validátory odvozené od této třídy patří ListValidator, SetValidator,
    TupleValidator (pro homogenní n-tice), FrozenSetValidator a další validátory
    pro kontejnerové typy.

    Použití pro odvozené třídy:
    =========================

    Příklad definice validátoru pro typ List:

    ```python
    class ListValidator(BaseIterableItemValidator):
        VALIDATOR_KEY = "list"
        ANNOTATION = List
        ORIGIN = list
        DESCRIPTION = "Seznam prvků"
        LONG_DESCRIPTION = "Validuje, že objekt je seznam (list) s prvky odpovídajícími specifikovanému typu."
    ```

    Příklad definice validátoru pro typ Set:

    ```python
    class SetValidator(BaseIterableItemValidator):
        VALIDATOR_KEY = "set"
        ANNOTATION = Set
        ORIGIN = set
        DESCRIPTION = "Množina prvků"
        LONG_DESCRIPTION = "Validuje, že objekt je množina (set) s prvky odpovídajícími specifikovanému typu."
    ```

    Detaily implementace:
    ===================

    Validace iterovatelných struktur probíhá ve dvou krocích:

    1. Prvotní validace typu kontejneru:
       Nejprve se ověří, zda je hodnota instancí očekávaného kontejnerového typu
       (definovaného v atributu ORIGIN) pomocí is_instance_verifier.

    2. Validace vnitřních prvků:
       Pokud je požadována validace vnitřních prvků (depth_check není False),
       extrahují se informace o očekávaném typu prvků z typové anotace, a následně
       se každý prvek v kontejneru validuje proti tomuto typu.

    Chybové stavy:
    ============

    Při validaci iterovatelných struktur mohou nastat následující chybové stavy:

    1. Hodnota není instancí očekávaného kontejnerového typu
       (např. pokud je očekáván seznam, ale hodnota je slovník)

    2. Některý z prvků uvnitř kontejneru neodpovídá očekávanému vnitřnímu typu
       (např. v List[int] se nachází řetězec)

    3. Problém při extrakci typových parametrů z anotace
       (nevalidní nebo neúplná typová anotace)

    V případě chyby validace je generována příslušná výjimka s podrobným popisem problému,
    pokud není nastaveno bool_only=True (v tom případě je vrácena hodnota False).

    Výkonnostní úvahy:
    ================

    Při implementaci a používání validátorů odvozených od této třídy je důležité
    zvažovat výkonnostní dopady:

    1. Validace iterovatelných struktur je výpočetně náročnější než jednoduchá
       kontrola typu, protože vyžaduje procházení všech prvků v kontejneru.

    2. Rekurzivní validace vnořených struktur může být velmi náročná pro hluboce
       vnořené nebo rozsáhlé datové struktury.

    3. Parametr depth_check lze použít k omezení hloubky validace a tím ke snížení
       výpočetní náročnosti, pokud není potřeba validovat všechny úrovně vnořených struktur.

    4. Pro kritické sekce kódu nebo validaci velmi rozsáhlých datových struktur
       může být vhodné validovat pouze typ kontejneru (depth_check=False) a vnitřní
       validaci provádět až v případě potřeby.

    Rozšíření a přizpůsobení:
    =======================

    Při vytváření nového validátoru odvozeného od této třídy:

    1. Vždy definujte všechny povinné atributy (VALIDATOR_KEY, ANNOTATION, ORIGIN, atd.)

    2. Ujistěte se, že ORIGIN je nastaven na správný Python typ nebo tuple typů,
       který bude použit pro is_instance kontrolu.

    3. Přepište metodu __call__ pouze tehdy, když standardní implementace
       nestačí pro daný typ validace (např. pro heterogenní tuple s různými typy prvků)

    4. Používejte výstižné hodnoty pro DESCRIPTION a LONG_DESCRIPTION,
       které pomohou uživatelům pochopit účel validátoru a požadavky na validovaná data
    """

    def __call__(
            self,
            value: Any,
            annotation: Any,
            custom_types: Optional[dict] = None,
            inner_check: Union[bool, int] = True,
            duck_typing: bool = False,
            bool_only: bool = False
    ) -> Union[bool, Any]:
        """
        Implementace validační metody pro kontejnerové typy s validací vnitřních prvků.

        Tato metoda zajišťuje dvouúrovňovou validaci iterovatelných struktur:
        1. Kontrola, zda hodnota odpovídá očekávanému kontejnerovému typu
        2. Validace jednotlivých prvků uvnitř kontejneru proti specifikovanému vnitřnímu typu

        Algoritmus validace:
        ------------------
        1. Deleguje validaci na specializovanou funkci iterable_item_verifier, která:
           a) Nejprve ověří, zda hodnota je instancí očekávaného kontejnerového typu
           b) Pokud je požadována vnitřní validace (inner_check není False), extrahuje
              typové parametry z anotace a validuje každý prvek kontejneru
           c) V případě vnořených struktur provádí rekurzivní validaci s respektováním
              nastavené hloubky validace

        2. Na základě parametru bool_only buď vrací výsledek jako boolean hodnotu,
           nebo v případě neúspěchu vyvolá výjimku s podrobným popisem problému

        Args:
            value (Any):
                Hodnota, která má být validována. Očekává se, že bude iterovatelná
                struktura odpovídající atributu ORIGIN validátoru.

            annotation (Any):
                Typová anotace proti které se má hodnota validovat.
                V kontextu této třídy obvykle obsahuje informace o vnitřním typu
                prvků (např. List[int], Set[str]).

            custom_types (Optional[dict], default=None):
                Slovník uživatelsky definovaných typů pro rozšířenou validaci.
                Používá se při rekurzivní validaci vnitřních prvků, pokud ty
                obsahují odkazy na uživatelsky definované typy.

            inner_check (Union[bool, int], default=True):
                Parametr řídící hloubku validace vnořených typů:
                - True: Validují se všechny úrovně vnořených struktur
                - False: Validuje se pouze typ kontejneru, ne vnitřní prvky
                - int: Validují se vnitřní prvky do specifikované maximální hloubky

            duck_typing (bool, default=False):
                Příznak, zda má být povolena duck typing validace.
                V kontextu BaseIterableItemValidator typicky není využíván,
                protože validace kontejnerů vyžaduje přesnou kontrolu typu.

            bool_only (bool, default=False):
                Příznak určující způsob hlášení nevalidních hodnot:
                - True: vrací False místo vyvolání výjimky
                - False: vyvolá výjimku s podrobným popisem problému

        Returns:
            Union[bool, Any]:
                - True: pokud je hodnota validní kontejner s validními prvky
                - False: pokud hodnota není validní a bool_only=True

        Raises:
            VerifyTypeError:
                Pokud hodnota není instancí očekávaného kontejnerového typu
                a bool_only=False.

            VerifyValueError:
                Pokud některý z prvků kontejneru neodpovídá očekávanému vnitřnímu typu
                a bool_only=False.

            VerifyUnexpectedInternalError:
                Pokud dojde k neočekávané chybě během validace
                (např. problém při extrakci typových parametrů).

        Poznámky:
            1. Parametr inner_check je klíčový pro řízení hloubky validace a může
               významně ovlivnit výkonnost validace, zejména pro velké nebo hluboce
               vnořené struktury.

            2. Validace vnitřních prvků je prováděna sekvenčně, takže v případě nevalidního
               prvku je výjimka vyvolána ihned, bez kontroly zbývajících prvků.

            3. Pro heterogenní kontejnery (např. Tuple[int, str, float]) by měly být
               použity specializované validátory, které přepisují tuto metodu, protože
               standardní implementace předpokládá homogenní typ prvků.

        Příklad použití v rámci aplikace:

        ```python
        # Vytvoření validátoru pro typ List
        validator = ListValidator()

        # Přímá validace hodnoty
        try:
            validator([1, 2, 3], List[int])  # Vrátí True
            validator(["a", "b"], List[int])  # Vyvolá VerifyValueError
            validator({1, 2, 3}, List[int])  # Vyvolá VerifyTypeError
        except VerifyError as e:
            print(f"Chyba validace: {e}")

        # Validace s návratovou hodnotou místo výjimky
        result = validator(["a", "b"], List[int], bool_only=True)  # Vrátí False

        # Validace pouze typu kontejneru, ne vnitřních prvků
        result = validator(["a", "b"], List[int], inner_check=False)  # Vrátí True
        ```
        """

        # Navrácení výstupu funkce pro validaci iterovatelných objektů
        return iterable_item_verifier(
            value,
            self.IS_INSTANCE,
            self.DUCK_TYPING,
            annotation,
            custom_types,
            inner_check,
            duck_typing,
            bool_only
        )


