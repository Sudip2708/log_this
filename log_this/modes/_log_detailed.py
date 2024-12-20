from typing import Callable, Any
import time
import inspect
import tracemalloc
from datetime import datetime

from .utils import (
    safe_serialize,
)


def log_detailed(
    logger,
    func: Callable,
    args: tuple,
    kwargs: dict,
    indent: str = "",
    start_blank: str = "",
    end_blank: str = ""
) -> Any:
    """
    Loguje podrobný report o průběhu volání funkce, včetně měření času, využití paměti,
    vstupních parametrů a výstupu.

    Args:
        logger: Logger pro logování zpráv.
        func (Callable): Funkce, jejíž volání je logováno.
        args (tuple): Argumenty předané logované funkci.
        kwargs (dict): Klíčové argumenty předané logované funkci.
        indent (str, optional): Řetězec pro odsazení logovací zprávy. Default je "".
        start_blank (str, optional): Řetězec přidaný na začátek zprávy pro prázdný řádek. Default je "".
        end_blank (str, optional): Řetězec přidaný na konec zprávy pro prázdný řádek. Default je "".

    Returns:
        Any: Výsledek volání původní dekorované funkce s předanými argumenty.

    Notes:
        Funkce loguje podrobné informace o průběhu volání, včetně času spuštění,
        cesty k souboru, vstupních parametrů, typu výstupu, doby trvání běhu, a
        využití paměti. Používá `tracemalloc` pro sledování rozdílů v paměti
        mezi začátkem a koncem volání funkce. Výsledky jsou zaznamenány ve formátu
        vhodném pro ladění a analýzu výkonu.
    """


    # Začátek měření běhu loggeru
    logger_time = time.perf_counter()

    # Úvodní zpráva
    logger.debug(f"{start_blank}{indent}"
                 f"# START LogThis('detailed') "
                 f"↓ {datetime.now()} "
                 f"↓ {func.__name__} ↓")
    logger.debug(f"{indent}"
                 f"# >>> File: {inspect.getfile(func)}")
    logger.debug(f"{indent}"
                 f"# >>> Input parameters: {safe_serialize(args)} "
                 f"| Input kwords: {safe_serialize(kwargs)}")

    # Spuštění tracemalloc pro měření paměti (pouze pokud ještě neběží)
    tracing_was_active = tracemalloc.is_tracing()
    if not tracing_was_active:
        tracemalloc.start()

    # Vytvoření záznamu paměti před spuštěním fuknce
    snapshot_before = tracemalloc.take_snapshot()

    # Zahájení měření času běhu funkce
    function_time = time.perf_counter()

    # Volání funkce
    try:
        result = func(*args, **kwargs)
        logger.debug(f"{indent}"
                     f"# >>> Outcome: {result} "
                     f"| Type: {type(result).__name__}")
        return result

    # Zachycení výjimky
    except Exception as e:
        logger.debug(f"{indent}"
                     f"# >>> Outcome: Raised exception {type(e).__name__}"
                     f": {str(e)}")
        raise

    # Dodatek
    finally:

        # Zaznamenání měření času běhu funkce
        function_duration = time.perf_counter() - function_time

        # Zpracování využití paměti
        snapshot_after = tracemalloc.take_snapshot()
        stats = snapshot_after.compare_to(snapshot_before, 'lineno')
        memory_used = sum(stat.size_diff for stat in stats)

        # Ukončení tracemalloc (pouze pokud nebyl aktivní před voláním)
        if not tracing_was_active:
            tracemalloc.stop()

        # Závěrečná zpráva
        logger.debug(f"{indent}"
                     f"# >>> Running time: {function_duration:.6f} sec "
                     f"| Memory usage: {memory_used} bytes")
        logger.debug(f"{indent}"
                     f"# END LogThis('detailed') ↑ {func.__name__}' "
                     f"↑ Log duration: {time.perf_counter() - logger_time:.6f} "
                     f"sec ↑{end_blank}")
