from typing import Any, Optional, Union

from .base_validator import BaseValidator
from ._verifiers import is_instance_verifier, duck_typing_verifier


class BaseIsInstanceValidator(BaseValidator):
    """
    Základní třída pro validátory založené na kontrole typu pomocí isinstance().

    BaseIsInstanceValidator poskytuje implementaci pro nejběžnější typ validace v typovém
    systému - ověření, zda hodnota je instancí očekávaného typu. Tato třída je navržena
    jako základní stavební blok pro validátory jednoduchých typů (int, str, float, bool, atd.)
    a dalších neparametrických typů, které lze ověřit pomocí přímé kontroly typu.

    Klíčové koncepty:
    ================

    1. Přímá typová validace
       Základním principem této třídy je použití Pythonového operátoru isinstance()
       pro ověření typu hodnoty. Tato metoda je efektivní a přesná, ale funguje pouze
       pro hodnoty, které jsou přímými potomky validovaného typu nebo s ním kompatibilní
       podle hierarchie dědičnosti v Pythonu.

    2. Duck typing podpora
       Kromě přímé kontroly typu poskytuje třída také podporu pro "duck typing" -
       princip, kdy objekt je považován za validní, pokud má požadované chování
       (atributy, metody), bez ohledu na jeho skutečný typ. Tento přístup je
       typický pro Python a umožňuje větší flexibilitu při validaci.

    3. Delegování validace
       Implementace validační logiky je delegována na specializované funkce
       (is_instance_verifier a duck_typing_verifier), což zajišťuje oddělení
       zodpovědností a umožňuje znovupoužití validační logiky.

    4. Minimální režie
       Tato třída je navržena s důrazem na minimální výpočetní režii pro jednoduché
       validace, což je klíčové pro efektivitu celého validačního systému, zejména
       při validaci velkého množství hodnot nebo složitých datových struktur.

    Architekturální kontext:
    ======================

    V hierarchii validátorů představuje BaseIsInstanceValidator nejjednodušší a
    nejčastěji používaný typ validátoru. Zatímco BaseValidator definuje obecné rozhraní,
    tato třída poskytuje konkrétní implementaci pro validaci založenou na typu.

    Validátory odvozené od této třídy typicky:
    1. Nastavují atribut IS_INSTANCE na požadovaný typ nebo tuple typů
    2. Volitelně definují DUCK_TYPING pro případy, kdy je potřeba flexibilnější validace
    3. Ve většině případů nemusí přepisovat metodu __call__, protože zdědí její
       implementaci z této třídy

    Některé složitější validátory (AnyValidator, CallableValidator, LiteralValidator, atd.)
    však mohou metodu __call__ přepsat, pokud potřebují provést specializovanější
    validaci, která není pokryta standardním ověřením typu.

    Použití pro odvozené třídy:
    =========================

    Příklad definice jednoduchého validátoru pro typ int:

    ```python
    class IntValidator(BaseIsInstanceValidator):
        VALIDATOR_KEY = "int"
        ANNOTATION = int
        IS_INSTANCE = int  # Typ pro kontrolu pomocí isinstance()
        DUCK_TYPING = None  # Pro int nepodporujeme duck typing
        DESCRIPTION = "Celé číslo"
        LONG_DESCRIPTION = "Validuje, že objekt je celé číslo (int)."
    ```

    Příklad validátoru s podporou duck typing:

    ```python
    class IterableValidator(BaseIsInstanceValidator):
        VALIDATOR_KEY = "iterable"
        ANNOTATION = Iterable
        IS_INSTANCE = collections.abc.Iterable
        DUCK_TYPING = {
            "has_attr": ("__iter__",)  # Ověření, že objekt má metodu __iter__
        }
        DESCRIPTION = "Iterovatelný objekt"
        LONG_DESCRIPTION = "Validuje, že objekt je iterovatelný (má metodu __iter__)."
    ```

    Duck typing mechanismy:
    =====================

    Validátor podporuje několik typů duck typing kontrol:

    1. "has_attr" - Ověření existence atributů nebo metod
       Kontroluje, zda objekt má všechny uvedené atributy, což je užitečné pro ověření
       základních protokolů (jako je iterovatelnost, volatelnost, atd.).

    2. "has_callable_attr" - Ověření existence volatelných atributů
       Kontroluje, zda objekt má uvedené atributy a zda jsou volatelné (funkce, metody).

    3. "has_coroutine_attr" - Ověření korutinových metod
       Specializovaná kontrola pro asynchronní protokoly, ověřuje, že atribut
       je korutinová funkce.

    4. "has_int_attr" - Ověření celočíselných atributů
       Používá se především pro validaci časových objektů (např. datetime),
       kdy se ověřuje, že atribut má celočíselnou hodnotu.

    5. "lambda" - Vlastní validační funkce
       Umožňuje definovat libovolnou validační logiku pomocí lambda funkce.

    Výkonnostní úvahy:
    ================

    Při implementaci a používání validátorů odvozených od této třídy je důležité
    zvažovat výkonnostní dopady:

    1. isinstance() je velmi efektivní operace v Pythonu, zatímco duck typing kontroly
       mohou být výrazně náročnější.

    2. Duck typing by měl být používán pouze tehdy, když je opravdu potřeba
       (např. pro validaci protokolů nebo při práci s objekty třetích stran).

    3. Pro kritické aplikace nebo validaci velkého množství dat může být vhodné
       upřednostnit přímou kontrolu typu před duck typingem.

    Rozšíření a přizpůsobení:
    =======================

    Při vytváření nového validátoru odvozeného od této třídy:

    1. Vždy definujte všechny povinné atributy (VALIDATOR_KEY, ANNOTATION, atd.)

    2. Pečlivě zvažte, zda má validátor podporovat duck typing, a pokud ano,
       jaké kontroly jsou potřeba

    3. Přepište metodu __call__ pouze tehdy, když standardní implementace
       nestačí pro daný typ validace

    4. Používejte výstižné hodnoty pro DESCRIPTION a LONG_DESCRIPTION,
       které pomohou uživatelům pochopit účel validátoru
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
        Implementace validační metody pro kontrolu typu hodnoty.

        Tato metoda provádí dva typy validace:

        1. Primární validace pomocí isinstance() - ověřuje, zda hodnota je instancí
           očekávaného typu definovaného v atributu IS_INSTANCE

        2. Volitelná duck typing validace - pokud je vyžadována a podporována,
           ověřuje, zda objekt má požadované chování (atributy, metody) bez ohledu
           na jeho skutečný typ

        Algoritmus validace:
        ------------------
        1. Pokud je požadován duck typing a validátor ho podporuje (má definovaný
           atribut DUCK_TYPING), deleguje validaci na duck_typing_verifier

        2. V opačném případě používá standardní is_instance_verifier pro přímou
           kontrolu typu

        3. Na základě parametru bool_only buď vrací výsledek jako boolean hodnotu,
           nebo v případě neúspěchu vyvolá výjimku s podrobným popisem problému

        Args:
            value (Any):
                Hodnota, která má být validována proti typové anotaci.

            annotation (Any):
                Typová anotace proti které se má hodnota validovat.
                V kontextu této třídy typicky odpovídá atributu ANNOTATION.

            custom_types (Optional[dict], default=None):
                Slovník uživatelsky definovaných typů pro rozšířenou validaci.
                Pro jednoduché validátory typicky není použit.

            inner_check (Union[bool, int], default=True):
                Parametr řídící hloubku validace vnořených typů.
                Pro jednoduché validátory typicky není relevantní.

            duck_typing (bool, default=False):
                Příznak, zda má být povolena duck typing validace.
                Pokud je True a validátor podporuje duck typing (má definovaný
                atribut DUCK_TYPING), provede se flexibilnější validace založená
                na kontrole požadovaných atributů/metod.

            bool_only (bool, default=False):
                Příznak určující způsob hlášení nevalidních hodnot:
                - True: vrací False místo vyvolání výjimky
                - False: vyvolá výjimku s podrobným popisem problému

        Returns:
            Union[bool, Any]:
                - True: pokud je hodnota validní vzhledem k očekávanému typu
                - False: pokud hodnota není validní a bool_only=True

        Raises:
            VerifyTypeError:
                Pokud hodnota není validní a bool_only=False. Výjimka obsahuje
                podrobný popis problému a návod na jeho řešení.

        Poznámky:
            1. Duck typing validace je výpočetně náročnější než přímá kontrola typu,
               proto je ve výchozím nastavení vypnutá (duck_typing=False).

            2. Parametr bool_only ovlivňuje pouze způsob hlášení nevalidních hodnot,
               nemá vliv na jiné typy výjimek (např. chybně specifikované anotace).

            3. Tato metoda deleguje skutečnou validační logiku na specializované
               funkce, což umožňuje její znovupoužití a testování.

        Příklad použití v rámci aplikace:

        ```python
        # Vytvoření validátoru pro typ int
        validator = IntValidator()

        # Přímá validace hodnoty
        try:
            validator(42, int)  # Vrátí True
            validator("text", int)  # Vyvolá VerifyTypeError
        except VerifyTypeError as e:
            print(f"Chyba validace: {e}")

        # Validace s návratovou hodnotou místo výjimky
        result = validator("text", int, bool_only=True)  # Vrátí False
        ```
        """

        # Pokud je zadán požadavek na duck typing a validační třída podporuje
        if duck_typing and self.DUCK_TYPING:

            # Volání funkce pro ověření na základě příkazů pro duck typing
            return duck_typing_verifier(value, self.DUCK_TYPING, bool_only)

        # Standardní validace pomocí isinstance
        return is_instance_verifier(value, self.IS_INSTANCE, bool_only)