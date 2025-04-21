import os
import sys
import site
import traceback as tb
from typing import List

from .verify_internal_unexpected_error import VerifyInternalUnexpectedError


class GetSimplifiedTraceback:
    """
    Třída pro navrácení stručného výpisu uživatelského kódu z tracebacku.

    Poskytuje jednoduchý způsob, jak získat čitelný a přehledný výpis
    z aktuálního tracebacku nebo tracebacku vyvolané výjimky,
    vyfiltrovaného pouze na záznamy uživatelského kódu.

    Jedná se o definici tzv. „chytré funkce“ — tedy třídy,
    která obsahuje veškerou logiku pro vytvoření požadovaného výstupu.

    Třída je určena k internímu použití, např. pro vytváření chybových oznámení.
    """

    _title = "» Stručný přehled návazností (kód řádku → podrobnosti): \n"

    def __call__(self) -> List[str]:
        """
        Vytvoří a vrátí stručný výpis z tracebacku.

        Metoda nejprve načte záznamy z tracebacku.
        Pokud existují, vytvoří a vrátí seznam se všemi relevantními řádky.

        Returns:
            Seznam s řetězci pro jednotlivé texty oznámení.

        Raises:
            GetSimplifiedTracebackUnexpectedError:
                Interní výjimka zachytávající veškeré neočekávané chyby.
                Není předpoklad, že by mohl být vyvolán logický typ chyby.

        Hints:
            self._trace_lines - Property vracející seznam s upravenými řádky tracebacku nebo prázdný seznam.
            self._title - Atribut obsahující úvodní nadpis.
            self._get_end_line(is_empty) - Statická metoda vracející závěrečnou větu dle obsahu tracebacku.
        """
        try:
            traces = self._trace_lines
            is_empty = len(traces) == 0
            return [self._title] + traces + [self._get_end_line(is_empty)]

        except Exception as e:
            raise VerifyInternalUnexpectedError(
                info = f"Chyba nastala při generování zjednodušeného tracebacku.",
                modul = "Zachyceno v metodě __call__ třídy GetSimplifiedTraceback",
                original_exception = e
            ) from e

    @staticmethod
    def _get_end_line(is_empty: bool) -> str:
        """
        Vytvoří závěrečný řádek pro výpis tracebacku.

        Args:
            is_empty: Zda je traceback prázdný.

        Returns:
            Závěrečná zpráva pro výpis tracebacku.
        """
        if not is_empty:
            return "  (Odkazy k dispozici výše, v podrobném výpisu tracebacku.) \n"
        return "  (V tracebacku nebyl nalezen žádný odkaz na uživatelem vytvořený kód.) \n"

    @staticmethod
    def _trace_line(frame) -> str:
        """
        Vrátí naformátovaný řádek pro záznam z tracebacku.

        Args:
            frame: Záznam z tracebacku (jeden krok zásobníku).

        Returns:
            Upravený a naformátovaný řádek.

        Hints:
            frame.line - Kód nacházející se na daném řádku.
            frame.filename - Absolutní cesta k souboru.
            frame.lineno - Číslo řádku v souboru.
            frame.name - Název funkce, třídy nebo modulu (pokud není <module>).
            os.path.basename() - Vrací název souboru bez celé cesty.
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
        Vytvoří z tracebacku seznam řádků odkazující na kody uživatele.

        Returns:
            Seznam formátovaných řádků tracebacku.

        Hints:
            self._trace_line(frame) - Interní metoda pro naformátování jednoho řádku.
            for frame in self._stack_summary - Iterace záznamů z tracebacku.
            self._is_library_code() - Podmínka filtrování knihoven a balíčků.
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

        Returns:
            Objekt StackSummary obsahující záznamy volání.

        Hints:
            sys.exc_info() - Vrací aktuální výjimku (type, value, traceback).
            tb.extract_tb() - Vytáhne traceback ze záznamu výjimky.
            tb.extract_stack() - Vytáhne aktuální zásobník volání.
        """
        _, _, exc_tb = sys.exc_info()
        if exc_tb:
            return tb.extract_tb(exc_tb)
        return tb.extract_stack()

    @property
    def _ignore_paths(self) -> List[str]:
        """
        Vrací cesty, které se mají ignorovat při filtrování.

        Jedná se o cesty pro standardní knihovny a balíčky.
        Použito pro rozlišení interních záznamů od záznamů kodu uživatele.

        Returns:
            Seznam absolutních cest ke složkám, které mají být ignorovány.

        Hints:
            os.__file__ - Umístění standardní knihovny.
            site.getsitepackages() - Cesty pro systémové balíčky.
            site.getusersitepackages() - Cesta pro uživatelské balíčky.
            os.path.abspath() - Vrací absolutní cstu.
        """
        return [
            os.path.abspath(os.path.dirname(os.__file__)),
            *map(os.path.abspath, site.getsitepackages()),
            os.path.abspath(site.getusersitepackages())
        ]

    def _is_library_code(self, abs_file_path: str) -> bool:
        """
        Zkontroluje, zda cesta k souboru patří do knihovny nebo balíčku.

        Args:
            abs_file_path: Absolutní cesta k souboru.

        Returns:
            True pokud cesta patří do knihovny, jinak False.

        Hints:
            any(abs_file_path.startswith(path) for path in self._ignore_paths)
                - Kontrola, zda cesta začíná některou z ignorovaných.
        """
        return any(
            abs_file_path.startswith(path)
            for path in self._ignore_paths
        )

get_simplified_traceback = GetSimplifiedTraceback()