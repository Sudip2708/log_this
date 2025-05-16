from typing import Any, Optional, Union

from .base_validator import BaseValidator
from .._verifiers import iterable_key_value_verifier


class BaseIterableKeyValueValidator(BaseValidator):
    """
    Základní třída pro validátory slovníkových a klíč-hodnota struktur.

    BaseIterableKeyValueValidator poskytuje implementaci pro validaci generických asociativních
    typů, jako jsou Dict[K, V], Mapping[K, V], MutableMapping[K, V] a další struktury,
    které obsahují páry klíč-hodnota. Tato třída zajišťuje třístupňovou validaci - nejprve
    ověří, že hodnota je instancí očekávaného asociativního typu, a následně validuje
    každý klíč a každou hodnotu ve slovníku proti definovaným typům.

    Klíčové koncepty:
    ================

    1. Generické typy s dvojicí parametrů
       Tato třída pracuje s generickými typy, které v Pythonu vyžadují dva typové
       parametry - jeden pro klíče a jeden pro hodnoty (např. Dict[str, int]). Tyto
       typové parametry jsou extrahovány z anotace a použity pro validaci jednotlivých
       klíčů a hodnot v asociativní struktuře.

    2. Dvojitá rekurzivní typová validace
       Na rozdíl od jednoduchých iterovatelných struktur, kde se validuje pouze jeden
       typ prvků, zde probíhá nezávislá validace pro klíče a hodnoty. To umožňuje
       pracovat i se složitými vnořenými strukturami jako Dict[str, List[Dict[int, bool]]],
       kde je nutná rekurzivní validace hodnot.

    3. Kontrola hloubky vnořených struktur
       Parametr depth_check řídí, jak hluboko v hierarchii vnořených struktur má
       validace pokračovat. To je zvláště důležité u slovníkových struktur, které
       mohou obsahovat komplexní vnořené datové struktury jako hodnoty.

    4. Delegování validace
       Podobně jako u ostatních validátorů, i tato třída deleguje vlastní validační
       logiku na specializovanou funkci (iterable_key_value_verifier), což zajišťuje
       oddělení zodpovědností a umožňuje znovupoužití validační logiky.

    Architekturální kontext:
    ======================

    V hierarchii validátorů představuje BaseIterableKeyValueValidator nejvyšší stupeň
    složitosti standardních validátorů. Zatímco BaseIsInstanceValidator pracuje pouze
    s přímou kontrolou typu a BaseIterableItemValidator přidává validaci vnitřních prvků,
    tato třída rozšiřuje validaci na dvě nezávislé typové kontroly pro klíče a hodnoty.

    Validátory odvozené od této třídy typicky:
    1. Nastavují atribut IS_INSTANCE na požadovaný asociativní typ (dict, collections.OrderedDict, atd.)
    2. Definují VALIDATOR_KEY a ANNOTATION pro příslušný typ z modulu typing (Dict, Mapping, atd.)
    3. Ve většině případů nemusí přepisovat metodu __call__, protože zdědí její
       implementaci z této třídy

    Mezi běžné validátory odvozené od této třídy patří DictValidator, MappingValidator,
    OrderedDictValidator a další validátory pro asociativní datové struktury.

    Použití pro odvozené třídy:
    =========================

    Příklad definice validátoru pro typ Dict:

    ```python
    class DictValidator(BaseIterableKeyValueValidator):
        VALIDATOR_KEY = "dict"
        ANNOTATION = Dict
        IS_INSTANCE = dict
        DESCRIPTION = "Slovník"
        LONG_DESCRIPTION = "Validuje, že objekt je slovník (dict) s klíči a hodnotami odpovídajícími specifikovaným typům."
    ```

    Příklad definice validátoru pro typ Mapping:

    ```python
    class MappingValidator(BaseIterableKeyValueValidator):
        VALIDATOR_KEY = "mapping"
        ANNOTATION = Mapping
        IS_INSTANCE = collections.abc.Mapping
        DESCRIPTION = "Mapování"
        LONG_DESCRIPTION = "Validuje, že objekt implementuje protokol mapování (Mapping) s klíči a hodnotami odpovídajícími specifikovaným typům."
    ```

    Detaily implementace:
    ===================

    Validace asociativních struktur probíhá ve třech krocích:

    1. Prvotní validace typu kontejneru:
       Nejprve se ověří, zda je hodnota instancí očekávaného asociativního typu
       (definovaného v atributu IS_INSTANCE) pomocí is_instance_verifier.

    2. Extrakce typových parametrů:
       Z typové anotace se extrahují informace o očekávaných typech klíčů a hodnot.
       Pokud tyto informace nejsou k dispozici (např. při použití nespecifického Dict
       bez typových parametrů), validace se omezí pouze na kontrolu typu kontejneru.

    3. Validace jednotlivých klíčů a hodnot:
       Pro každý pár klíč-hodnota ve slovníku se provede rekurzivní validace klíče
       proti očekávanému typu klíče a hodnoty proti očekávanému typu hodnoty.

    Chybové stavy:
    ============

    Při validaci asociativních struktur mohou nastat následující chybové stavy:

    1. Hodnota není instancí očekávaného asociativního typu
       (např. pokud je očekáván slovník, ale hodnota je seznam)

    2. Některý z klíčů neodpovídá očekávanému typu klíče
       (např. v Dict[int, str] je klíč typu řetězec)

    3. Některá z hodnot neodpovídá očekávanému typu hodnoty
       (např. v Dict[str, int] je hodnota typu řetězec)

    4. Problém při extrakci typových parametrů z anotace
       (nevalidní nebo neúplná typová anotace)

    V případě chyby validace je generována příslušná výjimka s podrobným popisem problému,
    pokud není nastaveno bool_only=True (v tom případě je vrácena hodnota False).

    Výkonnostní úvahy:
    ================

    Při implementaci a používání validátorů odvozených od této třídy je důležité
    zvažovat výkonnostní dopady:

    1. Validace asociativních struktur je výpočetně náročnější než validace jednoduchých
       kolekcí, protože vyžaduje dvojitou validaci pro každý pár klíč-hodnota.

    2. Rekurzivní validace vnořených struktur může být velmi náročná, zejména pokud
       hodnoty obsahují další vnořené slovníky nebo komplexní datové struktury.

    3. Parametr depth_check lze použít k omezení hloubky validace a tím ke snížení
       výpočetní náročnosti, pokud není potřeba validovat všechny úrovně vnořených struktur.

    4. Pro kritické sekce kódu nebo validaci velmi rozsáhlých slovníků může být vhodné
       validovat pouze typ kontejneru (depth_check=False) a vnitřní validaci provádět
       až v případě potřeby nebo selektivně pro konkrétní klíče.

    Typové anotace a typová bezpečnost:
    =================================

    Tato třída je klíčová pro zajištění typové bezpečnosti při práci se slovníky
    a mapováními v typovaném Pythonu. Poskytuje most mezi statickou typovou kontrolou
    (která probíhá během vývoje pomocí nástrojů jako mypy) a dynamickou validací
    za běhu programu.

    U slovníkových typů je typová bezpečnost obzvláště důležitá, protože:

    1. Slovníky často obsahují strukturovaná data načtená z externích zdrojů (JSON, YAML, databáze),
       kde není předem zaručen typ klíčů nebo hodnot.

    2. Chyby v typech klíčů mohou vést k neočekávanému chování při vyhledávání
       a manipulaci s daty.

    3. Vnořené datové struktury ve slovnících jsou častým zdrojem chyb při zpracování dat,
       pokud nejsou typy správně validovány.

    Rozšíření a přizpůsobení:
    =======================

    Při vytváření nového validátoru odvozeného od této třídy:

    1. Vždy definujte všechny povinné atributy (VALIDATOR_KEY, ANNOTATION, IS_INSTANCE, atd.)

    2. Ujistěte se, že IS_INSTANCE je nastaven na správný Python typ nebo tuple typů,
       který bude použit pro is_instance kontrolu.

    3. Přepište metodu __call__ pouze tehdy, když standardní implementace
       nestačí pro daný typ validace (např. pro speciální typy mapování
       s nestandardním chováním)

    4. Pokud validátor podporuje nestandardní formáty typových anotací nebo
       speciální chování pro určité typy klíčů nebo hodnot, je vhodné toto
       podrobně dokumentovat v popisu validátoru
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
        Implementace validační metody pro asociativní typy s validací klíčů a hodnot.

        Tato metoda zajišťuje třístupňovou validaci slovníkových struktur:
        1. Kontrola, zda hodnota odpovídá očekávanému asociativnímu typu
        2. Validace každého klíče proti specifikovanému typu klíče
        3. Validace každé hodnoty proti specifikovanému typu hodnoty

        Algoritmus validace:
        ------------------
        1. Deleguje validaci na specializovanou funkci iterable_key_value_verifier, která:
           a) Nejprve ověří, zda hodnota je instancí očekávaného asociativního typu
           b) Pokud je požadována vnitřní validace (inner_check není False), extrahuje
              typové parametry pro klíče a hodnoty z anotace
           c) Pro každý pár klíč-hodnota provede rekurzivní validaci klíče a hodnoty
              proti příslušným typovým parametrům
           d) V případě vnořených struktur respektuje nastavenou hloubku validace
              (parametr inner_check)

        2. Na základě parametru bool_only buď vrací výsledek jako boolean hodnotu,
           nebo v případě neúspěchu vyvolá výjimku s podrobným popisem problému

        Args:
            value (Any):
                Hodnota, která má být validována. Očekává se, že bude asociativní
                struktura odpovídající atributu IS_INSTANCE validátoru.

            annotation (Any):
                Typová anotace proti které se má hodnota validovat.
                V kontextu této třídy obvykle obsahuje informace o typech klíčů
                a hodnot (např. Dict[str, int], Mapping[int, List[str]]).

            custom_types (Optional[dict], default=None):
                Slovník uživatelsky definovaných typů pro rozšířenou validaci.
                Používá se při rekurzivní validaci klíčů a hodnot, pokud obsahují
                odkazy na uživatelsky definované typy.

            inner_check (Union[bool, int], default=True):
                Parametr řídící hloubku validace vnořených typů:
                - True: Validují se všechny úrovně vnořených struktur
                - False: Validuje se pouze typ kontejneru, ne klíče a hodnoty
                - int: Validují se klíče a hodnoty do specifikované maximální hloubky

            duck_typing (bool, default=False):
                Příznak, zda má být povolena duck typing validace.
                V kontextu BaseIterableKeyValueValidator typicky není využíván,
                protože validace asociativních struktur vyžaduje přesnou kontrolu typu.

            bool_only (bool, default=False):
                Příznak určující způsob hlášení nevalidních hodnot:
                - True: vrací False místo vyvolání výjimky
                - False: vyvolá výjimku s podrobným popisem problému

        Returns:
            Union[bool, Any]:
                - True: pokud je hodnota validní asociativní struktura s validními klíči a hodnotami
                - False: pokud hodnota není validní a bool_only=True

        Raises:
            VerifyTypeError:
                Pokud hodnota není instancí očekávaného asociativního typu a bool_only=False.

            VerifyValueError:
                Pokud některý z klíčů nebo hodnot neodpovídá očekávanému typu a bool_only=False.

            VerifyUnexpectedInternalError:
                Pokud dojde k neočekávané chybě během validace
                (např. problém při extrakci typových parametrů).

        Poznámky:
            1. Při validaci asociativních struktur je důležité brát v úvahu,
               že Python slovníky mohou mít klíče různých typů (na rozdíl od některých
               jiných jazyků, které vyžadují homogenní typy klíčů).

            2. Parametr inner_check je klíčový pro řízení hloubky validace a může
               významně ovlivnit výkonnost validace, zejména pro velké slovníky
               nebo slovníky s komplexními vnořenými strukturami.

            3. Validace probíhá sekvenčně pro každý pár klíč-hodnota, takže v případě
               nevalidního klíče nebo hodnoty je výjimka vyvolána ihned, bez kontroly
               zbývajících párů.

        Příklad použití v rámci aplikace:

        ```python
        # Vytvoření validátoru pro typ Dict
        validator = DictValidator()

        # Přímá validace hodnoty
        try:
            validator({"a": 1, "b": 2}, Dict[str, int])  # Vrátí True
            validator({"a": "value"}, Dict[str, int])    # Vyvolá VerifyValueError
            validator([1, 2, 3], Dict[str, int])         # Vyvolá VerifyTypeError
        except VerifyError as e:
            print(f"Chyba validace: {e}")

        # Validace s návratovou hodnotou místo výjimky
        result = validator({"a": "value"}, Dict[str, int], bool_only=True)  # Vrátí False

        # Validace pouze typu kontejneru, ne klíčů a hodnot
        result = validator({"a": "value"}, Dict[str, int], inner_check=False)  # Vrátí True

        # Validace slovníku s vnořenou strukturou
        nested_dict = {"users": {"alice": [1, 2], "bob": [3, 4]}}
        validator(nested_dict, Dict[str, Dict[str, List[int]]])  # Vrátí True
        ```
        """

        # Navrácení výstupu funkce pro validaci slovníkových objektů
        return iterable_key_value_verifier(
            value, self.IS_INSTANCE, annotation, inner_check, custom_types, bool_only
        )

