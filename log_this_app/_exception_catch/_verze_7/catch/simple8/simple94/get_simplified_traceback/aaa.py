from typing import Union

class GetSimplifiedTracebackInputError(TypeError):
    """Víjimka pro kontolu vstupních hodnot třídy GetSimplifiedTraceback"""

    title = "Zadán neplatný vstupní parametr pro GetSimplifiedTraceback. \n"

    def __init__(
            self,
            parameter: str,
            input_value: str,
            allowed_value: str,
            description: str
    ):
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

    def __str__(self):
        return self.message

def _get_skip_lines(skip_lines):
    if not isinstance(skip_lines, int) and skip_lines < 0:
        raise GetSimplifiedTracebackInputError(
            parameter="skip_lines",
            input_value=skip_lines,
            allowed_value="Celé kladné číslo",
            description="Určuje počet záznamů od konce, "
                        "které se mají ve výpisu vynechat."
        )
    return skip_lines


def _get_users_code_only(users_code_only):
    if not isinstance(users_code_only, bool):
        raise GetSimplifiedTracebackInputError(
            parameter="users_code_only",
            input_value=users_code_only,
            allowed_value="True / False",
            description="Určuje zda se mají vypsat pouze uživatelovo záznamy, "
                        "nebo všechny."
        )
    return users_code_only


def _get_lines_limit(lines_limit):
    if not isinstance(lines_limit, bool) or (
            not isinstance(lines_limit, int) and lines_limit < 0
    ):
        raise GetSimplifiedTracebackInputError(
            parameter="lines_limit",
            input_value=lines_limit,
            allowed_value="False pro všechny záznamy, "
                          "jinak celé kladné číslo pro definici počtu.",
            description="Určuje počet záznamů, které se mají vypsat."
        )
    return lines_limit


class GetSimplifiedTraceback:
    """
    Třída pro navrácení stručného výpisu z tracebacku.
    """

    _title = "» Stručný přehled návazností (kód řádku → podrobnosti):"
    _lines_count = 0  # Parametr pro počítání řádek

    def __call__(
            self,
            skip_lines: int = 2,
            users_code_only: bool = True,
            lines_limit: Union[bool, int] = False
    ):
        self._skip_lines = _get_skip_lines(skip_lines)
        self._users_code_only = _get_users_code_only(users_code_only)
        self._lines_limit = _get_lines_limit(lines_limit)
        self._get_simplified_traceback()

    def _get_simplified_traceback(self):
        return (
            self._title, self._trace_lines, self._end_line
        )

    @property
    def _end_line(self):
        # Přidání poslední řádky
        return (
            "   (V tracebacku nebyl nalezen žádný odkaz na uživatelem vytvořený kód.)"
            if self._lines_count
            else "  (Odkazy k dispozici výše, v podrobném výpisu tracebacku.)"
        )

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
            traceback.extract_tb(
                tb_obj) if tb_obj  # Vrací stack, který vedl ke konkrétní výjimce
            else traceback.extract_stack()[:-self._skip_lines]
        # Vrací aktuální volací zásobník v daném bodě
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
