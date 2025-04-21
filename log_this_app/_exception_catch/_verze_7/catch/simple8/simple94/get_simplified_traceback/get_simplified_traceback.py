
from typing import Union

from ._input_validations import (
    _get_skip_lines,
    _get_users_code_only,
    _get_lines_limit
)
from ._trace_lines_mixin import TraceLinesMixin


class GetSimplifiedTraceback(TraceLinesMixin):
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

    @property
    def _end_line(self):
        # Přidání poslední řádky
        return (
            "   (V tracebacku nebyl nalezen žádný odkaz na uživatelem vytvořený kód.)"
            if self._lines_count
            else "  (Odkazy k dispozici výše, v podrobném výpisu tracebacku.)"
        )

    def _get_simplified_traceback(self):
        return (
            self._title, self._trace_lines, self._end_line
        )


get_user_stack_text = GetSimplifiedTraceback()
