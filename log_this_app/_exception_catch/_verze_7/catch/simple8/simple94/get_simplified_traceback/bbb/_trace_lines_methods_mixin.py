import os
import sys
import site
import traceback
from typing import List


class TraceLinesMethodsMixin:

    @property
    def _trace_lines(self) -> List[str]:
        """
        Vytvoří seznam řádků s informacemi o jednotlivých voláních ve stacku.

        Returns:
            Seznam formátovaných řádků tracebacku
        """
        # Seznam na záznamy
        trace_lines = []

        try:
            # Cyklus přidávající položky seznamu
            for frame in self._stack_summary:

                # Podmínka kontrolující zda se má řádek vypsat
                if not self._is_library_code(frame.filename):
                    trace_lines.append(
                        f"   - {frame.line}"
                        f" → [file: {os.path.basename(frame.filename)}]"
                        f" → [line: {frame.lineno}]"
                        + (    # Pokud je uveden i modul, přidá se i tato informace
                            f" → [modul: {frame.name}]"
                            if frame.name != "<module>"
                            else ""
                        )
                    )

        except Exception as e:
            raise GetSimplifiedTracebackUnexpectedError(
                f"Neočekávaná chyba při generování zjednodušeného tracebacku. "
                f"Zachycena metodou self._trace_lines(): {e}"
            )

        # Navrácení seznamu s řetězci
        return trace_lines

    @property
    def _stack_summary(self) -> traceback.StackSummary:
        """
        Získá informace o aktuálním tracebacku nebo tracebacku výjimky.

        Returns:
            Objekt StackSummary obsahující informace o tracebacku
        """
        try:
            # Získání aktuálního tracebacku (vyvolání výjimky/normální požadavek)
            _, _, tb_obj = sys.exc_info()  # Načtení info o případné výjimce

            if tb_obj:
                # Vrací stack, který vedl ke konkrétní výjimce
                return traceback.extract_tb(tb_obj)
            else:
                # Vrací aktuální volací zásobník v daném bodě
                return traceback.extract_stack()[:-self._skip_lines]

        except Exception as e:
            raise GetSimplifiedTracebackUnexpectedError(
                f"Neočekávaná chyba při generování zjednodušeného tracebacku. "
                f"Zachycena metodou self._stack_summary(): {e}"
            )

    @property
    def _ignore_paths(self) -> List[str]:
        """
        Získá cesty, které se mají ignorovat pro vyfiltrování pouze uživatelských záznamů.

        Returns:
            Seznam cest ke standardním knihovnám a nainstalovaným balíčkům
        """
        try:
            return [
                os.path.abspath(os.path.dirname(os.__file__)),
                *map(os.path.abspath, site.getsitepackages()),
                os.path.abspath(site.getusersitepackages())
            ]

        except Exception as e:
            raise GetSimplifiedTracebackUnexpectedError(
                f"Neočekávaná chyba při generování zjednodušeného tracebacku. "
                f"Zachycena metodou self._ignore_paths(): {e}"
            )

    def _is_library_code(self, abs_file_path: str) -> bool:
        """
        Zkontroluje, zda daná cesta k souboru patří do standardní knihovny nebo balíčků.

        Args:
            abs_file_path: Absolutní cesta k souboru

        Returns:
            True pokud jde o kód ze standardní knihovny nebo balíčků, jinak False
        """
        try:
            # Pokud cesta začíná některou z cest v _ignore_paths, jde o knihovní kód
            return any(
                abs_file_path.startswith(path)
                for path in self._ignore_paths
            )

        except Exception as e:
            raise GetSimplifiedTracebackUnexpectedError(
                f"Neočekávaná chyba při generování zjednodušeného tracebacku. "
                f"Zachycena metodou self._is_library_code(): {e}"
            )

