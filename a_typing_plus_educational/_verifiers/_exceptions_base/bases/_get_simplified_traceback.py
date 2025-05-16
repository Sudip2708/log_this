import os
import sys
import site
import traceback as tb
from typing import List

from .verify_internal_unexpected_error import VerifyUnexpectedInternalError


class GetSimplifiedTraceback:
    """
    Třída pro navrácení stručného výpisu uživatelského kódu z tracebacku.

    Tato třída implementuje mechanismus pro extrakci a formátování relevantních
    částí tracebacku, který je zaměřen pouze na uživatelský kód. Výsledkem je
    přehledný výpis, který pomáhá uživatelům lépe pochopit kontext chyby.

    Klíčové koncepty:
    -----------------
    * Traceback filtrace - Odfiltrování systémových a knihovních volání z výpisu
    * Callables třída - Implementace třídy s metodou __call__, která se chová jako funkce
    * Kontext výjimky - Získání tracebacku z aktivní výjimky nebo aktuálního stavu

    Architekturální kontext:
    -----------------------
    Tato třída je součástí systému zpracování chyb knihovny a poskytuje
    infrastrukturu pro vytváření uživatelsky přívětivých chybových hlášení.
    Je navržena jako singleton instance (get_simplified_traceback), která se
    používá ve všech typech výjimek knihovny.

    Detaily implementace:
    --------------------
    * Třída využívá Python modul `traceback` pro získání záznamu o volání
    * Pro rozlišení uživatelského a systémového kódu se kontrolují cesty k souborům
    * Implementace využívá property pro lepší přehlednost a organizaci kódu
    * Výsledek je vrácen jako seznam řetězců pro flexibilní sestavení chybové zprávy

    Poznámky k rozšíření:
    --------------------
    * Při rozšiřování této třídy je vhodné zachovat stejný přístup k filtrování cest
    * Pro změnu formátu výstupu lze upravit metodu `_trace_line`
    * Při potřebě dalších informací z tracebacku je možné rozšířit metody pracující s `frame`
    """

    _title = "» Stručný přehled návazností (kód řádku → podrobnosti): \n"

    def __call__(self) -> List[str]:
        """
        Vytvoří a vrátí stručný výpis z tracebacku.

        Tato metoda implementuje rozhraní pro získání uživatelsky přívětivého výpisu
        z aktuálního tracebacku. Transformuje technické informace o zásobníku volání
        na srozumitelný výpis, který obsahuje pouze relevantní uživatelský kód.

        Algoritmus:
        ----------
        1. Získání řádků tracebacku pomocí property `_trace_lines`
        2. Kontrola, zda byly nalezeny nějaké relevantní řádky
        3. Sestavení výstupu včetně nadpisu a závěrečné poznámky
        4. Zachycení a předání neočekávaných chyb

        Returns:
            List[str]: Seznam řetězců obsahující formátovaný výpis tracebacku.
                       Prvním prvkem je nadpis, následují záznamy z tracebacku
                       a poslední prvek je závěrečná poznámka.

        Raises:
            VerifyUnexpectedInternalError: Pokud dojde k neočekávané chybě při
                                         zpracování tracebacku. Tato výjimka
                                         obaluje původní výjimku pro konzistentní
                                         zpracování chyb v rámci knihovny.

        Souvislosti:
        -----------
        Tato metoda je volána při vytváření chybových hlášení v systému výjimek
        knihovny a poskytuje kontext pro lokalizaci zdroje problému.
        """
        try:
            traces = self._trace_lines
            is_empty = len(traces) == 0
            return [self._title] + traces + [self._get_end_line(is_empty)]

        except Exception as e:
            raise VerifyUnexpectedInternalError(e) from e

    @staticmethod
    def _get_end_line(is_empty: bool) -> str:
        """
        Vytvoří závěrečný řádek pro výpis tracebacku.

        Generuje vhodnou závěrečnou poznámku pro výpis tracebacku v závislosti
        na tom, zda byly nalezeny nějaké relevantní řádky kódu.

        Args:
            is_empty (bool): Příznak indikující, zda je traceback prázdný.

        Returns:
            str: Formátovaná závěrečná zpráva pro výpis tracebacku.

        Souvislosti:
        -----------
        Tato metoda doplňuje výpis tracebacku o závěrečnou poznámku, která
        uživateli poskytuje dodatečný kontext ohledně přítomnosti nebo
        absence uživatelského kódu v tracebacku.
        """
        if not is_empty:
            return "  (Odkazy k dispozici výše, v podrobném výpisu tracebacku.) \n"
        return "  (V tracebacku nebyl nalezen žádný odkaz na uživatelem vytvořený kód.) \n"

    @staticmethod
    def _trace_line(frame) -> str:
        """
        Vrátí naformátovaný řádek pro záznam z tracebacku.

        Transformuje technické informace o jednom záznamu tracebacku
        na čitelný a informativní řetězec, který obsahuje kód řádku,
        název souboru, číslo řádku a název modulu.

        Args:
            frame: Objekt FrameSummary obsahující informace o jednom kroku zásobníku.

        Returns:
            str: Formátovaný řetězec obsahující relevantní informace o kroku zásobníku.

        Algoritmus:
        ----------
        1. Extrakce kódu řádku, názvu souboru a čísla řádku z frame objektu
        2. Formátování těchto informací do čitelného a strukturovaného řetězce
        3. Volitelné přidání informace o modulu, pokud není <module>

        Pokročilé koncepty:
        -----------------
        * FrameSummary - Speciální datová třída pro reprezentaci jednoho kroku zásobníku
        * os.path.basename - Extrakce pouze názvu souboru z absolutní cesty
        """
        return (
            f"   - {frame.line}"
            f" → [file: {os.path.basename(frame.filename)}]"
            f" → [line: {frame.lineno}]"
            + (
                f" → [modul: {frame.name}]" if frame.name != "<module>" else ""
            ) + "\n"
        )

    @property
    def _trace_lines(self) -> List[str]:
        """
        Vytvoří z tracebacku seznam řádků odkazující na kód uživatele.

        Metoda filtruje traceback tak, aby obsahoval pouze záznamy týkající se
        uživatelského kódu (tedy ne systémové knihovny a balíčky). Pro každý
        relevantní záznam vytvoří formátovaný řetězec.

        Returns:
            List[str]: Seznam formátovaných řádků tracebacku vztahujících se
                       k uživatelskému kódu.

        Algoritmus:
        ----------
        1. Iterace přes všechny záznamy v tracebacku (`_stack_summary`)
        2. Filtrování záznamů pomocí metody `_is_library_code`
        3. Transformace relevantních záznamů pomocí metody `_trace_line`

        Souvislosti:
        -----------
        Tato property je klíčovou částí implementace, která provádí filtraci
        a formátování dat tracebacku. Pracuje s výstupem z `_stack_summary`
        a poskytuje data pro metodu `__call__`.
        """
        return [
            self._trace_line(frame)
            for frame in self._stack_summary
            if not self._is_library_code(frame.filename)
        ]

    @property
    def _stack_summary(self) -> tb.StackSummary:
        """
        Získá informace o aktuálním tracebacku nebo tracebacku výjimky.

        Tato property detekuje, zda je k dispozici traceback aktivní výjimky,
        a pokud ano, použije jej. V opačném případě získá aktuální zásobník volání.

        Returns:
            tb.StackSummary: Objekt obsahující záznamy o krocích zásobníku volání.

        Algoritmus:
        ----------
        1. Kontrola, zda je k dispozici traceback aktivní výjimky pomocí `sys.exc_info()`
        2. Pokud ano, extrakce tracebacku pomocí `tb.extract_tb()`
        3. Pokud ne, extrakce aktuálního zásobníku volání pomocí `tb.extract_stack()`

        Pokročilé koncepty:
        -----------------
        * sys.exc_info() - Nízkoúrovňový přístup k informacím o aktuální výjimce
        * StackSummary - Datová struktura pro reprezentaci zásobníku volání
        * extract_tb/extract_stack - Utility pro extrakci zásobníku z různých zdrojů
        """
        _, _, exc_tb = sys.exc_info()
        if exc_tb:
            return tb.extract_tb(exc_tb)
        return tb.extract_stack()

    @property
    def _ignore_paths(self) -> List[str]:
        """
        Vrací cesty, které se mají ignorovat při filtrování.

        Tato property poskytuje seznam cest k systémovým knihovnám a balíčkům,
        které mají být ignorovány při filtrování tracebacku. Tyto cesty jsou
        používány metodou `_is_library_code` pro rozlišení uživatelského kódu
        od systémového.

        Returns:
            List[str]: Seznam absolutních cest ke složkám, které mají být ignorovány.

        Algoritmus:
        ----------
        1. Získání cesty ke standardní knihovně Pythonu pomocí `os.__file__`
        2. Získání cest k systémovým balíčkům pomocí `site.getsitepackages()`
        3. Získání cesty k uživatelským balíčkům pomocí `site.getusersitepackages()`
        4. Převedení všech cest na absolutní cesty pomocí `os.path.abspath()`

        Pokročilé koncepty:
        -----------------
        * os.__file__ - Speciální atribut modulu označující cestu k jeho souboru
        * site.getsitepackages() - Funkce pro získání systémových cest balíčků
        * site.getusersitepackages() - Funkce pro získání uživatelských cest balíčků
        * Absolutní vs. relativní cesty - Použití absolutních cest pro spolehlivé porovnání
        """
        return [
            os.path.abspath(os.path.dirname(os.__file__)),
            *map(os.path.abspath, site.getsitepackages()),
            os.path.abspath(site.getusersitepackages())
        ]

    def _is_library_code(self, abs_file_path: str) -> bool:
        """
        Zkontroluje, zda cesta k souboru patří do knihovny nebo balíčku.

        Tato metoda rozhoduje, zda daný soubor patří do standardní knihovny
        nebo nainstalovaného balíčku, nebo zda se jedná o uživatelský kód.
        Používá se pro filtrování tracebacku.

        Args:
            abs_file_path (str): Absolutní cesta k souboru.

        Returns:
            bool: True pokud cesta patří do knihovny nebo balíčku, jinak False.

        Algoritmus:
        ----------
        1. Kontrola, zda cesta začíná některou z ignorovaných cest
        2. Využití funkce `any` pro efektivní testování všech cest

        Souvislosti:
        -----------
        Tato metoda je klíčová pro filtrování tracebacku v metodě `_trace_lines`.
        Poskytuje logiku pro rozlišení uživatelského a systémového kódu.
        """
        return any(
            abs_file_path.startswith(path)
            for path in self._ignore_paths
        )

get_simplified_traceback = GetSimplifiedTraceback()