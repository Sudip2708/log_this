from abc import ABC
import os
import site
import sys
import traceback

from abc_helper import abc_property

class TraceLinesMixin(ABC):


    _skip_lines = abc_property("_skip_lines")
    _lines_limit = abc_property("_lines_limit")
    _lines_count = abc_property("_lines_count")
    _users_code_only = abc_property("_users_code_only")

    @property
    def _trace_lines(self):

        # Seznam na záznamy
        trace_lines = []

        # Cyklus přidávající položky seznamu
        for frame in self._stack_summary:

            # Podmínka kontrolující zda nedošlo k překročení poštu řádků
            if self._lines_limit_reached:
                break

            # Podmínka kontrolující zda se má řádek vypsat
            if not self._skip_line(frame.filename):
                trace_lines.append(
                    f"   - {frame.line}"
                    f" → [file: {os.path.basename(frame.filename)}]"  
                    f" → [line: {frame.lineno}]"
                    +  # Pokud je uveden i modul, přidá se i tato informace
                    f" → [modul: {frame.name}]"
                    if frame.name != "<module>"
                    else ""
                )

                # Přípočet počítání řádků
                self._lines_count += 1

        # Navrácení seznamu s řetězci
        return trace_lines

    @property
    def _stack_summary(self):
        # Získání aktuálního tracebacku (vyvolání výjimky/normální požadavek)
        _, _, tb_obj = sys.exc_info()  # Načtení info o případné výjimce
        return (
            traceback.extract_tb(tb_obj) if tb_obj  # Vrací stack, který vedl ke konkrétní výjimce
            else traceback.extract_stack()[:-self._skip_lines]  # Vrací aktuální volací zásobník v daném bodě
        )

    @property
    def _ignore_paths(self):
        """
        Cesty které se mají ignorovat pro vyfiltrování pouze uživatelských záznamů

        os.path.abspath(os.path.dirname(os.__file__)):
            - Tento řádek získává absolutní cestu k adresáři,
            kde se nachází standardní knihovna Pythonu.
            - To je důležité pro identifikaci rámců zásobníku,
            které pocházejí z vestavěných modulů Pythonu.

        *map(os.path.abspath, site.getsitepackages())
            - Tento řádek získává seznam absolutních cest k adresářům,
            kde jsou nainstalovány balíčky třetích stran
            (knihovny, které jsi si nainstaloval).
            - To zahrnuje jak globálně nainstalované balíčky,
            tak balíčky nainstalované ve tvém aktivním virtuálním prostředí.

        os.path.abspath(site.getusersitepackages())
            - Tento řádek získává absolutní cestu k adresáři,
            kde mohou být nainstalovány uživatelsky specifické balíčky.
        """
        return [
            os.path.abspath(os.path.dirname(os.__file__)),
            *map(os.path.abspath, site.getsitepackages()),
            os.path.abspath(site.getusersitepackages())
        ]

    @property
    def _lines_limit_reached(self):
        return self._lines_limit and self._lines_count > self._lines_limit

    def _skip_line(self, abs_file_path):
        return self._users_code_only and not self._is_user_code(abs_file_path)

    def _is_user_code(self, abs_file_path):
        return any(
            abs_file_path.startswith(path)
            for path in self._ignore_paths
        )




