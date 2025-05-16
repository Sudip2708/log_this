from typing import List, Optional, Union, Iterable
from ..._typing_aliases import TypeLike, CollectionOfTypeLike

from ._get_simplified_traceback import get_simplified_traceback


class VerifyError(Exception):
    """
    Základní výjimka knihovny Verify, obsahující kostru a logiku chybových zpráv.

    Tato třída slouží jako základ pro všechny výjimky v knihovně a poskytuje
    jednotný formát chybových zpráv včetně zjednodušeného tracebacku,
    popisu problému a návodu na jeho řešení.

    Klíčové koncepty:
    -----------------
    * Uživatelsky přívětivé chybové zprávy - Zaměření na srozumitelnost a použitelnost
    * Struktura "Co se stalo" a "Jak to opravit" - Poskytnutí kontextu a řešení
    * Zjednodušený traceback - Filtrování relevantních částí tracebacku

    Architekturální kontext:
    -----------------------
    Tato třída slouží jako základ hierarchie výjimek pro celou knihovnu.
    Implementuje společnou logiku pro formátování chybových zpráv,
    kterou všichni potomci zdědí. Nabízí konzistentní a předvídatelný
    způsob, jakým jsou chyby prezentovány uživateli.

    Detaily implementace:
    --------------------
    * Používá `get_simplified_traceback` pro získání uživatelsky přívětivé verze tracebacku
    * Přijímá dva klíčové seznamy řetězců: "co se stalo" a "jak to opravit"
    * Sestavuje komplexní chybovou zprávu s formátováním pro lepší čitelnost
    * Přepisuje metodu `__str__` pro zajištění konzistentního výstupu

    Povinné atributy a metody:
    -------------------------
    * what_happened (List[str]): Seznam řetězců popisujících problém
    * what_to_do (List[str]): Seznam řetězců navrhujících řešení
    * message (str): Kompletní formátovaná chybová zpráva
    * traceback (List[str]): Filtrovaný traceback zaměřený na uživatelský kód

    Příklady použití:
    ---------------
    ```python
    # Vytvoření konkrétní výjimky odvozené od VerifyError
    class ValueFormatError(VerifyError):
        def __init__(self, value, expected_format):
            what_happened = [
                f"  Hodnota '{value}' nemá očekávaný formát.\n"
            ]
            what_to_do = [
                f"  Ujistěte se, že hodnota odpovídá formátu: {expected_format}\n"
            ]
            super().__init__(what_happened, what_to_do)

    # Vyvolání výjimky
    raise ValueFormatError("2023-13-45", "YYYY-MM-DD")
    ```

    Poznámky k rozšíření:
    --------------------
    * Při vytváření nových typů výjimek zachovejte formát seznamů pro `what_happened` a `what_to_do`
    * Pro komplexnější scénáře lze v potomcích přidat další atributy a logiku
    * Zvažte přidání metody pro přidání dalších informací do existující zprávy
    """

    # Třídní atributy definující strukturu chybové zprávy
    title: str = "\n⚠ DOŠLO K CHYBĚ PŘI OVĚŘOVÁNÍ!\n"
    what_happened_intro: str = "» Co se stalo:\n"
    what_to_do_intro: str = "» Jak to opravit:\n"

    def __init__(
            self,
            what_happened: Union[List[str], str],
            what_to_do: Union[List[str], str],
            title: Optional[str] = None,
    ):
        """
        Inicializuje výjimku s předdefinovanou strukturou zprávy.

        Vytváří komplexní chybovou zprávu, která obsahuje zjednodušený traceback,
        popis problému a návod na jeho řešení. Zpráva je formátována pro
        maximální srozumitelnost a použitelnost.

        Args:
            what_happened (Union[List[str], str]): Popis problému - buď jako seznam
                                                  řetězců, nebo jako jeden řetězec.
            what_to_do (Union[List[str], str]): Návod na řešení - buď jako seznam
                                               řetězců, nebo jako jeden řetězec.
            title (Optional[str]): Volitelný nadpis zprávy, který přepíše výchozí nadpis.
                                 Vhodné pro specifické kategorie chyb.

        Raises:
            TypeError: Pokud parametry `what_happened` nebo `what_to_do` nejsou
                      ani seznam řetězců, ani řetězec.

        Algoritmus:
        ----------
        1. Konverze vstupních parametrů na seznamy řetězců, pokud je potřeba
        2. Získání zjednodušeného tracebacku
        3. Sestavení kompletní chybové zprávy
        4. Předání zprávy nadřazené třídě Exception

        Poznámky:
        --------
        Metoda umožňuje flexibilní zadávání zpráv, ale zachovává strukturovaný formát
        výsledné chybové zprávy pro konzistentní uživatelský zážitek.
        """
        # Normalizace vstupních parametrů
        self.what_happened = self._ensure_string_list(what_happened)
        self.what_to_do = self._ensure_string_list(what_to_do)

        # Získání zjednodušeného tracebacku
        self.traceback = get_simplified_traceback()

        # Použití vlastního nadpisu, pokud je poskytnut
        self._title = title if title is not None else self.title

        # Vytvoření kompletní chybové zprávy
        self.message = self._create_error_message()

        # Inicializace nadřazené třídy Exception
        super().__init__(self.message)

    def _create_error_message(self) -> str:
        """
        Vytvoří formátovanou chybovou zprávu ze všech komponent.

        Spojuje traceback, nadpis, popis problému a návod na řešení
        do jedné formátované zprávy s konzistentním rozložením.

        Returns:
            str: Kompletní formátovaná chybová zpráva.

        Poznámky:
        --------
        Tato metoda je oddělena od __init__ pro lepší organizaci kódu
        a možnost přepsání v potomcích, pokud je potřeba jiný formát zprávy.
        """
        return (
                ''.join(self.traceback) + "\n" +
                self._title +
                self.what_happened_intro +
                ''.join(self.what_happened) +
                self.what_to_do_intro +
                ''.join(self.what_to_do)
        )

    @staticmethod
    def _ensure_string_list(value: Union[TypeLike, CollectionOfTypeLike]) -> List[str]:
        """
        Zajistí, že hodnota je seznam řetězců.

        Pokud je hodnota řetězec, převede ji na jednoprvkový seznam.

        Args:
            value (Union[TypeLike, CollectionOfTypeLike]): Vstupní hodnota,
                buď samostatný typ, nebo řetězec, nebo tuple či seznam.

        Returns:
            List[str]: Seznam řetězců.

        Raises:
            NotStringListInternalError: Pokud vstupní hodnota není ani seznam řetězců, ani řetězec.

        Poznámky:
        --------
        Tato pomocná metoda umožňuje flexibilnější použití konstruktoru
        přijímáním jak jednotlivých řetězců, tak seznamů.
        """
        try:

            # Pokud je hodnota řetězec
            if isinstance(value, str):
                return [value]

            # Pokud je hodnota seznam řetězců
            if isinstance(value, list) and all(
                    isinstance(item, str) for item in value):
                return value

            # Ve všech ostatních případech vyvolej výjimku
            raise TypeError

        except TypeError:
            # Interní import z důvodu cyklického erroru
            from ..internal_errors import VerifyNotStringListInternalError
            raise VerifyNotStringListInternalError(value)

    def _format_items(self, value: Union[TypeLike, CollectionOfTypeLike, Iterable[str]]):
        """
        Formátuje iterovatelný kontejner typových a řetězcových položek pro lepší čitelnost.

        Převede iterovatelný kontejner řetězců a typů na jeden řetězec,
        kde jsou jednotlivé položky odděleny čárkou a každá položka
        je ohraničena zpětnými apostrofy (`). Tato statická metoda je určena
        pro vytváření uživatelsky přívětivých výpisů seznamů
        v chybových zprávách.

        Args:
            value (Union[TypeLike, CollectionOfTypeLike]): Vstupní hodnota,
                buď samostatný typ, nebo řetězec, nebo tuple či seznam.

        Returns:
            str: Formátovaný řetězec s položkami oddělenými čárkami
                 a ohraničenými zpětnými apostrofy.

        Příklady:
        ---------
        ```python
        items = ["hodnota1", "jiná hodnota", "poslední"]
        formatted = VerifyError._format_str_items(items)
        print(formatted)
        # Výstup: `hodnota1`, `jiná hodnota`, `poslední`
        ```

        Poznámky:
        --------
        Tato metoda je statická, protože pro svou činnost nepotřebuje
        instanci třídy `VerifyError`. Je navržena pro jednoduché
        a konzistentní formátování seznamů řetězců.
        """
        str_list = self._ensure_string_list(value)
        return ", ".join(f"`{item}`" for item in str_list)

    def __str__(self) -> str:
        """
        Vrací řetězcovou reprezentaci výjimky.

        Přepisuje výchozí metodu __str__ třídy Exception,
        aby vracela předem připravenou zprávu.

        Returns:
            str: Formátovaná chybová zpráva.
        """
        return self.message