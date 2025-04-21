import os
import sys
import site
import traceback
from typing import Union, List, Tuple, Optional


class GetSimplifiedTracebackInputError(TypeError):
    """Výjimka pro kontrolu vstupních hodnot třídy GetSimplifiedTraceback."""

    title = "Zadán neplatný vstupní parametr pro GetSimplifiedTraceback. \n"

    def __init__(
            self,
            parameter: str,
            input_value: any,
            allowed_value: str,
            description: str
    ):
        """
        Inicializace výjimky pro kontrolu vstupních hodnot.

        Args:
            parameter: Název parametru, který způsobil výjimku
            input_value: Hodnota, která byla zadána
            allowed_value: Popis povolených hodnot
            description: Popis účelu parametru
        """
        self.parameter = parameter
        self.input_value = input_value
        self.allowed_value = allowed_value
        self.description = description
        self.message = (
                self.title
                + f"Vstupní parametr '{self.parameter}' \n"
                + f"Zadaná hodnota: {self.input_value} \n"
                + f"Povolené hodnoty: {self.allowed_value} \n"
                + f"Popis parametru: {self.description} \n"
        )
        super().__init__(self.message)

    def __str__(self) -> str:
        """Vrátí textovou reprezentaci výjimky."""
        return self.message


class GetSimplifiedTraceback:
    """
    Třída pro navrácení stručného výpisu z tracebacku.

    Poskytuje jednoduchý způsob, jak získat čitelný a stručný výpis
    z aktuálního tracebacku nebo tracebacku vyvolané výjimky.
    """

    _title = "» Stručný přehled návazností (kód řádku → podrobnosti):"

    def __init__(self):
        """Inicializace třídy GetSimplifiedTraceback."""
        self._lines_count = 0  # Parametr pro počítání řádek
        self._skip_lines = 2
        self._users_code_only = True
        self._lines_limit = False

    def __call__(
            self,
            skip_lines: int = 2,
            users_code_only: bool = True,
            lines_limit: Union[bool, int] = False
    ) -> Tuple[str, List[str], str]:
        """
        Vytvoří a vrátí stručný výpis z tracebacku.

        Args:
            skip_lines: Počet záznamů od konce, které se mají ve výpisu vynechat
            users_code_only: Určuje zda se mají vypsat pouze uživatelovo záznamy
            lines_limit: Omezení počtu vypsaných řádků (False = bez omezení)

        Returns:
            Tuple obsahující název výpisu, seznam řádků tracebacku a závěrečný řádek

        Raises:
            GetSimplifiedTracebackInputError: Pokud jakýkoliv vstupní parametr není validní
        """
        try:
            self._skip_lines = self._validate_skip_lines(skip_lines)
            self._users_code_only = self._validate_users_code_only(
                users_code_only)
            self._lines_limit = self._validate_lines_limit(lines_limit)
            self._lines_count = 0  # Reset počítadla řádků
            return self._get_simplified_traceback()
        except GetSimplifiedTracebackInputError as e:
            # Předání výjimky do vyšší úrovně
            raise e
        except Exception as e:
            # Pokud dojde k neočekávané chybě, zalogujeme ji a vrátíme prázdný výsledek
            print(
                f"Neočekávaná chyba při generování zjednodušeného tracebacku: {e}")
            return self._title, [], "Došlo k chybě při zpracování tracebacku."

    def _validate_skip_lines(self, skip_lines: int) -> int:
        """
        Ověří, že skip_lines je platné celé kladné číslo.

        Args:
            skip_lines: Hodnota k ověření

        Returns:
            Ověřená hodnota skip_lines

        Raises:
            GetSimplifiedTracebackInputError: Pokud skip_lines není celé kladné číslo
        """
        if not isinstance(skip_lines, int) or skip_lines < 0:
            raise GetSimplifiedTracebackInputError(
                parameter="skip_lines",
                input_value=skip_lines,
                allowed_value="Celé kladné číslo",
                description="Určuje počet záznamů od konce, "
                            "které se mají ve výpisu vynechat."
            )
        return skip_lines

    def _validate_users_code_only(self, users_code_only: bool) -> bool:
        """
        Ověří, že users_code_only je platná booleovská hodnota.

        Args:
            users_code_only: Hodnota k ověření

        Returns:
            Ověřená hodnota users_code_only

        Raises:
            GetSimplifiedTracebackInputError: Pokud users_code_only není boolean
        """
        if not isinstance(users_code_only, bool):
            raise GetSimplifiedTracebackInputError(
                parameter="users_code_only",
                input_value=users_code_only,
                allowed_value="True / False",
                description="Určuje zda se mají vypsat pouze uživatelovo záznamy, "
                            "nebo všechny."
            )
        return users_code_only

    def _validate_lines_limit(self, lines_limit: Union[bool, int]) -> Union[
        bool, int]:
        """
        Ověří, že lines_limit je platná hodnota.

        Args:
            lines_limit: Hodnota k ověření

        Returns:
            Ověřená hodnota lines_limit

        Raises:
            GetSimplifiedTracebackInputError: Pokud lines_limit není boolean nebo kladné číslo
        """
        if isinstance(lines_limit, bool):
            return lines_limit
        elif isinstance(lines_limit, int) and lines_limit >= 0:
            return lines_limit
        else:
            raise GetSimplifiedTracebackInputError(
                parameter="lines_limit",
                input_value=lines_limit,
                allowed_value="False pro všechny záznamy, "
                              "jinak celé kladné číslo pro definici počtu.",
                description="Určuje počet záznamů, které se mají vypsat."
            )

    def _get_simplified_traceback(self) -> Tuple[str, List[str], str]:
        """
        Vytvoří stručný výpis tracebacku.

        Returns:
            Tuple obsahující nadpis, seznam řádků tracebacku a závěrečnou zprávu
        """
        traces = self._trace_lines
        return (self._title, traces, self._get_end_line(len(traces) == 0))

    def _get_end_line(self, is_empty: bool) -> str:
        """
        Vytvoří závěrečný řádek pro výpis tracebacku.

        Args:
            is_empty: Zda je traceback prázdný

        Returns:
            Závěrečná zpráva pro výpis tracebacku
        """
        if is_empty:
            return "   (V tracebacku nebyl nalezen žádný odkaz na uživatelem vytvořený kód.)"
        else:
            return "  (Odkazy k dispozici výše, v podrobném výpisu tracebacku.)"

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
                # Podmínka kontrolující zda nedošlo k překročení počtu řádků
                if self._lines_limit_reached:
                    break

                # Podmínka kontrolující zda se má řádek vypsat
                if not self._skip_line(frame.filename):
                    trace_lines.append(
                        f"   - {frame.line}"
                        f" → [file: {os.path.basename(frame.filename)}]"
                        f" → [line: {frame.lineno}]"
                        +  # Pokud je uveden i modul, přidá se i tato informace
                        (
                            f" → [modul: {frame.name}]" if frame.name != "<module>" else "")
                    )

                    # Přípočet počítání řádků
                    self._lines_count += 1
        except Exception as e:
            # Pokud dojde k chybě při zpracování tracebacku, přidáme informaci o chybě
            trace_lines.append(f"   - Chyba při zpracování tracebacku: {e}")

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
            print(f"Chyba při získávání informací o tracebacku: {e}")
            return traceback.StackSummary.empty()

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
            print(f"Chyba při získávání cest pro ignorování: {e}")
            return []

    @property
    def _lines_limit_reached(self) -> bool:
        """
        Zkontroluje, zda bylo dosaženo limitu počtu řádků.

        Returns:
            True pokud byl limit dosažen, jinak False
        """
        return isinstance(self._lines_limit,
                          int) and self._lines_count >= self._lines_limit

    def _skip_line(self, abs_file_path: str) -> bool:
        """
        Určí, zda se má daný řádek přeskočit ve výpisu.

        Args:
            abs_file_path: Absolutní cesta k souboru

        Returns:
            True pokud se má řádek přeskočit, jinak False
        """
        try:
            # Pokud chceme jen uživatelský kód, přeskočíme řádky z knihoven
            if self._users_code_only:
                return self._is_library_code(abs_file_path)
            return False
        except Exception:
            # V případě chyby raději řádek nevynecháme
            return False

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
        except Exception:
            # V případě chyby raději předpokládáme, že jde o uživatelský kód
            return False