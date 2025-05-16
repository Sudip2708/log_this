from typing import Any, Optional, Union
from abc import ABC, abstractmethod

from .tools import attributes_check


class BaseValidator(ABC):
    """
    Základní abstraktní třída pro všechny validátory typových anotací.

    BaseValidator definuje společné rozhraní a mechanismy pro validaci hodnot
    proti typovým anotacím v Pythonu. Slouží jako základ architektury celého
    validačního systému a zajišťuje konzistentní chování napříč všemi validátory.

    Klíčové koncepty:
    ================

    1. Validační proces
       Validátory ověřují, zda hodnota odpovídá určité typové anotaci. Každý validátor
       se specializuje na konkrétní typ anotace (např. int, str, List[T], Dict[K, V], atd.)
       a implementuje logiku potřebnou pro jeho validaci.

    2. Architektura validátorů
       Validační systém používá hierarchii tříd, kde BaseValidator definuje základní rozhraní
       a specializované základní třídy (např. BaseIsInstanceValidator, BaseIterableItemValidator)
       implementují společnou logiku pro určité kategorie validátorů. Koncové validační třídy
       pak obsahují specifickou implementaci pro konkrétní Python typy.

    3. Povinné třídní atributy
       Každá validační třída musí definovat sadu povinných atributů, které určují její chování,
       popisují validovaný typ a poskytují informace pro uživatele. Tyto atributy jsou kontrolovány
       při inicializaci podtřídy pomocí metody __init_subclass__.

    4. Metoda validace
       Hlavním vstupním bodem pro validaci je metoda __call__, která musí být implementována
       v každé podtřídě. To umožňuje používat instance validátorů jako funkce.

    Povinné třídní atributy:
    =======================

    VALIDATOR_KEY: str
        Unikátní identifikátor validátoru používaný při registraci a vyhledávání validátorů.
        Obvykle odpovídá názvu validovaného typu (např. "int", "list", "dict", atd.).

    ANNOTATION: Any
        Typová anotace, kterou validátor zpracovává. Slouží pro automatickou registraci
        validátorů a kontrolu kompatibility s požadavky.

    IS_INSTANCE: Any
        Typ nebo tuple typů pro kontrolu pomocí isinstance(). Určuje základní typy,
        které validátor akceptuje. Pro validátory s vlastní logikou může být None.

    DUCK_TYPING: Optional[dict]
        Specifikace pro duck-typing validaci, pokud je podporována. Může obsahovat
        klíče jako "has_attr" pro kontrolu přítomnosti atributů nebo metod.
        Pro validátory bez podpory duck-typing je None.

    DESCRIPTION: str
        Stručný popis validovaného typu pro dokumentaci a chybové zprávy.

    LONG_DESCRIPTION: str
        Podrobný popis validovaného typu a procesu validace pro rozšířenou dokumentaci
        a vysvětlení v nápovědě.

    Příklady implementace:
    ====================

    Příklad definice validátoru pro typ int:

    ```python
    class IntValidator(BaseIsInstanceValidator):
        VALIDATOR_KEY = "int"
        ANNOTATION = int
        IS_INSTANCE = int
        DUCK_TYPING = None
        DESCRIPTION = "Celé číslo"
        LONG_DESCRIPTION = "Validuje, že objekt je celé číslo (int)."
    ```

    Příklad definice validátoru pro seznam (List):

    ```python
    class ListValidator(BaseIterableItemValidator):
        VALIDATOR_KEY = "list"
        ANNOTATION = List[T]
        IS_INSTANCE = list
        DUCK_TYPING = {
            "has_attr": ("__getitem__", "__iter__", "__len__"),
        }
        DESCRIPTION = "Seznam"
        LONG_DESCRIPTION = "Validuje, že objekt je seznam (list) a ověřuje typy jeho prvků."
    ```

    Rozšíření systému:
    =================

    Při vytváření nového validátoru je třeba:
    1. Zvolit vhodnou základní třídu (BaseIsInstanceValidator, BaseIterableItemValidator, atd.)
    2. Definovat všechny povinné třídní atributy
    3. Případně přepsat metodu __call__, pokud je potřeba specifická validační logika

    Systém automaticky zkontroluje přítomnost všech povinných atributů při vytvoření
    nové podtřídy díky mechanismu __init_subclass__.
    """

    # Povinné konstanty, které musí definovat každá koncová validační třída
    VALIDATOR_KEY: Optional[str] = None
    ANNOTATION: Any = None
    IS_INSTANCE: Any = None
    DUCK_TYPING: Optional[dict] = None
    DESCRIPTION: Optional[str] = None
    LONG_DESCRIPTION: Optional[str] = None

    def __init_subclass__(cls):
        """
        Kontrola povinných atributů při vytvoření podtřídy BaseValidator.

        Tato metoda se automaticky spustí při definici každé nové podtřídy
        BaseValidator a zajišťuje, že třída má správně definované všechny
        povinné atributy. Tento mechanismus pomáhá předcházet chybám
        při implementaci nových validátorů a zajišťuje konzistenci
        v celém validačním systému.

        Metoda __init_subclass__ je mocný nástroj zavedený v PEP 487,
        který umožňuje rodičovské třídě reagovat na vytvoření potomka
        a provádět různé operace, jako je:

        1. Registrace validátorů v centrálním registru
        2. Kontrola kompletnosti implementace
        3. Nastavení výchozích hodnot
        4. Modifikace třídy nebo jejích atributů
        5. Vynucení invariantů a designových pravidel

        V našem případě ji používáme ke kontrole přítomnosti všech
        povinných atributů, což zajišťuje, že každý validátor bude
        mít všechny potřebné informace pro správné fungování v rámci
        validačního systému.

        Raises:
            VerifyNotImplementedAttributeError: Pokud třída nemá definované
                všechny povinné atributy.
        """
        super().__init_subclass__()
        # Kontrola, zda jsou všechny povinné atributy definovány
        attributes_check(cls)

    @abstractmethod
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
        Validační metoda pro ověření hodnoty proti typové anotaci.

        Tato abstraktní metoda definuje jednotné rozhraní pro validaci
        v celém systému. Díky použití metody __call__ lze instance validátorů
        používat přímo jako funkce. Každá podtřída musí implementovat tuto
        metodu a definovat specifickou validační logiku pro daný typ.

        Validační proces obvykle zahrnuje tyto kroky:
        1. Kontrola základního typu pomocí isinstance (pokud je relevantní)
        2. Specializovaná validace podle konkrétního typu
        3. Případná validace vnořených typů (pro kontejnerové typy)
        4. Vrácení výsledku nebo vyvolání výjimky

        Args:
            value (Any):
                Hodnota, která má být validována proti typové anotaci.
                Může se jednat o libovolný Python objekt.

            annotation (Any):
                Typová anotace proti které se má hodnota validovat.
                Může se jednat o základní typ (int, str), generický typ (List[int]),
                typový alias, union nebo jiný konstrukt z modulu typing.

            custom_types (Optional[dict], default=None):
                Slovník uživatelsky definovaných typů, které mají být brány v úvahu
                při validaci. Umožňuje rozšířit systém o vlastní typy. Výchozí je None.

            inner_check (Union[bool, int], default=True):
                Řídí hloubku validace vnořených typů:
                - True: Validují se i vnořené typy (neomezená hloubka)
                - False: Validuje se pouze hlavní typ (bez vnořených typů)
                - int: Validují se vnořené typy do zadané hloubky
                Výchozí je True.

            duck_typing (bool, default=False):
                Pokud je True, povoluje validaci pomocí duck-typing principu,
                kdy se nekontroluje přesný typ, ale pouze požadované metody
                nebo atributy. Výchozí je False.

            bool_only (bool, default=False):
                Řídí způsob hlášení neúspěšné validace:
                - True: Vrací False místo vyvolání výjimky
                - False: Vyvolá výjimku s podrobným popisem problému
                Výchozí je False.

        Returns:
            Union[bool, Any]:
                - True, pokud je hodnota validní vůči dané anotaci
                - False, pokud hodnota není validní a bool_only=True
                - Transformovaná hodnota v případě validátorů, které provádí konverzi

        Raises:
            Výjimky odvozené od VerifyError, pokud validace selže a bool_only=False.
            Konkrétní typ výjimky závisí na implementaci v podtřídě.

        Poznámky:
            Tato metoda je označena jako abstraktní, což znamená, že musí být
            implementována v každé konkrétní podtřídě. Abstraktní metody slouží
            k definici rozhraní a vynucení jeho implementace v potomcích.
        """
        pass