from typing import Callable, Union, Optional
from functools import wraps

from .manager_old import LocalManager, logger_settings
from .config import get_config
from .modes import (
    log_one_line,
    log_simple,
    log_detailed,
    log_report,
    mode_error,
)

# Vytvoření správce řádkování a odsazení
manager = LocalManager()

# Inicializace logeru
logger = logger_settings()

# Inicializace konfigurace
config = get_config()

# Definice dekorátoru
def log_this(
    mode: Optional[Union[bool, str, int]] = '',
) -> Callable:
    """
    Hlavní dekorátor pro logování funkcí s podporou různých režimů logování.

    Tento dekorátor umožňuje logování funkcí v několika režimech podle nastavené hodnoty `mode`:
    - False, None, 0, 'skip_this': Funkce nebude logována.
    - True, 1, 'one_line': Logování pouze názvu funkce a jejích vstupních parametrů.
    - 2, 'simple': Logování vstupních a výstupních parametrů.
    - 3, 'all': Logování vstupních a výstupních parametrů, doby běhu funkce a využití paměti.
    - 4, 'report': Podrobný report včetně analýzy prostředků a docstringu funkce.

    Args:
        mode (Optional[Union[bool, str, int]], optional): Režim logování. Pokud není nastaven, použije se výchozí konfigurace.
        config: Konfigurace pro logování (nastavení pro odsazení, prázdné řádky apod.).

    Returns:
        Callable: Funkce, která slouží jako dekorátor pro logování volání dekorované funkce.

    Notes:
        Režim logování je určen hodnotou `mode` a může být buď číslo, řetězec, nebo boolean.
        Dekorátor také využívá lokální proměnnou `thread_local` pro sledování hloubky volání funkce
        a správu logování na více úrovních v rámci více vláken.
    """

    # Kontrola, zda je mode celočíslenou hodnotu
    if not isinstance(mode, int):
        mode = config.values.get(mode, None)

    # Kontrola, zda je mode nastaven na přeskočení logování
    if mode == 0:
        return lambda func: func

    # Definice funkce dekorátoru
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):

            # Aktualizace hodnot manažera pro řádkování a odsazení
            manager.update_context(mode)

            # Zpracování logu
            try:

                # Načtení řádkování a odsazení
                indent = manager.get_indent()
                start_blank, end_blank = manager.get_blank_lines()

                # Zachycení výpisu na jeden řádek (pouze název a vstupní parametry)
                if mode in (1, 'one_line'):
                    return log_one_line(
                        logger, func, args, kwargs,
                        indent, start_blank, end_blank
                    )

                # Zachycení výpisu na čtyři řádky (přidává výstupní hodnotu)
                elif mode in (2, 'simple'):
                    return log_simple(
                        logger, func, args, kwargs,
                        indent, start_blank, end_blank
                    )

                # Zachycení výpisu na šest řádek (přidává dobu běhu a využití paměti)
                elif mode in (3, 'detailed'):
                    return log_detailed(
                        logger, func, args, kwargs,
                        indent, start_blank, end_blank
                    )

                # Zachycení plného výpisu (přidává analýzu prostředků a docstring)
                elif mode in (4, 'report'):
                    return log_report(
                        logger, func, args, kwargs,
                        indent, start_blank, end_blank, config.docstring_lines
                    )

                # Vyvolání výjimky, pokud nedošlo k zachycení modu
                else:
                    return mode_error(
                        logger, func, args, kwargs,
                        indent, start_blank, end_blank
                    )

            finally:
                # Dodatečná úprava hodnot manažera pro řádkování a odsazení
                manager.revert_context()

        return wrapper

    return decorator
