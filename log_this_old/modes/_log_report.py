from typing import Callable, Any
import logging
import time
import inspect
import tracemalloc
from datetime import datetime


def log_report(
    logger: logging.Logger,
    func: Callable[..., Any],
    args: tuple,
    kwargs: dict,
    serialize: Callable[..., Any],
    get_limited_docstring: Callable[..., str],
    indent: str = "",
    start_blank: str = "",
    end_blank: str = "",
) -> Any:
    """
    Loguje podrobný report o průběhu volání funkce, včetně anotací, vstupních parametrů,
    výstupu, doby běhu a využití paměti. Tento režim je určen pro získání podrobného přehledu
    o výkonu a paměťové náročnosti funkce.

    Args:
        logger (logging.Logger): Logger pro logování zpráv.
        func (Callable): Funkce, jejíž volání je logováno.
        args (tuple): Argumenty předané logované funkci.
        kwargs (dict): Klíčové argumenty předané logované funkci.
        serialize (Callable): Metoda pro serializaci hodnot.
        get_limited_docstring (Callable): Metoda pro navrácení přizpůsobeného docstringu.
        indent (str, optional): Řetězec pro odsazení logovací zprávy. Default je "".
        start_blank (str, optional): Řetězec přidaný na začátek zprávy pro prázdný řádek. Default je "".
        end_blank (str, optional): Řetězec přidaný na konec zprávy pro prázdný řádek. Default je "".

    Returns:
        Any: Výsledek volání původní funkce s předanými argumenty.

    Notes:
        Funkce loguje podrobné informace o průběhu volání, včetně cesty k souboru, anotací
        funkce, vstupních parametrů, doby běhu, využití paměti, a případného výstupu či výjimky.
        Využívá `tracemalloc` pro sledování změn v paměti během běhu funkce. Výsledky jsou zaznamenány
        pro účely ladění a analýzy výkonu a efektivity.
    """


    # Začátek měření běhu loggeru
    logger_time = time.perf_counter()

    # Úvodní zpráva
    logger.debug(f"{start_blank}{indent}"
                 f"# START LogThis('report') "
                 f"↓ {datetime.now()} "
                 f"↓ {func.__name__} ↓")

    # Cesta k souboru
    logger.debug(f"{indent}"
                 f"# >>> File: {inspect.getfile(func)}")

    # Anotace
    logger.debug(f"{indent}" 
                 f"# >>> Annotations: "
                 f"{func.__annotations__ if func.__annotations__ else 'N/A'}")

    # Vstupní parametry
    logger.debug(f"{indent}"
                 f"# >>> Input parameters: {serialize(args)} "
                 f"| Input kwords: {serialize(kwargs)}")

    # Prvních 3 řádků z docstringu
    logger.debug(f"{indent}"
                 f"# >>> Docstring: {get_limited_docstring(func.__doc__)}")

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

        # Info o době běhu a využití paměti
        logger.debug(f"{indent}"
                     f"# >>> Running time: {function_duration:.6f} sec "
                     f"| Memory usage: {memory_used} bytes")

        # Výpis využití paměti
        if len(stats) > 0:
            logger.debug(f"{indent}"
                         f"# >>> Memory allocation listing:")
            for stat in stats:
                logger.debug(f"{indent}"
                             f"# >>> > Allocated: {stat.size_diff} bytes, "
                             f"Line: {stat.traceback[0].lineno}, "
                             f"File: {stat.traceback[0].filename}")

        # Závěrečná zpráva
        logger.debug(f"{indent}"
                     f"# END LogThis('report') ↑ {func.__name__}' "
                     f"↑ Log duration: {time.perf_counter() - logger_time:.6f} "
                     f"sec ↑{end_blank}")
