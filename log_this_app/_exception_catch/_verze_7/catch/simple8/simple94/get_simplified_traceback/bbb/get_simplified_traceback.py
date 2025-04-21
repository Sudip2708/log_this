import os
import sys
import site
import traceback as tb
from typing import List


class GetSimplifiedTracebackUnexpectedError(Exception):
    pass


class GetSimplifiedTraceback:
    """
    Třída pro navrácení stručného výpisu z tracebacku pouze se záznami uživatelovo kodu.

    Poskytuje jednoduchý způsob, jak získat čitelný a stručný výpis
    z aktuálního tracebacku nebo tracebacku vyvolané výjimky,
    vyfiltrovaného pouze na záznamy uživatelov kodu.

    Jedná se o definici 'chytré funkce', tedy třídy,
    která obsahuje veškerou logiku pro navrácení daného výstupu.

    Tříde je určena k internímu použití, pro případ vytváření chybového oznamu.
    Použita v kodu:
    """

    _title = "» Stručný přehled návazností (kód řádku → podrobnosti):"

    def __call__(self) -> List[str]:
        """
        Vytvoří a vrátí stručný výpis z tracebacku.

        Metoda nejprve načte záznamy z tracebacku.
        Dále zkontroluje zda obsahují nějaký záznam (potřeba pro definici posledního řádku).
        Následně vytvoří a vrátí seznam se všemi řádky.

        Returns:
            Seznam s řetězci pro jednotlivé texty oznamu.

        Raises:
            GetSimplifiedTracebackInputError
                - Interní výjimka, která zachytává veškeré nečekané chyby.
                - Není předpoklad že by kod mohl vyvolal logickou výjimku.

        Hints:
            self._trace_lines - Property vracející seznam s upravenými řádky tracbacku a nebo prázdný seznam.
            self._title - Atribut obsahující úvodní nadpis.
            self._get_end_line(is_empty) - Property vracející závěrečnou větu.

        """
        try:
            traces = self._trace_lines
            is_empty = len(traces) == 0
            return [self._title] + traces + [self._get_end_line(is_empty)]

        except Exception as e:
            raise GetSimplifiedTracebackUnexpectedError(
                f"Neočekávaná chyba při generování zjednodušeného tracebacku. "
                f"Zachycena metodou self.__call__(): {e}"
            )

    @staticmethod
    def _get_end_line(is_empty: bool) -> str:
        """
        Vytvoří závěrečný řádek pro výpis tracebacku.

        Args:
            is_empty: Zda je traceback prázdný

        Returns:
            Závěrečná zpráva pro výpis tracebacku
        """
        if not is_empty:
            return "  (Odkazy k dispozici výše, v podrobném výpisu tracebacku.)"
        return "  (V tracebacku nebyl nalezen žádný odkaz na uživatelem vytvořený kód.)"

    @staticmethod
    def _trace_line(frame):
        """
        Vrátí naformátovaný řádek pro záznam z tracebacku.

        Args:
            frame: Záznam z tracebacku.

        Returns:
            Upravený a naformátovaný řádek.

        Hints:
            frame.line
                - Kod nacházející se na řádku pro který byl vytvořen záznam.
            os.path.basename()
                - Metoda pro záskání jména souboru z definice cesty.
            frame.filename
                - Absolutní cesta k souboru pro který byl vytvořen záznam.
            frame.lineno
                - Číslo řádku pro který byl vytvořen záznam.
            frame.name
                - Název modulu (třídy, metody, funkce) pro který byl vytvořen záznam.
                - Pokud jde o volně ložený kod a nemá tuto hodnotu, nezobrazuje se.
        """
        return (
            f"   - {frame.line}"
            f" → [file: {os.path.basename(frame.filename)}]"
            f" → [line: {frame.lineno}]"
            + (
            # Pokud je uveden i modul, přidá se i tato informace
                f" → [modul: {frame.name}]"
                if frame.name != "<module>"
                else ""
            )
        )

    @property
    def _trace_lines(self) -> List[str]:
        """
        Vytvoří seznam řádků s informacemi o jednotlivých voláních ve stacku, které se váží k uživatelovo kodu.

        Returns:
            Seznam formátovaných řádků tracebacku.

        Hints:
            self._trace_line(frame)
                - Interní metoda pro navrácení naformátovaného řádku.
            for frame in self._stack_summary
                - Cyklus procházející záznamy získané ze zásobníku.
            if not self._is_library_code(frame.filename)
                - Podmínka vyřazující záznamy které se nevztahují
                k uživatelem napsanému kodu.
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

        Metoda nejprve načte záznam o případné výjimce.
        A na jeho základě vrátí příslučný zásovník.

        Returns:
            Objekt StackSummary obsahující informace o tracebacku.

        Hints:
            sys.exc_info() -
            _, _, - Vynechání prvních dvou návratových hodnot (doplnit co reprezentují)
            exc_tb -
            tb - Zkrácený zápis (alias) pro knihovnu traceback
            extract_tb(exc_tb) -
            extract_stack() -
        """
        _, _, exc_tb = sys.exc_info()
        if exc_tb:
            return tb.extract_tb(exc_tb)
        return tb.extract_stack()


    @property
    def _ignore_paths(self) -> List[str]:
        """
        Získá cesty, které se mají ignorovat pro vyfiltrování pouze uživatelských záznamů.

        Returns:
            Seznam cest ke standardním knihovnám a nainstalovaným balíčkům.

        Hints:
            os.path.abspath() -
            os.path.dirname() -
            os.__file__ -
            *map() -
            site.getsitepackages() -
            site.getusersitepackages() -
        """
        return [
            os.path.abspath(os.path.dirname(os.__file__)),
            *map(os.path.abspath, site.getsitepackages()),
            os.path.abspath(site.getusersitepackages())
        ]


    def _is_library_code(self, abs_file_path: str) -> bool:
        """
        Zkontroluje, zda daná cesta k souboru patří do standardní knihovny nebo balíčků.


        Metoda prochází seznam s definicí absolutních cest,
        které se do výpisu nemají uvést, a porovnává je,
        zda začínají stejně jako aktuálně předaná absolutní cesta.

        Args:
            abs_file_path: Absolutní cesta k souboru.

        Returns:
            True pokud jde o kód ze standardní knihovny nebo balíčků,
            jinak False.

        Hints:
            abs_file_path.startswith(path)
                - Kontrola zda cesta začíná stejně jako cesta
                ze seznamu ignorovaných cest.
            for path in self._ignore_paths
                - Cyklus procházející seznam ignorovaných cest.
        """
        return any(
            abs_file_path.startswith(path)
            for path in self._ignore_paths
        )



