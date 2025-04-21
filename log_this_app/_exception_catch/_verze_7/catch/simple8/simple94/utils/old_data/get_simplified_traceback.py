import traceback
import sys
import os
from typing import Union

from .is_user_code import is_user_code
from ..exceptions import VerifyUnexpectedError


def get_simplified_traceback(
        skip_lines: int = 2,
        users_code_only: bool = True,
        lines_limit: Union[bool, int] = False
):
    """Vrátí zjednodušený traceback se zohledněním systémových záznamů.

    Args:
        skip_lines (int): Počet řádků od konce stacku, které budou odebrány (např. volání této funkce).
        users_code_only (bool): Pokud True, vrací pouze záznamy patřící do uživatelského kódu.
        lines_limit (Union[bool, int]): Pokud False, vypisují se všechny záznamy, jinak dle číselné reprezentace hodnoty.

    Returns:
        List[str]: Seznam zjednodušených řádků tracebacku.
    """

    # Ověření vstupu
    if not isinstance(skip_lines, int) and skip_lines < 0:
        raise TypeError(
            "Vstupní parametr 'skip_lines' pro funkci 'get_simplified_traceback', "
            "které určuje počet řádků od konce které se mají vynechat, "
            "musí být celé kladné číslo!"
        )
    if not isinstance(users_code_only, bool):
        raise TypeError(
            "Vstupní parametr 'users_code_only' pro funkci 'get_simplified_traceback', "
            "který určuje, zda se mají vypsat pouze záznamy pro uživatelovo kod, "
            "musí být bool!"
        )
    if not isinstance(lines_limit, bool) or (not isinstance(lines_limit, int) and skip_lines < 0):
        raise TypeError(
            "Vstupní parametr 'lines_limit' pro funkci 'get_simplified_traceback', "
            "který určuje, zda se mají vyspat všechny záznamy nebo jen některé, "
            "musí být bool a nebo celé kladné číslo určující počet záznamů, které se vypíší!"
        )


    try:

        # Získání aktuálního tracebacku (vyvolání výjimky/normální požadavek)
        _, _, tb_obj = sys.exc_info()  # Načtení info o případné výjimce
        stack_summary = (
            traceback.extract_tb(tb_obj) if tb_obj  # Vrací stack, který vedl ke konkrétní výjimce
            else traceback.extract_stack()[:-skip_lines]  # Vrací aktuální volací zásobník v daném bodě
        )

        # Vytvoření seznamu s úvodem
        trace_lines = ["» Stručný přehled návazností (kód řádku → podrobnosti):"]
        lines_count = 0  # Parametr pro počítání řádek

        # Cyklus přidávající položky seznamu
        for frame in stack_summary:

            # Podmínka kontrolující zda nedošlo k překročení poštu řádků
            if lines_limit and lines_count > lines_limit:
                break

            # Podmínka kontrolující zda se mají vypysovat jen uživatelské záznami
            if not users_code_only or is_user_code(frame.filename):
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
            lines_count += 1

        # Přidání poslední řádky
        trace_lines.append(
            "   (Ve výše uvedeném tracebacku nebyl nalezen žádný odkaz na uživatelem vytvořený kód.)"
            if lines_count
            else "  (Odkazy k dispozici výše, v podrobném výpisu tracebacku.)"
        )

        # Návratová hodnota je seznam obsahující řetězce jednotlivých řádků
        return trace_lines

    # Ošetření případů, kdy by samotná funkce způsobila chybu
    except Exception as e:
        raise VerifyUnexpectedError(
            f"Neočekávaná chyba zachycená ve funkci 'get_simplified_traceback' "
            f"při generování zjednodušeného tracebacku: {e}"
        )